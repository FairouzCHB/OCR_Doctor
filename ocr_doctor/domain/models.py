from dataclasses import dataclass


@dataclass(frozen=True)
class OcrResult:
    text: str
    word_confidences: tuple[float, ...]
    elapsed_s: float
