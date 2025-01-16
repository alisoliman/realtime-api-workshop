"""Service for managing AI assistants."""

import json
import re
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class AssistantService:
    """A service for managing AI assistants and their interactions."""

    def __init__(self, language: str = "English"):
        self.language = language
        self.agents = {}

    def get_tools_for_assistant(self, id):
        """Retrieve tools for a specific assistant."""
        return [
            {
                "type": "function",
                "name": tool["name"],
                "parameters": tool["parameters"],
                "description": tool["description"],
            }
            for tool in self.agents[id]["tools"]
        ]

    def register_agent(self, agent):
        """Register a new agent in the service."""
        agent["system_message"] = self.format_string(
            agent["system_message"], {"language": self.language}
        )
        self.agents[agent["id"]] = agent
        # Also register as root for compatibility
        self.agents["root"] = agent

    def get_agent(self, id):
        """Retrieve an agent by its ID."""
        return self.agents.get(id)

    async def get_tool_response(self, tool_name, parameters, call_id):
        """Execute a tool and return its response."""
        logger.debug(
            f"getToolResponse: tool_name={tool_name}, parameters={parameters}, call_id={call_id}"
        )

        # Find the tool in any agent
        tool = None
        for agent in self.agents.values():
            for t in agent["tools"]:
                if t["name"] == tool_name:
                    tool = t
                    break
            if tool:
                break

        if not tool:
            logger.error(f"Tool {tool_name} not found")
            return None

        # Execute tool
        content = tool["returns"](parameters)
        logger.debug(f"Tool {tool_name} returned content: {content}")

        response = {
            "type": "conversation.item.create",
            "item": {
                "type": "function_call_output",
                "call_id": call_id,
                "output": content,
            },
        }
        return response

    def format_string(self, text, params):
        """Format a string with given parameters."""
        if not text:
            return text
        return text.format(**params)
