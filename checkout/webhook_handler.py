from django.http import HttpResponse

class StripeWebhookHandler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event"""
        return HttpResponse(
            content = f'Unhandled webhook received: {event["type"]}',
            status = 200
        )

    def handle_payment_intent_succeeded(self, event):
        # print(event.data.object)
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200
        )

    def handle_payment_intent_failed(self, event):
        return HttpResponse(
            content = f'Webhook received: {event["type"]}',
            status = 200
        )