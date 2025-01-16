"""Main application file for the simple function calling demo."""

import chainlit as cl
from uuid import uuid4
from chainlit.logger import logger

from realtime2 import RealtimeClient
from dotenv import load_dotenv
load_dotenv(override=True)

# Define our main assistant
main_assistant = {
    "id": "Assistant_Main",
    "name": "Technical Support",
    "description": "A simple technical support assistant that can help with basic service issues.",
    "system_message": """
    You are a technical support agent that helps customers with basic service issues.
    Keep sentences short and simple, suitable for a voice conversation.
    
    Your tasks are:
    - Check if there are any known issues with the service
    - Check customer's usage data when needed
    - Provide simple troubleshooting steps
    
    Common issues and solutions:

    - Internet Service:
        - No connection:
            1. Check cables and power
            2. Restart the router
            3. Check service status
        - Slow connection:
            1. Check current usage
            2. Verify service status
            3. Try basic troubleshooting
    
    Always be polite and professional.
    Keep your responses brief and clear.
    """,
    "tools": [
        {
            "name": "check_usage",
            "description": "Check customer's service usage data",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string", "description": "Customer's ID"},
                },
                "required": ["customer_id"]
            },
            "returns": lambda input: {
                "current_usage": "80GB",
                "limit": "100GB",
                "status": "ACTIVE"
            }
        },
        {
            "name": "check_service_status",
            "description": "Check if there are any known service issues",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {"type": "string", "description": "Service to check (internet, mobile)"},
                },
                "required": ["service"]
            },
            "returns": lambda input: {
                "status": "OK" if input["service"] == "mobile" else "DEGRADED",
                "details": "No issues reported" if input["service"] == "mobile" else "Maintenance in progress"
            }
        }
    ]
}

async def setup_openai_realtime():
    """Initialize and configure the OpenAI Realtime Client with event handlers."""

    openai_realtime = RealtimeClient(system_prompt="")
    cl.user_session.set("track_id", str(uuid4()))

    async def handle_conversation_updated(event):
        """Handle real-time updates to the conversation."""
        item = event.get("item")
        delta = event.get("delta")
        
        if event:
            if "input_audio_transcription" in item["type"]:
                msg = cl.Message(content=delta["transcript"], author="user")
                msg.type = "user_message"
                await msg.send()
        if delta:
            if 'audio' in delta:
                await cl.context.emitter.send_audio_chunk(
                    cl.OutputAudioChunk(
                        mimeType="pcm16", 
                        data=delta['audio'], 
                        track=cl.user_session.get("track_id")
                    )
                )

    async def handle_item_completed(item):
        """Process completed conversation items."""
        if item["item"]["type"] == "message":
            content = item["item"]["content"][0]
            if content["type"] == "audio":
                await cl.Message(content=content["transcript"]).send()

    async def handle_conversation_interrupt(event):
        """Handle conversation interruptions."""
        cl.user_session.set("track_id", str(uuid4()))
        await cl.context.emitter.send_audio_interrupt()

    async def handle_error(event):
        """Log errors during conversation."""
        logger.error(event)

    # Register event handlers
    openai_realtime.on('conversation.updated', handle_conversation_updated)
    openai_realtime.on('conversation.item.completed', handle_item_completed)
    openai_realtime.on('conversation.interrupted', handle_conversation_interrupt)
    openai_realtime.on('error', handle_error)

    # Register our main assistant
    openai_realtime.assistant.register_agent(main_assistant)

    cl.user_session.set("openai_realtime", openai_realtime)
    return openai_realtime


@cl.on_chat_start
async def start():
    """Initialize the chat session."""
    await setup_openai_realtime()


@cl.on_message
async def on_message(message: cl.Message):
    """Process incoming chat messages."""
    openai_realtime: RealtimeClient = cl.user_session.get("openai_realtime")
    if openai_realtime and openai_realtime.is_connected():
        await openai_realtime.send_user_message_content([{"type": 'input_text', "text": message.content}])
    else:
        await cl.Message(content="Please activate voice mode before sending messages!").send()


@cl.on_audio_start
async def on_audio_start():
    """Initialize audio streaming session."""
    try:
        openai_realtime: RealtimeClient = cl.user_session.get("openai_realtime")
        await openai_realtime.connect()
        logger.info("Connected to OpenAI realtime")
        return True
    except Exception as e:
        await cl.ErrorMessage(content=f"Failed to connect to OpenAI realtime: {e}").send()
        return False


@cl.on_audio_chunk
async def on_audio_chunk(chunk: cl.InputAudioChunk):
    """Process incoming audio chunks."""
    openai_realtime: RealtimeClient = cl.user_session.get("openai_realtime")
    if openai_realtime:
        if openai_realtime.is_connected():
            await openai_realtime.append_input_audio(chunk.data)
        else:
            logger.info("RealtimeClient is not connected")


@cl.on_audio_end
@cl.on_chat_end
@cl.on_stop
async def on_end():
    """Clean up resources when the application stops."""
    openai_realtime: RealtimeClient = cl.user_session.get("openai_realtime")
    if openai_realtime and openai_realtime.is_connected():
        await openai_realtime.disconnect()
