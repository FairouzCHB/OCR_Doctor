
# OCR Doctor — Initial Baseline

## Dataset
- Image: `data/test.png`
- Reference: `ground_truth/story.txt`
- OCR engine: Tesseract
- Language: English (`eng`)

## Evaluation configuration
- Character Error Rate (CER)
- Word Error Rate (WER)
- Normalization: collapse whitespace into single spaces
- Case and punctuation are preserved.

## Results

| Metric | Baseline |
|---|---:|
| CER | 0.56% |
| WER | 3.16% |

## Interpretation

Tesseract successfully extracted most of the text from this
sample image.

These results represent an initial sanity-check baseline,
not a general evaluation of OCR performance.

A larger and more diverse dataset will be required for
meaningful comparisons of preprocessing strategies.
