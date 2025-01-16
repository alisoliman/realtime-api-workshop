# Realtime API Workshop

A hands-on workshop for building voice-enabled AI assistants using OpenAI's Realtime API. This workshop guides you through creating a multi-agent system for a telecom company's customer service, demonstrating real-world applications of AI in voice interactions.

## Project Overview

This workshop consists of four progressive modules, each building upon the previous one to create a comprehensive understanding of AI assistant development:

### 00-websocket-basics
An introduction to WebSocket communication, providing the foundation for real-time interactions. This module covers:
- Basic WebSocket server setup
- Client-server communication patterns
- Handling real-time events

### 01-getting-started-function-calling
Introduction to Azure OpenAI's Realtime API with function calling capabilities:
- Setting up basic AI assistants
- Implementing function calling
- Handling assistant responses
- Basic conversation management

### 02-building-multi-agent-system
The main workshop module implementing a complete telecom customer service system:
- Multiple specialized AI assistants (Technical, Sales, Activation)
- Inter-assistant communication and routing
- Voice-optimized responses
- Mock backend service integration

### 03-voice-rag
Advanced module focusing on voice-enabled Retrieval Augmented Generation:
- Voice-optimized RAG implementation
- Document retrieval and context management
- Natural conversation flow with document references

#### Workshop Exercises
1. [Building a Billing Assistant](./02-building-multi-agent-system/EXERCISE-BILLING-ASSISTANT.md) - Create a specialized assistant for handling billing inquiries

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Azure OpenAI API key
- Basic understanding of Python and WebSockets

### Installation & Running

#### Option 1: Using uv (Recommended)
The fastest way to run the project is using uv directly:
```bash
# Navigate to the desired module
cd 02-building-multi-agent-system

# Run the chat application
uv run chainlit run chat.py
```

#### Option 2: Traditional Setup
If you prefer using a traditional virtual environment:
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the chat application
chainlit run chat.py
```

### Environment Setup
```bash
cp .env.example .env
# Edit .env with your Azure OpenAI API key and endpoint
```

## Project Structure

```
realtime-api-workshop/
├── 00-websocket-basics/          # WebSocket fundamentals
│   ├── server.py                 # Basic WebSocket server
│   └── requirements.txt          # Module-specific dependencies
│
├── 01-getting-started-function-calling/  # Function calling basics
│   ├── assistant_service.py      # Basic assistant implementation
│   ├── chat.py                   # Chat interface
│   └── workshop.md               # Module guide and instructions
│
├── 02-building-multi-agent-system/      # Multi-agent implementation
│   ├── agents/                   # Specialized AI assistants
│   │   ├── activation.py         # Service activation assistant
│   │   ├── billing.py           # Billing assistant
│   │   ├── root.py              # Main routing assistant
│   │   ├── sales.py             # Sales assistant
│   │   └── technical.py         # Technical support assistant
│   ├── solution/                 # Complete implementation
│   ├── assistant_service.py      # Enhanced assistant service
│   ├── chat.py                   # Main chat application
│   └── EXERCISE-BILLING-ASSISTANT.md  # Billing assistant exercise
│
├── 03-voice-rag/                 # Voice-enabled RAG implementation
│   └── workshop.md               # Module guide and instructions
│
└── requirements.txt              # Global project dependencies
```

## Development Tools

- **uv**: Fast Python package installer and resolver
- **Chainlit**: Development tool for testing and debugging AI assistants

## Contributing

We welcome contributions! Please feel free to submit pull requests with improvements, bug fixes, or new exercises.

## TODO

- [ ] Add requirements.txt as an alternative for uv