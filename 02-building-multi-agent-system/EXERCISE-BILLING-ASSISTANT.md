# Exercise: Building a Billing Assistant for Voice Interactions

## Overview
In this exercise, you'll create a specialized billing assistant that handles customer billing and payment inquiries through voice interactions. This assistant will be part of your Realtime API system and demonstrate how to build voice-optimized AI assistants.

## Learning Objectives
- Design and implement a voice-optimized AI assistant for billing inquiries
- Create mock billing tools that simulate real backend services
- Practice proper assistant routing and inter-assistant communication
- Implement professional, concise responses suitable for voice interactions

## Prerequisites
- Completed the previous exercises
- Understanding of Python and the assistant framework
- Basic knowledge of billing and payment concepts

## Exercise Structure

### Part 1: Understanding the Components

#### The Billing Assistant's Role
The billing assistant is responsible for:
- Providing current billing information
- Showing payment history
- Updating payment methods
- Routing non-billing queries to appropriate assistants

#### Key Design Principles
1. **Voice-First**: All responses must be concise and clear for voice interactions
2. **Professional Tone**: Maintain a professional, helpful demeanor
3. **Proper Routing**: Know when to handle queries and when to route to other assistants
4. **Data Privacy**: Handle billing information with appropriate security considerations

### Part 2: Implementation Steps

#### Step 1: Create the Billing Tools
Create `billing.py` in your `agents` directory with these mock tools:

```python
def fetch_billing_details(input):
    """Get customer's current billing information.
    
    Args:
        input (dict): Must contain 'customerCode' to identify the customer
        
    Returns:
        dict: Current billing status including balance and due date
    """
    return {
        "balance": 45.75,
        "due_date": "2025-02-01",
        "latest_charges": "Monthly service fee of €30, plus a €15 phone accessory charge, plus taxes and fees."
    }

def fetch_payment_history(input):
    """Get customer's recent payments.
    
    Args:
        input (dict): Must contain 'customerCode' to identify the customer
        
    Returns:
        list: Recent payment transactions
    """
    return [
        {"date": "2024-12-20", "amount": 50.00, "method": "Credit Card"},
        {"date": "2024-11-20", "amount": 30.00, "method": "Credit Card"},
    ]

def update_payment_method(input):
    """Update customer's payment method.
    
    Args:
        input (dict): Must contain:
            - customerCode: Customer identifier
            - paymentMethod: New payment method details
            
    Returns:
        str: Confirmation message
    """
    return f"Payment method updated to {input['paymentMethod']} for customer {input['customerCode']}"
```

#### Step 2: Configure the Billing Assistant
Add this configuration to `billing.py`:

```python
billing_assistant = {
    "id": "Assistant_BillingAssistant",
    "name": "Billing Assistant",
    "description": """Call this if:
        - Customer has billing or payment inquiries
        - Customer needs to check balance or payment history
        - Customer wants to update payment method

        DO NOT CALL IF:
        - Customer needs technical support
        - Customer wants product information
        - Customer needs service activation
        - Customer needs general assistance""",
    "system_message": """You are a billing representative helping customers with billing inquiries.
        
        IMPORTANT GUIDELINES:
        1. Keep responses SHORT and CLEAR - perfect for voice interactions
        2. Always verify customer identity before sharing billing info
        3. Use professional language
        4. Route technical issues to Technical Assistant
        5. Route service activation issues to Activation Assistant
        
        YOUR TASKS:
        - Provide billing details (balance, due dates)
        - Show payment history
        - Help update payment methods
        - Route non-billing queries appropriately""",
    "tools": [
        {
            "name": "fetch_billing_details",
            "description": "Get customer's current billing status",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Customer's unique identifier"
                    }
                }
            },
            "returns": fetch_billing_details
        },
        {
            "name": "fetch_payment_history",
            "description": "Get customer's payment history",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Customer's unique identifier"
                    }
                }
            },
            "returns": fetch_payment_history
        },
        {
            "name": "update_payment_method",
            "description": "Update customer's payment method",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Customer's unique identifier"
                    },
                    "paymentMethod": {
                        "type": "string",
                        "description": "New payment method details"
                    }
                }
            },
            "returns": update_payment_method
        }
    ]
}
```

#### Step 3: Register the Assistant
Update your `chat.py`:

```python
from agents.billing import billing_assistant

def setup_openai_realtime():
    # ... existing setup code ...
    
    # Register billing assistant BEFORE root assistant
    openai_realtime.assistant.register_agent(billing_assistant)
    openai_realtime.assistant.register_root_agent(root_assistant)
```

### Part 3: Testing Your Implementation

#### Test Scenarios
Try these conversations to verify proper functionality:

1. Basic Balance Check
   ```
   User: "What's my current balance?"
   Assistant: *Should ask for customer identification*
   User: *Provides customer code*
   Assistant: *Should show balance and due date*
   ```

2. Payment History
   ```
   User: "Show me my recent payments"
   Assistant: *Should ask for customer identification*
   User: *Provides customer code*
   Assistant: *Should list recent payments*
   ```

3. Update Payment Method
   ```
   User: "I want to update my credit card"
   Assistant: *Should ask for customer identification*
   User: *Provides customer code*
   Assistant: *Should guide through payment method update*
   ```

4. Proper Routing
   ```
   User: "My internet is not working"
   Assistant: *Should route to Technical Assistant*
   ```

#### Verification Checklist
- [ ] Responses are concise and voice-friendly
- [ ] Customer identification is properly requested
- [ ] Tool responses are clearly communicated
- [ ] Non-billing queries are correctly routed
- [ ] Professional tone is maintained

### Common Pitfalls
1. **Long Responses**: Keep responses short and focused
2. **Missing Identity Verification**: Always verify customer before sharing data
3. **Improper Routing**: Know when to route to other assistants
4. **Tool Integration**: Ensure all tools have proper 'returns' functions
5. **Error Handling**: Gracefully handle invalid inputs

### Challenge Tasks
1. Add support for payment plans
2. Implement bill explanation feature
3. Add support for multiple currencies
4. Create a billing statement generator
5. Add a payment reminder system

## Next Steps
After completing this exercise, explore:
- Adding more sophisticated billing features
- Implementing real backend integrations
- Adding support for different payment providers
- Enhancing security measures
- Improving voice interaction patterns

## Resources
- [Voice Design Best Practices](https://example.com)
- [Billing System Integration Patterns](https://example.com)
- [Security in Financial Systems](https://example.com)
