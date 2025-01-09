#!/usr/bin/env python
import asyncio
import websockets
import json
import random
from aiohttp import web
import aiohttp_cors

# Store connected clients
clients = set()
game_state = {"ball_position": {"x": 50, "y": 50}, "direction": {"x": 1, "y": 1}}

async def update_game():
    """Update game state and broadcast to all clients"""
    while True:
        # Update ball position
        game_state["ball_position"]["x"] += game_state["direction"]["x"] * 2
        game_state["ball_position"]["y"] += game_state["direction"]["y"] * 2

        # Bounce off walls
        if game_state["ball_position"]["x"] >= 100 or game_state["ball_position"]["x"] <= 0:
            game_state["direction"]["x"] *= -1
        if game_state["ball_position"]["y"] >= 100 or game_state["ball_position"]["y"] <= 0:
            game_state["direction"]["y"] *= -1

        if clients:  # Only broadcast if there are connected clients
            message = json.dumps({
                "type": "game_update",
                "position": game_state["ball_position"]
            })
            websockets.broadcast(clients, message)
        
        await asyncio.sleep(0.05)  # Update every 50ms

async def websocket_handler(websocket):
    """Handle individual WebSocket connections"""
    try:
        # Register client
        clients.add(websocket)
        print(f"Client connected. Total clients: {len(clients)}")
        
        # Send welcome message
        await websocket.send(json.dumps({
            "type": "welcome",
            "message": "Welcome to the WebSocket workshop!"
        }))

        async for message in websocket:
            try:
                data = json.loads(message)
                
                # Echo the message back with a type
                response = {
                    "type": "echo",
                    "message": data.get("message", ""),
                    "timestamp": data.get("timestamp", "")
                }
                
                # Broadcast to all clients
                websockets.broadcast(clients, json.dumps(response))
                
            except json.JSONDecodeError:
                await websocket.send(json.dumps({
                    "type": "error",
                    "message": "Invalid JSON format"
                }))

    except websockets.exceptions.ConnectionClosed:
        print("Client connection closed unexpectedly")
    
    finally:
        # Unregister client
        if websocket in clients:
            clients.remove(websocket)
            print(f"Client disconnected. Total clients: {len(clients)}")

# REST API Routes
async def get_ball_position(request):
    """REST endpoint to get current ball position"""
    return web.json_response({
        "position": game_state["ball_position"],
        "timestamp": asyncio.get_event_loop().time()
    })

async def echo_message(request):
    """REST endpoint to echo messages"""
    try:
        data = await request.json()
        return web.json_response({
            "type": "echo",
            "message": data.get("message", ""),
            "timestamp": data.get("timestamp", "")
        })
    except json.JSONDecodeError:
        return web.json_response({
            "error": "Invalid JSON format"
        }, status=400)

def init_rest_app():
    """Initialize REST API application"""
    app = web.Application()
    
    # Setup CORS to allow all origins
    cors = aiohttp_cors.setup(app, defaults={
        "*": aiohttp_cors.ResourceOptions(
            allow_credentials=True,
            expose_headers="*",
            allow_headers="*",
            allow_methods=["GET", "POST", "OPTIONS"]
        )
    })
    
    # Add routes with CORS
    cors.add(app.router.add_get("/api/ball", get_ball_position))
    cors.add(app.router.add_post("/api/echo", echo_message))
    
    return app

async def start_rest_server():
    """Start the REST server"""
    app = init_rest_app()
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8766)
    await site.start()
    print("REST server started on http://localhost:8766")

async def start_websocket_server():
    """Start the WebSocket server"""
    async with websockets.serve(websocket_handler, "localhost", 8765):
        print("WebSocket server started on ws://localhost:8765")
        await asyncio.Future()  # Run forever

async def main():
    """Start both WebSocket and REST servers"""
    # Start the game update loop
    asyncio.create_task(update_game())
    
    # Start both servers
    await asyncio.gather(
        start_rest_server(),
        start_websocket_server()
    )

if __name__ == "__main__":
    asyncio.run(main())
