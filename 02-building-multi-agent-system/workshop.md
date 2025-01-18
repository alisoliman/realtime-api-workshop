# Building a Multi-Agent System

Learn to create a complete customer service system using multiple specialized AI assistants that work together to handle different types of customer inquiries.

## Overview

This module implements a telecom customer service system with specialized agents for:
- Technical Support
- Sales
- Service Activation
- Billing ([Exercise](./EXERCISE-BILLING-ASSISTANT.md))

## System Architecture

### Components
- Root Agent: Routes inquiries to specialized agents
- Specialized Agents: Handle domain-specific queries
- Backend Services: Mock implementations of telecom services
- Voice Interface: Optimized for natural conversation

### Implementation Details
- Inter-agent communication protocols
- Context management and state handling
- Voice response optimization
- Error handling and fallback strategies

## Getting Started

1. **Configure API**
   ```bash
   cp ../.env.example .env
   # Add your Azure OpenAI credentials
   ```

2. **Run the Application**
   
   Choose one of these methods:

   **Using uv (Recommended)**
   ```bash
   uv run chainlit run chat.py
   ```

   **Using Traditional Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   chainlit run chat.py
   ```

## Exercises

1. [Building a Billing Assistant](./EXERCISE-BILLING-ASSISTANT.md)
   - Implement specialized billing functionality
   - Handle payment inquiries
   - Process billing disputes

## Key Concepts

- Multi-agent coordination
- Specialized knowledge domains
- Context preservation
- Voice interaction optimization
- Error handling and recovery

## Solution

A complete implementation is available in the [solution](./solution) directory.
