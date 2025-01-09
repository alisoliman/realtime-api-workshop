#!/usr/bin/env python
import asyncio
import websockets
import json
import sys
import datetime
import argparse
from typing import Optional

class WebSocketClient:
    def __init__(self, uri: str = "ws://localhost:8765"):
        self.uri = uri
        self.websocket: Optional[websockets.WebSocketClientProtocol] = None

    async def receive_messages(self):
        """Handle incoming messages from the server"""
        try:
            while True:
                message = await self.websocket.recv()
                data = json.loads(message)
                
                # Pretty print different message types
                if data["type"] == "welcome":
                    print(f"\n🎉 {data['message']}")
                elif data["type"] == "echo":
                    print(f"\n📩 Echo received: {data['message']}")
                elif data["type"] == "game_update":
                    # Print ball position updates (optional, commented out to reduce noise)
                    # print(f"\r🎾 Ball position: x={data['position']['x']:.1f}, y={data['position']['y']:.1f}", end="")
                    pass
                elif data["type"] == "error":
                    print(f"\n❌ Error: {data['message']}")
                
        except websockets.exceptions.ConnectionClosed:
            print("\n❌ Connection to server closed")
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")

    async def send_message(self, message: str):
        """Send a message to the server"""
        try:
            data = {
                "message": message,
                "timestamp": datetime.datetime.now().isoformat()
            }
            await self.websocket.send(json.dumps(data))
            print(f"\n📤 Sent: {message}")
        except Exception as e:
            print(f"\n❌ Error sending message: {str(e)}")

    async def interactive_session(self):
        """Start an interactive WebSocket session"""
        try:
            async with websockets.connect(self.uri) as websocket:
                self.websocket = websocket
                print(f"🔌 Connected to {self.uri}")
                print("📝 Type your messages (press Ctrl+C to exit)")
                
                # Start receiving messages in the background
                receive_task = asyncio.create_task(self.receive_messages())
                
                while True:
                    try:
                        message = await asyncio.get_event_loop().run_in_executor(
                            None, input, "\n✍️  Enter message: "
                        )
                        if message.strip():
                            await self.send_message(message)
                    except KeyboardInterrupt:
                        print("\n👋 Goodbye!")
                        break
                    
                receive_task.cancel()
                try:
                    await receive_task
                except asyncio.CancelledError:
                    pass
                
        except Exception as e:
            print(f"❌ Connection error: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description="WebSocket Client Example")
    parser.add_argument(
        "--uri", 
        default="ws://localhost:8765",
        help="WebSocket server URI (default: ws://localhost:8765)"
    )
    args = parser.parse_args()

    client = WebSocketClient(args.uri)
    try:
        asyncio.run(client.interactive_session())
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    main()
