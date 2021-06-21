class PayloadHandler:

    def __init__(self, webhook, payload):
        """
        webhook: Webhook instance
        payload: JSON representation of the payload
        """
        self.webhook = webhook
        self.payload = payload
        self.repo = self.get_repo()

    def handle(self):
        pass

    def get_repo(self):
        return self.webhook.repo

    def ping(self):
        return 'pong'
