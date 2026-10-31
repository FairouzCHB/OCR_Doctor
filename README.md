# OCR Doctor

### Intelligent, Quality-Aware Multilingual OCR

**Analyzes blurry, tilted or poorly lit document photos, explores how to correct their defects selectively, and measures whether text recognition improves.**

Supports Arabic, French and English. Developed independently for the Thirduni project hackathon (October 2026).

> **Project status:** Image-quality analysis, OCR integration, synthetic dataset generation and evaluation foundations are implemented. Adaptive selection and the interactive web interface remain under development.

---

## The Problem

OCR engines such as Tesseract can recognize clean scans accurately, but photographs of forms, receipts and certificates often contain blur, rotation, shadows or low contrast. These defects can cause recognition errors.

A common approach is to apply the same preprocessing operations to every image. However, this can sometimes make recognition worse: aggressive thresholding may erase thin character strokes, while denoising may remove French accents or the dots and fine details of Arabic letters.

OCR Doctor investigates a more selective approach: analyze the image first, identify its potential defects, and determine which corrections are appropriate before running OCR.

The objective is not to apply more transformations, but to apply the right transformations and measure their actual impact.

## How It Works

The following diagram presents the proposed end-to-end OCR Doctor architecture.

![OCR Doctor Pipeline](docs/ocr_doctor_pipeline_flowchart.png)

1. **Validate (planned):** Check the uploaded image before processing.
2. **Analyze:** Measure blur (variance of the Laplacian), skew (line-angle estimation), contrast (grayscale standard deviation) and lighting (large-scale illumination estimation). These measurements form a quality profile.
3. **Select (planned):** Use the quality profile to determine appropriate preprocessing operations through rule-based or learned selection strategies.
4. **Preprocess (in progress):** Apply selected image-enhancement operations.
5. **Recognize:** Extract text using Tesseract OCR.
6. **Evaluate:** Compare extracted text against ground truth using Character Error Rate (CER) and Word Error Rate (WER), while recording processing time.

**The central research question:**

*Can quality-aware preprocessing outperform fixed preprocessing strategies, and does the improvement hold across different languages and degradation types?*

A negative result is also a valid research result.

## Project Status

| Component | Current state |
|---|---|
| CER and WER metrics with unit tests | Implemented |
| Tesseract adapter (Arabic, French, English, word confidences and timing) | Implemented |
| Quality analyzer (blur, skew, contrast and lighting) | Implemented |
| Synthetic multilingual dataset | Generated |
| Deskewing | Implemented |
| CLAHE contrast enhancement | Implemented |
| Adaptive thresholding, denoising and lighting correction | Planned |
| Image validation | Planned |
| Rule-based preprocessing selector | Planned |
| Learned selector (Decision Tree, Random Forest) | Planned |
| Complete experimental comparison | Planned |
| Streamlit web interface | Planned |
| Evaluation on real phone photographs | Planned |

The current prototype establishes the analysis, OCR, dataset and evaluation foundations. The complete adaptive selection pipeline is the next major development objective.

## Results

The following table defines the planned main experiment. Results will be populated after the preprocessing pipeline, selectors and experimental evaluation have been implemented and validated.

| Method | CER | WER | Time per image |
|---|---|---|---|
| A. Raw OCR | TBD | TBD | TBD |
| B. Fixed preprocessing | TBD | TBD | TBD |
| C. Rule-based adaptive | TBD | TBD | TBD |
| D. Learned adaptive | TBD | TBD | TBD |
| E. Oracle (experimental upper bound) | TBD | TBD | N/A |

The oracle represents the best candidate strategy according to ground-truth evaluation for an individual image. It is an experimental reference, not a deployable model.

### Preliminary Sanity Checks

The following observations come from individual controlled examples. They are not representative benchmark results.

- **Blur:** Variance of the Laplacian decreases as stronger blur is introduced.
- **Skew:** A synthetic 5° rotation was measured at approximately -5°. After deskewing, the estimated angle returned to approximately 0°.
- **Contrast:** Grayscale standard deviation decreases as image contrast is reduced.
- **OCR:** One clean English sample produced a CER of 0.56% and a WER of 3.16%.

These experiments verify initial component behavior. Broader evaluation across the multilingual dataset is still required.

## Quick Start

### Requirements

- Git
- Docker Desktop or Docker Engine

### Clone the Repository

```bash
git clone https://github.com/FairouzCHB/OCR_Doctor.git
cd OCR_Doctor
```

### Build the Docker Image

```bash
docker build -t ocr-doctor .
```

The Docker image installs Python dependencies, Tesseract with Arabic, English and French language data, and Noto fonts. It also creates a dedicated non-root application user.

### Verify Installed OCR Languages

```bash
docker run --rm ocr-doctor tesseract --list-langs
```

Expected language data includes:

```text
ara
eng
fra
osd
```

### Run Automated Tests

```bash
docker run --rm ocr-doctor python -m pytest
```

### Check Code Quality

```bash
docker run --rm ocr-doctor ruff check .
docker run --rm ocr-doctor ruff format --check .
```

### Run an Example Experiment

```bash
docker run --rm ocr-doctor python experiments/test_deskew.py
```

The available experiment scripts can be found in the `experiments/` directory.

### Start an Interactive Development Container

The Docker image is configured as a persistent development environment.

```bash
docker run -d --name ocr-doctor ocr-doctor
docker exec -it ocr-doctor bash
```

To stop the container:

```bash
docker stop ocr-doctor
```

To restart it later:

```bash
docker start ocr-doctor
docker exec -it ocr-doctor bash
```

**Note:** The current Docker configuration provides a development and experiment environment. A finished interactive CLI and hosted web interface are not yet available.

## Dataset

The current synthetic dataset contains:

- **30 source documents:** 10 each in Arabic, French and English.
- **5 image conditions per document:** clean, mild blur, moderate blur, strong blur and rotation.
- **150 generated images:** 90 training, 30 validation and 30 testing images.
- **Ground truth:** Original source text retained for recognition evaluation.

The dataset is split by source document so that generated variants of the same original text do not appear across different dataset splits.

Arabic text is rendered using appropriate shaping support.

Synthetic data provides known degradation conditions and exact source text, making controlled experiments possible. However, it does not reproduce every characteristic of real photographs, such as complex shadows, perspective distortion, paper texture and camera compression.

Real-world document photographs will be added in a later development stage.

## Project Structure

```text
OCR_Doctor/
│
├── ocr_doctor/
│   ├── analysis/          Image-quality indicators
│   ├── dataset/           Synthetic dataset generation
│   ├── domain/            Shared data models
│   ├── evaluation/        CER, WER and evaluation utilities
│   ├── ocr/               OCR interface and Tesseract adapter
│   └── preprocessing/
│       ├── base.py
│       └── steps/         Deskewing and contrast enhancement
│
├── experiments/           Experimental scripts and tests
│   └── results/           Experiment notes and results
│
├── scripts/               Project utilities
├── docs/                  Documentation and pipeline diagrams
├── results/               Consolidated experimental results
├── tests/                 Automated tests
├── data/                  Generated images and dataset splits
│
├── Dockerfile
├── requirements.txt
└── README.md
```

The architecture is intended to evolve as adaptive selection and the complete processing pipeline are implemented.

### Design Principles

The project follows several software design principles:

- **Adapter pattern:** Separates the Tesseract implementation from the rest of the system.
- **Abstraction:** Provides a common interface for preprocessing operations.
- **Modularity:** Keeps image analysis, preprocessing, OCR and evaluation as separate components.
- **Testability:** Supports independent testing of individual components.
- **Immutable data models:** Helps maintain consistent quality profiles and experiment results.

A registry, factory and dependency-injection architecture may be introduced as the pipeline grows.

## AI Research Direction

OCR Doctor investigates two complementary AI directions.

### 1. Machine Learning for Adaptive Preprocessing

This is the core applied-AI research direction.

The system will use image-quality indicators such as blur, skew, contrast and lighting as features for selecting suitable preprocessing strategies.

Two approaches will be investigated:

**Rule-Based Selection**

- Use thresholds derived from training-data analysis.
- Select operations according to detected image defects.
- Provide explanations for selection decisions.

**Learned Selection**

- Investigate Decision Tree and Random Forest models.
- Use image-quality measurements as input features.
- Predict suitable preprocessing strategies.
- Compare learned selection against explicit rules.

The objective is to determine whether machine learning provides measurable improvements over fixed and rule-based preprocessing.

### 2. Optional LLM-Assisted Document Understanding

A future extension is to investigate Large Language Models (LLMs) after OCR extraction.

Potential capabilities include:

- Extracting tables into structured, editable data.
- Generating summaries of document contents.
- Organizing extracted information into structured JSON.
- Supporting further document analysis.

This component would complement the OCR engine, not replace it.

Any future integration would require explicit consent before external document processing, structured output validation, prompt-injection safeguards and request limits.

Neither the adaptive ML selectors nor the LLM features should be considered completed functionality at this stage.

## Tech Stack and AI Tools

**Languages and libraries**

- Python 3.12
- OpenCV
- Pillow
- NumPy
- pytest
- Ruff

**OCR**

- Tesseract OCR
- Arabic, English and French language data

**Development environment**

- Docker
- Git
- GitHub

**Planned technologies**

- scikit-learn
- Streamlit
- Pydantic

**AI tools used during development**

ChatGPT and Claude were used for planning, technical explanations, code assistance and documentation drafting. The author is responsible for reviewing, implementing, running and testing the project.

## Limitations

- **Synthetic-to-real-world gap:** Most current data is synthetic. Real photographs introduce shadows, perspective distortion, paper texture and compression artefacts.
- **Quality indicators:** Current scores are heuristic measurements, not perfect representations of human readability.
- **Language differences:** Arabic, French and English have different script and recognition characteristics. Results must be evaluated separately rather than generalized across languages.
- **Preprocessing trade-offs:** A transformation that improves one image may damage another.
- **Computational cost:** Adaptive processing introduces analysis overhead. Accuracy improvements must therefore be evaluated alongside latency.
- **Experimental scope:** Preliminary component tests do not establish that adaptive preprocessing improves overall OCR performance.

## What Happens Next

Over the next three months, the development priorities are:

1. Complete the preprocessing pipeline with thresholding, denoising and additional image-enhancement operations.
2. Develop an explainable rule-based selector.
3. Establish controlled comparisons against raw OCR and fixed preprocessing.
4. Investigate Decision Tree and Random Forest models for learned selection.
5. Expand the dataset with real document photographs in all three languages.
6. Evaluate performance using CER, WER and processing latency.
7. Develop a Streamlit interface for interactive document processing.
8. Investigate perspective correction, page detection and retake recommendations.

An optional future direction is LLM-assisted table extraction and document summarization, with validated outputs and explicit user consent.

## Author

**Fairouz Cheikh Bassa**

Sole developer responsible for the project concept, research direction, technical architecture, implementation, experiments, evaluation and documentation.

## References

1. Smith, R. (2007). *An Overview of the Tesseract OCR Engine.* ICDAR 2007, pp. 629–633.  
   https://doi.org/10.1109/ICDAR.2007.4376991

2. Sauvola, J., & Pietikäinen, M. (2000). *Adaptive document image binarization.* Pattern Recognition, 33(2), 225–236.  
   https://doi.org/10.1016/S0031-3203(99)00055-2

3. Alaei, A., Bui, V., Doermann, D., & Pal, U. (2024). *Document Image Quality Assessment: A Survey.* ACM Computing Surveys, 56(2), Article 29.  
   https://doi.org/10.1145/3606692

4. Eutamene, A., Kholladi, M. K., Gaceb, D., & Belhadef, H. (2017). *A Dual PSO-Adaptive Mean Shift for Preprocessing Optimization on Degraded Document Images.* International Journal of Applied Metaheuristic Computing, 8(1), 61–76.  
   https://doi.org/10.4018/IJAMC.2017010104

### Technical Documentation

- Tesseract OCR: https://tesseract-ocr.github.io/
- OpenCV: https://docs.opencv.org/
- scikit-learn: https://scikit-learn.org/stable/
- Pillow: https://pillow.readthedocs.io/
- pytest: https://docs.pytest.org/

---

*OCR Doctor — Towards intelligent, adaptive and quality-aware document understanding.*
