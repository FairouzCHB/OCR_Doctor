OCR Doctor
OCR Doctor is a research and development prototype for improving multilingual
text extraction from imperfect document images. It focuses on Arabic, French,
and English.

The project combines document-image quality analysis, Tesseract OCR,
preprocessing experiments, and quantitative evaluation. Its longer-term goal
is to select suitable preprocessing operations according to the defects
detected in each document.
The problem
OCR engines can make recognition errors when document images are blurred,
rotated, low in contrast, or unevenly illuminated. OCR Doctor investigates
how detecting these image-quality issues and applying suitable corrections
can improve text extraction.
Current prototype
Implemented components include:
- Image-quality analysis: blur, skew, contrast, and lighting indicators.
- OCR adapter: Tesseract integration with English (eng), French (fra),
  and Arabic (ara) language mappings.
- Preprocessing experiments: document deskewing and CLAHE-based contrast
  enhancement.
- Evaluation metrics: Character Error Rate (CER) and Word Error Rate (WER).
- Synthetic dataset: generated document images in the three target
  languages, with clean, blurred, and rotated variants.
- Development checks: automated tests with pytest and code-quality
  checks with Ruff.
This is an evolving prototype, not yet a hosted web application or a finished
end-user product. Some preprocessing operations and the intelligent
strategy-selection component remain planned work.
Technology stack
- Python
- Tesseract OCR
- OpenCV
- Pillow
- NumPy
- Docker
- pytest
- Ruff
Repository structure
ocr_doctor/
  analysis/             # Image-quality indicators and integrated analyzer
  dataset/              # Synthetic document rendering and generation
  domain/               # Shared domain models
  evaluation/           # CER and WER metrics
  ocr/                  # OCR interface and Tesseract adapter
  preprocessing/        # Preprocessing interfaces and operations
experiments/            # Experimental scripts and comparisons
tests/                  # Automated tests
scripts/                # Dataset and project utility scripts
data/                   # Local datasets and generated images (mostly ignored)
The exact contents may evolve as development continues.
Running locally
The project is developed and tested in a Docker-based environment.
1. Install Docker Desktop (or Docker Engine) and Git.
2. Clone the repository:
   git clone https://github.com/FairouzCHB/OCR_Doctor.git
   cd OCR_Doctor
3. Build the project image from the repository's Dockerfile:
   docker build -t ocr-doctor .
4. Run the image's configured default command:
   docker run --rm ocr-doctor
The current image includes Tesseract language data for Arabic, English, and
French. The repository is organized around experiments and Python modules;
there is not yet a deployed browser interface. To run a particular experiment
or test, inspect the corresponding script in experiments/ or scripts/.

To run the automated test suite from the project's configured development
environment:
pytest
To check code quality and formatting:
ruff check .
ruff format --check .
Evaluation
The project uses:
- CER (Character Error Rate): character-level difference between the
  recognized text and the reference text.
- WER (Word Error Rate): word-level difference between the recognized
  text and the reference text.
Current experiments are prototype-level sanity checks. Broader evaluation
across document types, layouts, and real-world images is planned.
Roadmap
- Complete and integrate the preprocessing pipeline.
- Expand and diversify the Arabic, French, and English dataset.
- Evaluate each preprocessing strategy against a baseline OCR system.
- Develop intelligent strategy selection based on image-quality indicators.
- Test on real-world document images.
- Build a user-friendly interface and consider deployment.
Team
Add each team member's full name and a concise, accurate description of their
actual contribution before submitting the repository.
- Fairouz Cheikh Bassa: project implementation and development. Update this
  line if needed to reflect the exact work completed.
- [Teammate full name]: [Add their actual contribution.]
Project status
Active prototype under development.
