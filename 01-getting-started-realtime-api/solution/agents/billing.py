"""Billing Assistant Module

This module defines the billing assistant and its supporting functions for managing
billing inquiries and payment-related operations.
"""

def fetch_billing_details(input):
    """Retrieve billing details for a customer.
    
    Args:
        input (dict): Contains customerCode for identifying the customer
        
    Returns:
        dict: Customer's billing information including balance and due date
    """
    # In a real implementation, this would fetch data from a billing system
    return {
        "balance": 45.75,
        "due_date": "2025-02-01",
        "latest_charges": "Monthly service fee of €30, plus a €15 phone accessory charge, plus taxes and fees."
    }

def fetch_payment_history(input):
    """Retrieve payment history for a customer.
    
    Args:
        input (dict): Contains customerCode for identifying the customer
        
    Returns:
        list: List of recent payment transactions
    """
    # In a real implementation, this would fetch data from a payment system
    return [
        {"date": "2024-12-20", "amount": 50.00, "method": "Credit Card"},
        {"date": "2024-11-20", "amount": 30.00, "method": "Credit Card"},
    ]

def update_payment_method(input):
    """Update a customer's payment method.
    
    Args:
        input (dict): Contains customerCode and new payment method details
        
    Returns:
        str: Confirmation message of the update
    """
    # In a real implementation, this would update the payment system
    return f"Payment method updated to {input['paymentMethod']} for customer {input['customerCode']}"

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
    "system_message": """You are a billing representative who assists customers with their billing or payment inquiries.
        Keep sentences short and simple, suitable for a voice conversation, so it's *super* important that answers are as short as possible. Use professional language.
        
        Your tasks are:
        - Verify the customer's identity if needed (e.g., full name, last 4 of credit card on file, or other unique ID if required).
        - Provide billing details, such as current balance, recent charges, and any past-due amounts.
        - Provide payment history if requested.
        - Support the customer in setting up or updating their payment method.
        - If the customer's billing issue relates to an unactivated or newly purchased service, route them to the Activation Assistant.
        - If the customer's billing inquiry involves a possible technical issue (e.g., charged for a service that is not working), route them to the Technical Assistant.
        
        IMPORTANT NOTES:
        - Act politely and professionally.
        - Use short, concise statements suitable for a quick voice call.
        - If any internal information or deeper investigation is needed, do not hesitate to inform the customer and consult the relevant tools or route the correct assistant if beyond billing scope.""",
    "tools": [
        {
            "name": "fetch_billing_details",
            "description": "Retrieve the customer's current billing details (balance, due date, latest charges).",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Unique identifier for the customer to fetch billing info."
                    }
                }
            },
            "returns": fetch_billing_details
        },
        {
            "name": "fetch_payment_history",
            "description": "Retrieve the customer's recent payment history.",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Unique identifier for the customer to fetch their payment history."
                    }
                }
            },
            "returns": fetch_payment_history
        },
        {
            "name": "update_payment_method",
            "description": "Updates the customer's stored payment method (e.g., new credit card).",
            "parameters": {
                "type": "object",
                "properties": {
                    "customerCode": {
                        "type": "string",
                        "description": "Unique identifier for the customer to update payment method."
                    },
                    "paymentMethod": {
                        "type": "string",
                        "description": "New payment method details (e.g., 'Visa ending in 1234')."
                    }
                }
            },
            "returns": update_payment_method
        }
    ]
}
