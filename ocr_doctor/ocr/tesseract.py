import time

import pytesseract
from PIL import Image

from ocr_doctor.domain.models import OcrResult
from ocr_doctor.ocr.base import OcrEngine


class TesseractEngine(OcrEngine):
    LANGUAGES = {
        "en": "eng",
        "fr": "fra",
        "ar": "ara",
    }

    def __init__(self, psm: int = 3, timeout: int = 30):
        self.psm = psm
        self.timeout = timeout

    def read(self, image: Image.Image, lang: str) -> OcrResult:
        language = self.LANGUAGES.get(lang, lang)
        config = f"--oem 1 --psm {self.psm}"
        start_time = time.perf_counter()

        data = pytesseract.image_to_data(
            image,
            lang=language,
            config=config,
            output_type=pytesseract.Output.DICT,
            timeout=self.timeout,
        )

        words = []
        confidences = []

        for text, conf in zip(data["text"], data["conf"]):
            if text.strip() and float(conf) >= 0:
                words.append(text)
                confidences.append(float(conf))

        elapsed = time.perf_counter() - start_time

        return OcrResult(
            text=" ".join(words),
            word_confidences=tuple(confidences),
            elapsed_s=elapsed,
        )
