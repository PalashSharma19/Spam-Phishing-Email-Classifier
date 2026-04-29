# Hybrid Spam & Phishing Detection System

This project implements a hybrid approach combining rule-based detection with machine learning models to identify spam and phishing messages.

## Features
- **Rule-based expert scoring system**: Detects urgency language, phishing URLs, and formatting issues.
- **ML-based text classification**: Custom-built TF-IDF and Logistic Regression implementation.
- **Hybrid decision logic**: Combines scores from ML and Rule Engine for better accuracy (WIP).

## Tech Stack
- **Python**: Core logic and scripting.
- **Pandas & Numpy**: Data processing and matrix operations.
- **SQLite / MySQL**: Future database integrations for storing classifications.

## Prerequisites
- Python 3.8+
- `pip` package manager

## Installation

1. Clone this repository:
   ```bash
   git clone <your-repository-url>
   cd "Email Classifier"
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows:
   .venv\Scripts\activate
   # macOS/Linux:
   source .venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To test the Machine Learning model, run:
```bash
python src/LR_model.py
```

## Project Structure
```
.
├── data/               # Raw and processed datasets
├── database/           # SQL schemas and DB connection scripts
├── notebooks/          # Jupyter notebooks for data exploration
├── rules/              # Rule-based scoring engine logic
├── src/                # Core ML model and text processing scripts
└── requirements.txt    # Python dependencies
```

## Project Status
- Rule engine implementation: **Completed**
- ML Model implementation: **Completed**
- Hybrid Logic & Database: **In Progress**

## License
[MIT](LICENSE)
