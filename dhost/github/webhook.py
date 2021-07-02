class PayloadHandler:
    """A class to handle Github webhooks.

    Github docs: https://docs.github.com/en/github-ae@latest/developers/\
        webhooks-and-events/webhooks/webhook-events-and-payloads#push

    Args:
        webhook (Webhook): Webhook instance.
        payload (JSON): JSON representation of the payload.
    """

    def __init__(self, webhook, payload):
        self.webhook = webhook
        self.payload = payload
        self.repo = self.get_repo()

    def handle(self):
        pass

    def get_repo(self):
        return self.webhook.repo

    def ping(self):
        return 'pong'
