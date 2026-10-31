from abc import ABC, abstractmethod

from PIL import Image

from ocr_doctor.domain.models import OcrResult


class OcrEngine(ABC):
    @abstractmethod
    def read(self, image: Image.Image, lang: str) -> OcrResult:
        pass
