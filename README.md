# Cyber_Threat_Detection_using_LSTM

## Project Overview
This project is a deep learning-based system that classifies cybersecurity-related text into predefined categories like malware, tools, vulnerability, identity, etc., using an LSTM model and Natural Language Processing (NLP). It includes a Flask web app for real-time predictions.

---

## Features
- Built using LSTM neural network for text classification
- Preprocessed using Keras Tokenizer and padding
- Web interface powered by Flask
- Accepts raw threat descriptions and returns predicted category and confidence

---

## Model Architecture
- Tokenizer (vocab size = 10,000)
- Embedding Layer (64-dim)
- LSTM Layer
- Dense Layers + Softmax output

---

## Technologies Used
- Python 3.x
- Keras / TensorFlow
- Flask
- Pandas, NumPy, Scikit-learn

---

## Folder Structure
```
cyber-threat-classifier/
├── app.py
├── cyber_threat_model.keras
├── tokenizer.pkl
├── label_encoder.pkl
├── cyber_threat_data.csv
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Installation
```bash
# Clone the repo
git clone https://github.com/your-username/cyber-threat-classifier.git
cd cyber-threat-classifier

# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
Then visit `http://127.0.0.1:5000` in your browser.

---

## Sample Input
```
"The attacker used Mimikatz to extract credentials from memory."
```
**Output:** tools

---

## Results
- Accuracy: 94.6%
- F1-Score: 94.1%
- Precision: 92.7%
- Recall: 95.5%


![Build](https://github.com/Murali-ux07/Cyber_Threat_Detection_using_LSTM/actions/workflows/python-lint.yml/badge.svg)
