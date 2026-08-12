# Medsafe AI 

Medsafe AI is an intermediate Generative AI capstone project built to enhance patient safety by combining local **Tesseract OCR**, **RapidFuzz**, and **LLaMA 3 (via Ollama)**.

##  Features
1. **Medicine Interaction Analysis**: Fuzzy matching against a medical database paired with LLaMA 3 interaction evaluation.
2. **Prescription OCR & Extraction**: Upload prescription images to extract text using Tesseract and structure medicine data using LLaMA 3.
3. **Symptom Guidance & Risk Assessment**: Patient-centric symptom evaluation providing educational risk scoring and home-care guidelines.

## Tech Stack
- Python 3.10+
- Streamlit
- Ollama (LLaMA 3)
- Tesseract OCR / Pytesseract
- RapidFuzz

## Setup & Installation
1. Install **Ollama** locally and pull the LLaMA 3 model:
   ```bash
   ollama pull llama3