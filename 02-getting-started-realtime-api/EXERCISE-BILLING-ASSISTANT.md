# Exercise: Adding a Billing Assistant

In this exercise, you'll extend the Realtime API system by adding a specialized assistant that handles billing and payment inquiries. You will:
1. Create a new assistant configuration  
2. Add custom tools for the assistant  
3. Integrate the assistant with the existing system  

---

## Exercise Goals
- Learn how to create and configure a new assistant  
- Implement custom tools with mock data  
- Integrate the new billing functionality into your existing assistant network  

---

## Step-by-Step Guide

### 1. Create the Billing Assistant File
In the `agents` directory, create a new file `billing.py` with three key parts:

#### Tool Functions

```python
def fetch_billing_details(input):
    """Retrieve billing details for a customer.
    
    Args:
        input (dict): Contains 'customerCode' to identify the customer.
        
    Returns:
        dict: Customer's billing information including balance and due date.
    """
    return {
        "balance": 45.75,
        "due_date": "2025-02-01",
        
        "latest_charges": "Monthly service fee of €30, plus a €15 phone accessory charge, plus taxes and fees."
    }

def fetch_payment_history(input):
    """Retrieve payment history for a customer."""
    return [
        {"date": "2024-12-20", "amount": 50.00, "method": "Credit Card"},
        {"date": "2024-11-20", "amount": 30.00, "method": "Credit Card"},
    ]

def update_payment_method(input):
    """Update a customer's payment method."""
    return f"Payment method updated to {input['paymentMethod']} for customer {input['customerCode']}"

```







1. Tool Functions:
```python
def fetch_billing_details(input):
    """Retrieve billing details for a customer.
    
    Args:
        input (dict): Contains customerCode for identifying the customer
        
    Returns:
        dict: Customer's billing information including balance and due date
    """
    return {
        "balance": 45.75,
        "due_date": "2025-02-01",
        "latest_charges": "Monthly service fee of €30, plus a €15 phone accessory charge, plus taxes and fees."
    }

def fetch_payment_history(input):
    """Retrieve payment history for a customer."""
    return [
        {"date": "2024-12-20", "amount": 50.00, "method": "Credit Card"},
        {"date": "2024-11-20", "amount": 30.00, "method": "Credit Card"},
    ]

def update_payment_method(input):
    """Update a customer's payment method."""
    return f"Payment method updated to {input['paymentMethod']} for customer {input['customerCode']}"
```

2. Assistant Configuration:
```python
billing_assistant = {
    "id": "Assistant_BillingAssistant",
    "name": "Billing Assistant",
    "description": """Call this if:
        - The customer wants to discuss billing or payment inquiries.
        - The customer wants to check outstanding balances, view payment history, or set up a new payment method.

        DO NOT CALL IF:
        - The customer needs technical support (call Technical Support).
        - The customer wants to learn about product pricing or details (call Sales Assistant).
        - The customer wants to activate or replace a service (call Activation Assistant).
        - The customer needs a general greeting or final closure (call Greeter).""",
    "system_message": """You are a billing representative who assists customers with their billing or payment inquiries...""",
    "tools": [
        {
            "name": "fetch_billing_details",
            "description": "Retrieve the customer's current billing details.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Unique identifier for the customer."
                    }
                }
            },
            "returns": fetch_billing_details  # Important: Include the function reference
        },
        # ... other tools with their 'returns' functions ...
    ]
}
```

3. Important Implementation Notes:
   - Each tool MUST include a `returns` key with the corresponding function
   - Tool functions should handle invalid inputs gracefully
   - Keep responses concise for voice interactions

### 2. Update the Chat Application
Modify your `chat.py` file to import and register the new billing assistant:

```python
from agents.billing import billing_assistant  # Add this import

# In the setup_openai_realtime function:
openai_realtime.assistant.register_agent(billing_assistant)
# Make sure this is BEFORE registering the root agent
openai_realtime.assistant.register_root_agent(root_assistant)
```

### 3. Test the Integration
1. Start your chat application:
   ```bash
   uv run chainlit run chat.py
   ```

2. Try these test conversations:
   - "I'd like to check my current balance"
   - "Can you help me update my payment method?"
   - "Show me my recent payments"

3. Verify that:
   - The root assistant correctly routes to billing
   - The billing assistant asks for customer codes
   - Tool responses are properly formatted
   - Transitions between assistants are smooth

### Expected Behavior
- The root assistant should recognize billing-related queries and route them to the billing assistant
- The billing assistant should:
  - Ask for customer identification when needed
  - Handle billing inquiries using its tools
  - Route non-billing queries back to appropriate assistants
- All responses should be concise and voice-friendly

### Common Issues and Solutions
1. Tool Execution Errors:
   - Ensure each tool has a `returns` function specified
   - Verify tool function parameters match the schema
   - Handle missing or invalid inputs gracefully

2. Assistant Routing Issues:
   - Register billing assistant before the root agent
   - Verify assistant ID matches in all references
   - Check system message for clear routing rules

## Challenge Tasks
1. Add a new tool to the billing assistant that allows customers to set up automatic payments
2. Implement a tool that generates a PDF billing statement
3. Add support for multiple currencies in the billing details
4. Add input validation for customer codes
5. Implement a more sophisticated mock database for billing data

## Solution
The complete solution can be found in the `solution` directory, which includes:
- Fully implemented billing assistant with all tools
- Updated chat application with proper integration
- Example conversations demonstrating the billing assistant in action

## Tips
- Keep the assistant's responses concise and suitable for voice interactions
- Implement proper error handling in tool functions
- Test edge cases in customer interactions
- Consider security implications when handling billing data

## Next Steps
After completing this exercise, you'll have a better understanding of:
- Creating and integrating new assistants into the system
- Implementing robust tool functions with proper error handling
- Best practices for handling sensitive information
- Inter-assistant communication patterns
