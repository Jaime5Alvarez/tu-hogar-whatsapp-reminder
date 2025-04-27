import json
from twilio.rest import Client

from src.modules.whatsapp.domain.interfaces import IWhatsappService


class TwilioWhatsappService(IWhatsappService):
    def __init__(self, account_sid: str, auth_token: str):
        self.client = Client(account_sid, auth_token)

    def send_template_message(
        self, from_number: str, template_sid: str, content_variables: dict, to: str
    ):
        self.client.messages.create(
            from_=from_number,
            content_sid=template_sid,
            content_variables=json.dumps(content_variables),
            to=to,
        )
