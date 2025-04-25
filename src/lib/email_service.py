from src.utils.utils import is_debug_mode
import resend
from src.config.constants import RESEND_API_KEY


class EmailService:
    def send_email(self, message: str):
        if is_debug_mode():
            return
        resend.api_key = RESEND_API_KEY
        params: resend.Emails.SendParams = {
            "from": "Acme <onboarding@resend.dev>",
            "to": ["jaime5alvarez5h@gmail.com"],
            "subject": "tu hogar whatsapp reminder",
            "html": f"<p>{message}</p>",
        }
        resend.Emails.send(params)
