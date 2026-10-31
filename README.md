# OCR Doctor

**Diagnoses blurry, tilted or poorly lit document photos, fixes only what is wrong, and measures how much the text recognition improves.**

Works on Arabic, French and English. Built by one person for the Thirduni team project hackathon (October 2026).

| Status | Working analysis, OCR and evaluation core. Adaptive selection and web interface: see [Status](#status) |

---

## The problem

OCR engines such as Tesseract read clean scans well, but phone photos of forms, receipts and certificates are often tilted, blurry, shadowed or low in contrast, and the text comes out wrong. The usual fix is to apply the same preprocessing steps to every image. That can backfire: thresholding can erase thin strokes, and denoising can remove French accents or the dots on Arabic letters.

OCR Doctor works like a doctor instead of applying the same medicine to everyone: it examines the image first, treats only what is wrong, and then proves with numbers whether the treatment helped.

## How it works

![OCR Doctor pipeline](docs/pipeline.png)

1. **Validate** the uploaded image.
2. **Analyze** its quality: blur (variance of the Laplacian), skew (line-angle estimation), contrast (grayscale standard deviation) and lighting (large-scale illumination estimate). The result is a quality profile.
3. **Select** preprocessing steps from the profile, with a rule-based selector and a learned one (Decision Tree or Random Forest) that share one interface.
4. **Preprocess**, then **recognize** the text with Tesseract.
5. **Evaluate** against ground truth with Character Error Rate (CER) and Word Error Rate (WER), and record processing time.

The research question: *does quality-aware preprocessing beat a fixed preprocessing pipeline, and does it hold across languages and degradation types?* A negative result is reported as a result.

## Status

| Component | State |
|---|---|
| Metrics (CER, WER) with unit tests | Done |
| Tesseract adapter (Arabic, French, English, word confidences, timing) | Done |
| Quality analyzer (blur, skew, contrast, lighting) | Done, checked on controlled degradations |
| Synthetic multilingual dataset | Done (see [Dataset](#dataset)) |
| Preprocessing: deskew, CLAHE | Done, early experiments |
| Other preprocessing steps (thresholding, denoising, lighting correction) | `TODO: update` |
| Rule-based selector | `TODO: update` |
| Learned selector (Decision Tree, Random Forest) | `TODO: update` |
| Streamlit web interface | `TODO: update` |
| Evaluation on real phone photos | `TODO: update` |

## Results

Reported on the held-out **test split**, which was not used to tune thresholds or train the selector.

| Method | CER | WER | Time per image |
|---|---|---|---|
| A. Raw OCR | `TBD` | `TBD` | `TBD` |
| B. Fixed preprocessing | `TBD` | `TBD` | `TBD` |
| C. Rule-based adaptive | `TBD` | `TBD` | `TBD` |
| D. Learned adaptive | `TBD` | `TBD` | `TBD` |
| E. Oracle (best strategy per image, upper bound only) | `TBD` | `TBD` | n/a |

Preliminary sanity checks so far (single controlled examples, not a benchmark):

- Variance of the Laplacian falls as blur increases.
- A synthetic 5° rotation is measured at about -5°, and after deskewing the estimate drops to about 0°.
- Grayscale standard deviation falls as contrast is reduced.
- One clean English sample: CER 0.56%, WER 3.16%. Tesseract is already near-perfect on clean images, so gains can only appear on degraded ones.

## Quick start

Requirements: Git and Docker.

```bash
git clone https://github.com/FairouzCHB/OCR_Doctor.git
cd OCR_Doctor
docker build -t ocr-doctor .
```

The image installs Python dependencies, Tesseract with Arabic, English and French data, and Noto fonts, and runs as a non-root user.

```bash
docker run --rm ocr-doctor tesseract --list-langs     # expect: ara, eng, fra, osd
docker run --rm ocr-doctor python -m pytest           # automated tests
docker run --rm ocr-doctor ruff check .               # code quality
docker run --rm ocr-doctor python experiments/test_deskew.py   # example experiment
```

`TODO: add the commands that generate the dataset and run the main experiment once they exist.`

## Dataset

- 30 synthetic source documents: 10 each in Arabic, French and English, including paragraphs, receipt-style text and short lists.
- 5 conditions per document: clean, mild blur, moderate blur, strong blur, rotated. That gives 150 images (90 train, 30 validation, 30 test).
- The split is made **by source document**, so variants of the same text never appear in both training and test data.
- Ground truth is the exact original Unicode text, with Arabic text rendered using shaping.

Synthetic data gives exact ground truth and known degradation levels, but it does not capture everything about real photos. See [Limitations](#limitations).

## Project structure

```
ocr_doctor/
  domain/          shared data models (quality profile, OCR result)
  analysis/        image-quality indicators
  preprocessing/   image enhancement steps
  selection/       rule-based and learned selectors
  ocr/             OCR engine interface and Tesseract adapter
  evaluation/      CER, WER, experiment runner
  security/        upload validation (planned)
  ai/, feedback/   optional extensions (planned)
  pipeline.py      orchestration
app/               Streamlit interface (planned)
corpus/            source texts and fixed split manifest
experiments/       experiment scripts
tests/             pytest suite
```

Design: Strategy pattern for interchangeable steps and selectors, Adapter for the OCR engine, a registry for preprocessing steps, dependency injection for testability, and immutable data models.

## Tech stack and AI tools

- **Languages and libraries:** Python 3.12, OpenCV, Pillow, NumPy, pytest, Ruff.
- **OCR:** Tesseract (Arabic, English, French).
- **Environment:** Docker, Git, GitHub.
- **Planned:** scikit-learn, Streamlit, Pydantic.
- **AI tools used during development:** ChatGPT and Claude, used for planning, explanations, code assistance and drafting documentation. The author ran and tested the code.

## Limitations

- Most data is synthetic. Real photos have shadows, perspective, paper texture and compression that the generator does not reproduce.
- Quality scores are heuristics, not perfect measures of how hard an image is to read.
- Arabic OCR is generally weaker than French or English. Results are reported per language and are not generalized across them.
- Some preprocessing steps help one image and harm another. That is the reason for selecting steps per image.
- An adaptive pipeline adds analysis time, so accuracy gains are reported next to latency.

## What happens next

In the next three months: add real phone photos for all three languages, perspective correction and page detection, and a retake-advice feature ("tilted 6°, uneven light: photograph near a window"). Then ship a hosted interface with opt-in feedback so consented usage data can retrain the selector offline. Optional later work is an API that other document tools can call, and LLM-based table extraction and summaries with validated output and explicit consent.

## Author

**Fairouz Cheikh Bassa**, sole developer: design, implementation, experiments and documentation.

## References

- Smith, R. (2007). *An Overview of the Tesseract OCR Engine.* ICDAR 2007. https://doi.org/10.1109/ICDAR.2007.4376991
- Sauvola, J., & Pietikäinen, M. (2000). *Adaptive document image binarization.* Pattern Recognition, 33(2), 225-236. https://doi.org/10.1016/S0031-3203(99)00055-2

Extended project document: `docs/PROJECT.md`.
