from src.config.constants import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN
from src.modules.whatsapp.domain.interfaces import IWhatsappService
from src.modules.whatsapp.infraestructure.twilio import TwilioWhatsappService


class WhatsappUseCase(IWhatsappService):
    def __init__(self, whatsapp_service: IWhatsappService):
        self.whatsapp_service = whatsapp_service

    def send_template_message(
        self, from_number: str, template_sid: str, content_variables: dict, to: str
    ):
        return self.whatsapp_service.send_template_message(
            from_number, template_sid, content_variables, to
        )


class FactoryWhatsappUseCase:
    @staticmethod
    def create():
        whatsapp_service = TwilioWhatsappService(
            TWILIO_ACCOUNT_SID,
            TWILIO_AUTH_TOKEN,
        )
        return WhatsappUseCase(whatsapp_service)
