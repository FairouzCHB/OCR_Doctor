from PIL import Image

from ocr_doctor.domain.models import OcrResult
from ocr_doctor.ocr.base import OcrEngine
from ocr_doctor.ocr.tesseract import TesseractEngine


class FakeEngine(OcrEngine):
    def read(self, image: Image.Image, lang: str) -> OcrResult:
        return OcrResult(
            text="Hello world",
            word_confidences=(95.0, 90.0),
            elapsed_s=0.1,
        )


def test_fake_engine_implements_interface():
    engine = FakeEngine()
    image = Image.new("RGB", (100, 100))
    result = engine.read(image, lang="en")
    assert result.text == "Hello world"
    assert result.word_confidences == (95.0, 90.0)
    assert result.elapsed_s == 0.1


def test_tesseract_engine_returns_ocr_result():
    engine = TesseractEngine()
    image = Image.new("RGB", (100, 100), color="white")
    result = engine.read(image, lang="en")
    assert isinstance(result, OcrResult)
    assert isinstance(result.text, str)
    assert isinstance(result.word_confidences, tuple)
    assert result.elapsed_s >= 0
