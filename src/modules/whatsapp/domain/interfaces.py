from abc import ABC, abstractmethod


class IWhatsappUseCase(ABC):
    @abstractmethod
    def send_template_message(
        self, from_number: str, template_sid: str, content_variables: dict, to: str
    ):
        pass


class IWhatsappService(ABC):
    @abstractmethod
    def send_template_message(
        self, from_number: str, template_sid: str, content_variables: dict, to: str
    ):
        pass
