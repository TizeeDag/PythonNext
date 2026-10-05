"""A reusable greeting card module."""
class GreetingCard:
    def __init__(self, recipient='Dana Ev', sender='Eyal Ch'):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        print(f'To: {self._recipient}, From: {self._sender}')
