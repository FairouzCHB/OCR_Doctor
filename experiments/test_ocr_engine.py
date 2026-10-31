from PIL import Image

from ocr_doctor.ocr.tesseract import TesseractEngine

images = [
    ("English", "data/test.png", "en"),
    ("French", "data/frensh_test.png", "fr"),
    ("Arabic", "data/arabic_test.png", "ar"),
]

for language_name, image_path, lang in images:
    print(f"\n{'=' * 15} {language_name} {'=' * 15}")

    image = Image.open(image_path)
    engine = TesseractEngine(psm=6)

    result = engine.read(image, lang=lang)

    average_confidence = (
        sum(result.word_confidences) / len(result.word_confidences)
        if result.word_confidences
        else 0
    )

    print("Extracted text:")
    print(result.text)
    print(f"Average confidence: {average_confidence:.2f}")
    print(f"Elapsed time: {result.elapsed_s:.3f}s")
