# OCR Doctor

### Intelligent, Quality-Aware Multilingual OCR

OCR Doctor is an individual AI engineering project exploring how document-image analysis, adaptive preprocessing, and machine learning can improve text extraction from imperfect documents in Arabic, French, and English.

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

The current prototype includes:

- Image-quality analysis using OpenCV.
- Blur, skew, contrast, and lighting indicators.
- Tesseract OCR integration.
- Arabic, French, and English language support.
- Character Error Rate (CER) and Word Error Rate (WER).
- Synthetic document dataset and degradation experiments.
- Initial deskewing and CLAHE preprocessing experiments.
- Automated testing with pytest.
- Code-quality checks with Ruff.

The complete adaptive selection pipeline and user interface are still under development.

## 4. AI and Intelligent Document Processing

OCR Doctor explores two complementary AI directions.

### 4.1 Machine Learning for Adaptive Preprocessing

This is the project's core applied-AI research direction.

Instead of applying identical image transformations to every document, the system aims to learn which preprocessing operations are most suitable according to the document's quality characteristics.

Two approaches will be investigated:

**Rule-based selection**

- Analyze blur, skew, contrast, and lighting.
- Derive decision thresholds from the training dataset.
- Select appropriate preprocessing operations.
- Provide explanations for each selection.

**Learned selection**

- Use image-quality indicators as machine-learning features.
- Investigate Decision Tree and Random Forest models.
- Train models to predict suitable preprocessing strategies.
- Compare learned decisions with rule-based selection.

The objective is to determine whether learned adaptive selection can improve OCR accuracy while controlling unnecessary transformations and processing time.

### 4.2 AI-Assisted Document Understanding

A second, more advanced direction is to explore Large Language Models (LLMs) to extend OCR Doctor beyond text extraction.

Potential capabilities include:

- **Table extraction:** Convert document tables into structured, editable data.
- **Document summarization:** Generate concise summaries of extracted content.
- **Information extraction:** Organize relevant document information into structured JSON.
- **Document analysis:** Support further interpretation of extracted content.

This component will be optional and complementary to the OCR engine, not a replacement for it.

Planned safeguards include structured output validation using Pydantic, protection against prompt injection, explicit consent before external image processing, and request and cost limits.

These AI capabilities are research and development objectives, not completed features.

## 5. Technology Stack

**Currently used:**

Python, Tesseract OCR, OpenCV, Pillow, NumPy, Docker, pytest, Ruff, Git and GitHub.

**Planned or under consideration:**

Streamlit, scikit-learn, Pydantic and an optional external LLM API.

## 6. Architecture

The intended architecture separates the system into modular components:

```text
app/                    User interface (planned)
ocr_doctor/
  domain/               Shared data models
  analysis/             Image-quality analysis
  preprocessing/        Image enhancement operations
  selection/            Rule-based and learned selectors
  ocr/                  OCR engine interfaces
  evaluation/            Metrics and experiments
  ai/                   Optional AI-assisted features
  feedback/             Feedback management
  security/             Upload validation and safeguards
  pipeline.py           Processing orchestration
data/                   Datasets and ground truth
experiments/             Experimental scripts
tests/                   Automated tests
```

The architecture is designed around modularity and replaceability:

- **Strategy pattern:** interchangeable preprocessing operations and selection methods.
- **Adapter pattern:** replaceable OCR engines and future LLM integrations.
- **Registry/factory:** consistent registration and creation of preprocessing operations.
- **Pipeline composition:** controlled execution of analysis, selection, preprocessing, and OCR.
- **Dependency injection:** independent components that are easier to test and compare.
- **Immutable data models:** structured profiles and results.

This is the target architecture; not every component has been implemented yet.

## 7. Installation and Execution

### Requirements

- Git
- Docker Desktop or Docker Engine

### Clone the repository

```bash
git clone https://github.com/FairouzCHB/OCR_Doctor.git
cd OCR_Doctor
```

### Build the Docker image

```bash
docker build -t ocr-doctor .
```

The image installs Python dependencies, Tesseract OCR, Arabic, English and French language data, and Noto fonts. It also creates a dedicated non-root application user.

### Start the development container

```bash
docker run -d --name ocr-doctor ocr-doctor
```

### Access the container

```bash
docker exec -it ocr-doctor bash
```

### Verify Tesseract languages

```bash
tesseract --list-langs
```

Expected languages include:

```text
ara
eng
fra
osd
```

### Run experiments

From inside the container, execute the available Python experiment scripts.

For example, if the script is present:

```bash
python experiments/test_deskew.py
```

Consult the `experiments/` and `scripts/` directories for available scripts.

### Run automated tests

```bash
pytest
```

### Check code quality

```bash
ruff check .
ruff format --check .
```

### Stop or restart the container

```bash
docker stop ocr-doctor
docker start ocr-doctor
```

To remove it:

```bash
docker rm -f ocr-doctor
```

**Note:** The current Docker configuration provides a persistent development environment. A finished interactive CLI and hosted web interface are planned future improvements.

## 8. Evaluation Methodology

The project uses two principal OCR metrics:

- **Character Error Rate (CER):** Measures character-level recognition errors.
- **Word Error Rate (WER):** Measures word-level recognition errors.

Planned experiments will compare:

1. Raw OCR without preprocessing.
2. OCR with a fixed preprocessing pipeline.
3. OCR with rule-based adaptive preprocessing.
4. OCR with learned adaptive preprocessing.
5. An oracle selection strategy as an experimental upper-bound reference.

Results will be analyzed by language and degradation type, with processing latency considered alongside recognition quality.

## 9. Research Roadmap

The development roadmap includes:

- Completing the preprocessing pipeline.
- Expanding the Arabic, French, and English dataset.
- Validating image-quality indicators.
- Developing an explainable rule-based selector.
- Comparing adaptive strategies against fixed baselines.
- Investigating Decision Trees and Random Forests for learned selection.
- Building a user-friendly interface.
- Implementing secure document-upload handling.
- Exploring AI-assisted table extraction and document summarization.
- Evaluating the system on real-world document images.
- Investigating feedback-driven improvements and deployment.

## 10. Limitations and Current Status

OCR Doctor is an evolving research prototype, not yet a finished or deployed application.

The dataset requires further expansion, particularly with real-world images. The complete adaptive selector, integrated preprocessing pipeline, user interface, and broader experimental evaluation remain future work.

The optional LLM capabilities are also planned research directions.

The project prioritizes measurable improvements rather than assuming that every preprocessing operation improves OCR. Both successful and unsuccessful experimental results will be considered.

## 11. Author

**Fairouz Cheikh Bassa**

Sole developer responsible for the project's research direction, architecture, implementation, experiments, and evaluation.

---

*OCR Doctor — Towards intelligent, adaptive, and quality-aware document understanding.*
