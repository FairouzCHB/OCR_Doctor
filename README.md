# OCR Doctor

### Intelligent, Quality-Aware Multilingual OCR

OCR Doctor is an individual AI engineering project exploring how document-image analysis and adaptive preprocessing can improve text extraction from imperfect documents in Arabic, French, and English.

## 1. Project Overview

Traditional OCR systems can struggle with documents affected by blur, rotation, low contrast, uneven lighting, noise, or low resolution.

OCR Doctor explores a different approach: rather than applying the same preprocessing operations to every image, the system first analyzes document quality, identifies potential defects, and aims to select the most appropriate corrections before text recognition.

The long-term objective is to develop an intelligent document-processing pipeline that can diagnose, improve, recognize, and evaluate document images.

## 2. The Main Idea

The project follows five main stages:

1. **Analyze:** Measure blur, skew, contrast, and lighting.
2. **Diagnose:** Identify image-quality problems.
3. **Select:** Determine which preprocessing operations are appropriate.
4. **Recognize:** Extract text using an OCR engine.
5. **Evaluate:** Compare recognition results using CER and WER.

The central research question is whether adaptive preprocessing can outperform fixed preprocessing strategies across different languages and image conditions.

## 3. Current Implementation

- Image-quality analysis using OpenCV.
- Blur, skew, contrast, and lighting indicators.
- Tesseract OCR integration.
- Arabic, French, and English language support.
- Character Error Rate (CER) and Word Error Rate (WER).
- Synthetic document dataset and degradation experiments.
- Initial deskewing and CLAHE preprocessing experiments.
- Automated testing with pytest.
- Code-quality checks with Ruff.

The current implementation is a research prototype. The complete adaptive selection pipeline and user interface are still under development.

## 4. Technology Stack

Python, Tesseract OCR, OpenCV, Pillow, NumPy, Docker, pytest, Ruff, Git and GitHub.

Planned technologies include Streamlit and scikit-learn.

## 5. Architecture

The intended architecture separates the system into modular components:

- `domain/`: shared data models.
- `analysis/`: image-quality analysis.
- `preprocessing/`: image enhancement operations.
- `selection/`: rule-based and learned strategy selection.
- `ocr/`: OCR engine interfaces and implementations.
- `evaluation/`: metrics and experiments.
- `ai/`: optional AI-assisted document understanding.
- `security/`: image validation and safeguards.
- `pipeline.py`: orchestration of the complete workflow.
- `app/`: future user interface.

The architecture is designed to make components replaceable, testable, and comparable.

## 6. Installation and Execution

### Requirements

- Git
- Docker Desktop or Docker Engine
- Python development environment (for local development)

### Clone the repository

```bash
git clone https://github.com/FairouzCHB/OCR_Doctor.git
cd OCR_Doctor
```

### Build the Docker image

```bash
docker build -t ocr-doctor .
```

### Run the container

```bash
docker run --rm ocr-doctor
```

The current Docker image provides the project's configured execution environment. Individual experiments and scripts should be run according to their actual entry points.

### Run tests

```bash
pytest
```

### Check code quality

```bash
ruff check .
ruff format --check .
```

**Note:** The CLI workflow is evolving. Exact commands for individual analysis, OCR, preprocessing, and evaluation experiments will be documented as their entry points are finalized.

## 7. Evaluation Methodology

The project uses two principal OCR metrics:

- **CER:** Character Error Rate.
- **WER:** Word Error Rate.

The planned experiments compare raw OCR, fixed preprocessing, rule-based adaptive preprocessing, and learned adaptive preprocessing.

Results will be analyzed by language and degradation type, with processing time considered alongside recognition quality.

## 8. Research Roadmap

- Complete the preprocessing pipeline.
- Expand the multilingual dataset.
- Validate image-quality indicators.
- Develop an explainable rule-based selector.
- Compare adaptive strategies against fixed baselines.
- Investigate decision trees and random forests for learned selection.
- Build a user-friendly interface.
- Explore secure document processing and optional AI-assisted features.
- Evaluate the system on real-world document images.

## 9. Limitations

OCR Doctor is not yet a finished or deployed application. The dataset requires further expansion, particularly with real-world images. The complete adaptive selector, interface, and broader experimental evaluation remain future work.

The project prioritizes measurable improvements rather than assuming that every preprocessing operation improves OCR.

## 10. Author

**Fairouz Cheikh Bassa**

Individual developer responsible for the project's research direction, architecture, implementation, experiments, and evaluation.

---

OCR Doctor — An ongoing exploration of intelligent document understanding.
