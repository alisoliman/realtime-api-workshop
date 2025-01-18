# Realtime API Workshop

Build voice-enabled AI assistants using Azure OpenAI's Realtime API. Create a multi-agent system for customer service applications.

## Workshop Modules

| Module | Focus | Documentation |
|--------|-------|---------------|
| 1. WebSocket Basics | Real-time Communication Fundamentals | [Guide](./00-websocket-basics/README.md) |
| 2. Function Calling | OpenAI Realtime API Integration | [Guide](./01-getting-started-function-calling/workshop.md) |
| 3. Multi-Agent System | Customer Service Implementation | [Guide](./02-building-multi-agent-system/README.md) |
| 4. Voice RAG | Voice-Optimized Document Retrieval | [Guide](./03-voice-rag/README.md) |

## Setup

1. **Prerequisites**
   - Python 3.8+
   - Azure OpenAI API key

2. **Environment**
   ```bash
   cp .env.example .env
   # Add your Azure OpenAI credentials
   ```

3. **Dependencies**
   Each module contains its own setup instructions and requirements. You can choose to:
   - Use `uv` for faster package management
   - Set up a traditional virtual environment with `requirements.txt`

## Development Tools

- **uv**: Fast Python package installer (recommended)
- **Chainlit**: AI assistant development framework

## Contributing

Contributions welcome via pull requests.