# WebSocket Basics Workshop

Welcome to the WebSocket basics workshop! In this module, you'll learn about WebSockets through hands-on examples.

## What are WebSockets?

WebSockets are a protocol that enables two-way communication between a client and server over a single, long-lived connection. Unlike HTTP, which is request-response based, WebSockets allow for:
- Real-time data transfer
- Bi-directional communication
- Lower latency than HTTP polling

## Workshop Contents

This workshop includes:
1. A simple WebSocket echo server (`server.py`)
2. An interactive web client (`index.html` and `static/main.js`)
3. A Python WebSocket client (`client.py`)

## Getting Started

1. Install the requirements:
```bash
pip install -r requirements.txt
```

2. Start the WebSocket server:
```bash
python server.py
```

3. Open the web client in your browser:
```bash
python -m http.server 8000
```
Then visit http://localhost:8000

## Interactive Examples

1. **Echo Test**: Send messages and see them echoed back
2. **Bouncing Ball Demo**: 
   - A simple animation showing a ball bouncing around the canvas
   - Demonstrates server-pushed updates in real-time
   - Shows how WebSockets enable:
     * Continuous data streaming from server to client
     * Smooth animations without client-side requests
     * Same state synchronized across all connected clients
3. **Chat Room**: Basic multi-client chat functionality

## Key Concepts Covered

- WebSocket Connection Lifecycle
- Message Handling
- Error Handling
- Asynchronous Programming with WebSockets
- Real-time Updates

## Next Steps

After completing this module, you'll be ready to work with the Azure OpenAI Realtime API, which uses similar WebSocket concepts for real-time AI interactions.
