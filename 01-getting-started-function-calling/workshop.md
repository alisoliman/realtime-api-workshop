# Workshop: Building a Realtime Voice Assistant with Chainlit

Welcome to our workshop on creating a **voice-enabled assistant** using [Chainlit](https://docs.chainlit.io/) and Azure OpenAI's Realtime API. The main goal is to show how to:
- Accept **live audio** and **text** input from users
- Integrate **Azure OpenAI** for conversational AI
- Demonstrate **function calling** and **tool usage** in a practical setting

We'll walk through the key components of the workshop's codebase and highlight how each piece fits together. Note that there's a file called `realtime2.py` containing many low-level helper functions, which we won't go into detail about. It primarily deals with the underlying websocket connections, streaming audio, and conversation event handling.

## Project Structure

Below is a simplified layout of the main files you'll see in this workshop:

```
realtime-api-workshop/
├── 01-getting-started-function-calling/  # Workshop folder for function calling examples
│   ├── .env                                  # Azure OpenAI API keys and endpoint 
│   ├── chat.py                          # Main application script
│   ├── realtime2.py                     # Azure OpenAI realtime client implementation
│   └── assistant_service.py             # Assistant management and tool handling
```

### `chat.py`
This is the **main application file** demonstrating how to:
1. **Initialize** Chainlit and create a user session
2. **Set up** a realtime client (`RealtimeClient`) for audio input/output
3. **Register** handlers for text messages and audio data
4. **Route** user queries to the correct assistant tools or functions

Chainlit callbacks (`@cl.on_chat_start`, `@cl.on_message`, etc.) manage the flow of user interactions. For example:
- `@cl.on_message` handles **text** input
- `@cl.on_audio_start`, `@cl.on_audio_chunk`, and `@cl.on_audio_end` handle **audio** streaming
- `@cl.on_chat_end` and `@cl.on_stop` ensure that resources are properly cleaned up

### `assistant_service.py`
A dedicated service for managing AI assistants and their tools. While this service supports multiple agents, **for this workshop we'll focus on a single technical support agent**. Multi-agent scenarios will be explored in the `02-building-multi-agent-system` module.

The service provides:
- **Agent Management**: Registers and configures our technical support assistant
- **Tool Registry**: Maintains the collection of tools our assistant can use
- **Function Execution**: Handles the execution of tool functions and formats their responses

For example, here's how we register our technical support assistant:
```python
assistant = {
    "id": "tech_support",
    "system_message": "You are a technical support agent...",
    "tools": [{
        "name": "check_service_status",
        "description": "Check if a service is operational",
        "parameters": {...},
        "returns": lambda params: {"status": "operational"}
    }]
}
service.register_agent(assistant)
```

### `realtime2.py`
Contains a **collection of helper classes and functions** for:
- Managing WebSocket connections to Azure OpenAI's realtime endpoint
- Handling event-based workflows (like `conversation.item.created`, `response.created`)
- Audio processing (PCM16, float32 conversion)
- Azure authentication and session management

## Key Concepts

1. **Realtime Client (`RealtimeClient`):**  
   A specialized client that maintains a WebSocket connection, enabling:
   - Bi-directional streaming of **audio** data (16-bit PCM format)
   - **Event-driven** conversation updates
   - Azure OpenAI authentication and session management

2. **Chainlit Integration:**  
   By using Chainlit's hooks (e.g., `@cl.on_chat_start`), we can:
   - **Initialize** the realtime client as soon as a chat session starts
   - **Pass** user's text or audio data to Azure OpenAI
   - **Handle** responses (text and audio) in real time

3. **Function Calling / Tools:**  
   Assistants can call **tools** to perform tasks. For instance:
   ```python
   # Example tool definition
   {
       "name": "check_service_status",
       "description": "Check if a service is operational",
       "parameters": {
           "type": "object",
           "properties": {
               "service": {
                   "type": "string",
                   "description": "Service to check (internet, mobile)"
               }
           }
       }
   }
   ```

## Workshop Flow

1. **User Connection:**  
   When a participant opens the workshop UI, `uv run chainlit run chat.py` starts a local server. Users can type messages or speak into the microphone.

2. **Message Handling:**  
   - **Text Input**: Processed through the `on_message` callback
   - **Audio Input**: Streamed as 16-bit PCM chunks, transcribed by Azure OpenAI

3. **Assistant Response:**  
   - The assistant provides responses in text or audio format
   - Function calls are automatically handled when needed
   - All responses are optimized for voice interaction

4. **Updates & Logging:**  
   - Comprehensive event logging helps track conversation flow
   - Debug messages available for troubleshooting

## Next Steps

After exploring the code and seeing how everything works together, you'll have a foundation for:
- **Adding new tools** for more complex tasks
- **Switching** between different assistants (e.g., billing, sales)
- **Scaling** the realtime approach for production
- Experimenting with **audio streaming** and **voice generation**

---

**Remember**: Most of the heavy lifting for streaming and event handling is encapsulated in `realtime2.py`, allowing you to focus on building your assistant's capabilities rather than dealing with low-level audio and WebSocket management.

Enjoy the workshop!
