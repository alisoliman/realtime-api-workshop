# WebSocket Basics Workshop

Learn the fundamentals of real-time communication with WebSockets through hands-on examples.

## What are WebSockets?

WebSockets are a protocol that enables two-way communication between a client and server over a single, long-lived connection. Unlike HTTP, which is request-response based, WebSockets allow for:
- Real-time data transfer
- Bi-directional communication
- Lower latency

## Core Concepts

- **Real-time Communication**: Two-way data transfer over a single, persistent connection
- **Bi-directional Flow**: Both server and client can initiate communication
- **Event-Driven Architecture**: Handle messages and events asynchronously

## Implementation Details

### Server (`server.py`)
- WebSocket server setup and configuration
- Client connection management
- Event handling and message broadcasting

### Client Implementation
- Browser-based client (`index.html`, `static/main.js`)
- Python client example (`client.py`)
- Connection lifecycle management

## Workshop Contents

This workshop includes:
1. A simple WebSocket echo server (`server.py`)
2. An interactive web client (`index.html` and `static/main.js`)
3. A Python WebSocket client (`client.py`)

## Getting Started

1. Install dependencies:
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

## Key Features

- Connection management
- Message broadcasting
- Error handling
- Client authentication
- Event-driven message processing

## Key Concepts Covered

- WebSocket Connection Lifecycle
- Message Handling
- Error Handling
- Asynchronous Programming with WebSockets
- Real-time Updates

## Next Steps

After completing this module, you'll be ready to work with the Azure OpenAI Realtime API, which uses similar WebSocket concepts for real-time voice-enabled interactions.

Move on to [Function Calling](../01-getting-started-function-calling/workshop.md) to learn about integrating OpenAI's Realtime API.
