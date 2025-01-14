import json
import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

class AssistantService:
    """A service for managing AI assistants and their interactions.
    
    This service handles the registration, configuration, and coordination of multiple AI assistants,
    including their tools and inter-assistant communication capabilities. It supports a hierarchical
    structure where assistants can delegate tasks to other assistants.
    
    Args:
        language (str, optional): The primary language for assistant communications. Defaults to "English".
    """
    
    def __init__(self, language: str = "English"):
        self.language = language
        self.agents = {}
  
    def get_tools_for_assistant(self, id):
        """Retrieve all available tools for a specific assistant.
        
        This method combines the assistant's own tools with other assistants represented as tools,
        enabling inter-assistant communication and task delegation.
        
        Args:
            id (str): The unique identifier of the assistant
            
        Returns:
            list: A list of tool definitions including both real tools and other assistants as tools
        """
        # Get tools for agent
        # This includes the agent's own tools and other agents as tools
        agent_real_tools = self.agents[id]['tools']
        other_agents_as_tools = [
            {
                'name': ag['id'],
                'description': ag['description'],
                'parameters': {
                    'type': 'object',
                    'properties': {}
                },
                'returns': lambda foo: ag['id']
            }
            for k, ag in self.agents.items() if k != id
        ]

        tools_definitions = [
            {
                'type': 'function',
                'name': tool['name'],
                'parameters': tool['parameters'],
                'description': tool['description']
            }
            for tool in agent_real_tools + other_agents_as_tools
        ]
        return tools_definitions

    def register_agent(self, agent):
        """Register a new agent in the service.
        
        This method adds a new agent to the service, formatting its system message
        with the configured language.
        
        Args:
            agent (dict): Agent configuration including ID, system message, and tools
        """
        agent['system_message'] = self.format_string(agent['system_message'], {'language': self.language})
        self.agents[agent['id']] = agent

    def get_agent(self, id):
        """Retrieve an agent by its ID.
        
        Args:
            id (str): The unique identifier of the agent
            
        Returns:
            dict: The agent configuration if found, None otherwise
        """
        return self.agents.get(id)

    def register_root_agent(self, root_agent):
        """Register the root agent and configure inter-agent communication.
        
        This method:
        1. Adds a tool to all other agents to switch back to the root agent
        2. Registers the root agent both under its ID and under "root"
        3. Formats the root agent's system message with the configured language
        
        Args:
            root_agent (dict): Root agent configuration including ID, system message, and tools
        """
        # Ensure every other agent has a tool to switch back to the root agent
        for k, ag in self.agents.items():
            ag['tools'].append({
                'name': root_agent['id'],
                'description': f"If customer asks any question that is outside of your work scope, DO use this to switch back to {root_agent['id']}.",
                'parameters': {
                    'type': 'object',
                    'properties': {}
                },
                'returns': lambda arg: root_agent['id']
            })

        # Register root agent, also with "root" key
        root_agent['system_message'] = self.format_string(root_agent['system_message'], {'language': self.language})
        self.agents["root"] = self.agents[root_agent['id']] = root_agent

    async def get_tool_response(self, tool_name, parameters, call_id):
        """Execute a tool or switch to another agent based on the tool name.
        
        This method handles both actual tool execution and inter-agent switching.
        For agent switches, it configures the new agent's session with appropriate
        tools and instructions.
        
        Args:
            tool_name (str): Name of the tool to execute or agent to switch to
            parameters (dict): Parameters for the tool execution
            call_id (str): Unique identifier for the tool call
            
        Returns:
            dict: Tool execution result or agent switch configuration
        """
        print(f"getToolResponse: tool_name={tool_name}, parameters={parameters}, call_id={call_id}")
        
        # Invoked tool is either a real tool or an agent
        all_tools = [tool for ag in self.agents.values() for tool in ag['tools']]
        all_agents_as_tools = [
            {
                'name': ag['id'],
                'description': ag['description'],
                'parameters': {'type': 'object', 'properties': {}},
                'returns': lambda foo: ag['id']
            }
            for ag in self.agents.values()
        ]
        tools = all_tools + all_agents_as_tools
        
        # Get tool by name
        tool = next((t for t in tools if t['name'] == tool_name), None)
        
        # Execute tool
        # If tool_name matches "assistant", it means we are switching to another agent
        if re.search(r'assistant', tool_name, re.IGNORECASE):
            agent = self.agents[tool_name]
            logger.debug(f"Switching to agent {agent['id']}")
            config_message = {
                'type': 'session.update',
                'session': {
                    'turn_detection': {
                        'type': 'server_vad'
                    },
                    'instructions': self.format_string(agent['system_message'], {'language': self.language}),
                    # NOTE we dont' simply use agent['tools'] here because we want to include other agents as tools
                    'tools': self.get_tools_for_assistant(tool_name)
                }
            }
            return config_message
        else:            
            # TODO check if tool.returns() may be a coroutine and use await if necessary
            content = tool['returns'](parameters)
            logger.debug(f"Tool {tool_name} returned content: {content}")
            response = {
                'type': 'conversation.item.create',
                'item': {
                    'type': 'function_call_output',
                    'call_id': call_id,
                    'output': content
                }
            }
            return response

    def format_string(self, text, params):
        """Format a string with given parameters.
        
        Args:
            text (str): The template string to format
            params (dict): Parameters to insert into the template
            
        Returns:
            str: The formatted string
        """
        # TODO additional logic may be added here, 
        # like providing common instructions for all agents to follow voice-specific guidelines
        return text.format(**params)
