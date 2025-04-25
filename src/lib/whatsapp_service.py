class WhatsappService:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def send_message(self, message: str):
        print(f"Sending message to {self.phone_number}: {message}")
