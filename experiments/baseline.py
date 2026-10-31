from pathlib import Path

import pytesseract
from PIL import Image

from ocr_doctor.evaluation.metrics import cer, wer

reference = Path("ground_truth/story.txt").read_text(encoding="utf-8")
image = Image.open("data/test.png")
hypothesis = pytesseract.image_to_string(image, lang="eng")

print("OCR Doctor - Initial Baseline")
print("-----------------------------")
print(f"CER: {cer(reference, hypothesis):.2%}")
print(f"WER: {wer(reference, hypothesis):.2%}")
