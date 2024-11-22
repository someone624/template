import stripe

# Stripe API configuration
stripe.api_key = "your-secret-key"

def process_payment(amount, currency="usd", source=None, description=""):
    """
    Processes a payment using Stripe.
    """
    try:
        charge = stripe.Charge.create(
            amount=int(amount * 100),  # Stripe uses the smallest currency unit
            currency=currency,
            source=source,
            description=description,
        )
        return charge
    except stripe.error.StripeError as e:
        print(f"Error processing payment: {e}")
        return None

def refund_payment(charge_id):
    """
    Refunds a payment using Stripe.
    """
    try:
        refund = stripe.Refund.create(charge=charge_id)
        return refund
    except stripe.error.StripeError as e:
        print(f"Error refunding payment: {e}")
        return None