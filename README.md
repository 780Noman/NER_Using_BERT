---
title: BERT for Named Entity Recognition
emoji: 🤖
colorFrom: indigo
colorTo: blue
sdk: streamlit
sdk_version: "1.33.0"
app_file: app.py
pinned: false
---

<div align="center">

# **Fine-Tuned BERT for Named Entity Recognition (NER)**

[![Hugging Face App](https://img.shields.io/badge/🤗%20Hugging%20Face-App-blue.svg)](https://huggingface.co/spaces/Nomi78600/bert-ner-app)
[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow.svg)](https://huggingface.co/Nomi78600/bert-ner-squad)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

</div>

This project provides a complete workflow for fine-tuning a `bert-base-cased` model for Named Entity Recognition (NER) and deploying it as an interactive web application using Streamlit and Hugging Face.

The application identifies four types of named entities in user-provided text:
- **<font color="#ffc107">PER</font>**: Person
- **<font color="#007bff">ORG</font>**: Organization
- **<font color="#28a745">LOC</font>**: Location
- **<font color="#dc3545">MISC</font>**: Miscellaneous

---

## 🚀 Live Demo

A live version of this application is deployed and running on Hugging Face Spaces.

**[➡️ Access the Live Application Here](https://huggingface.co/spaces/Nomi78600/bert-ner-app)**

---

## ✨ Core Features

- **Interactive UI**: A clean and simple user interface powered by Streamlit for easy interaction.
- **Real-time NER**: Input any text and get immediate NER predictions from the fine-tuned BERT model.
- **Rich Entity Highlighting**: Identified entities are highlighted with color-coded labels directly in the input text for clear and intuitive visualization.
- **Extracted Entity List**: A clean list of all recognized entities and their types is displayed below the main analysis.
- **Hosted on the Hub**: The fine-tuned model is hosted on the [Hugging Face Hub](https://huggingface.co/Nomi78600/bert-ner-squad), allowing for easy integration and access.

---

## 🛠️ Technologies & Frameworks

| Category      | Technology                                                                                                                                |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **Modeling**  | `Python`, `PyTorch`                                                                                                                       |
| **NLP**       | `Hugging Face Transformers` (for model architecture), `Hugging Face Datasets` (for data handling)                                         |
| **Web App**   | `Streamlit`                                                                                                                               |
| **Deployment**| `Hugging Face Spaces`                                                                                                                     |
| **Dataset**   | `CoNLL-2003`                                                                                                                              |
| **Base Model**| `bert-base-cased`                                                                                                                         |

---

## ⚙️ Setup and Local Installation

To run this project on your local machine, please follow these steps.

### Prerequisites

- Python 3.8+
- Git

### Installation Steps

1.  **Clone the repository:**
    Open your terminal and clone the repository, then navigate into the project directory.
    ```bash
    git clone https://github.com/780Noman/NER_Using_BERT.git
    cd NER_Using_BERT
    ```

2.  **Set up a virtual environment (Recommended):**
    This isolates the project's dependencies from your system's Python installation.
    ```bash
    # Create a virtual environment
    python -m venv venv

    # Activate it
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    The required packages are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Streamlit Application:**
    This command will start the local web server.
    ```bash
    streamlit run app.py
    ```
    Your web browser should open with the application running at `http://localhost:8501`. The app will download the model from the Hugging Face Hub on its first run.

---

## 🚢 Deployment

This application is deployed on **Hugging Face Spaces**. The deployment workflow is configured as follows:

1.  **Model Hosting**: The fine-tuned `BertForTokenClassification` model is hosted on the [Hugging Face Hub](https://huggingface.co/Nomi78600/bert-ner-squad).
2.  **Application Code**: The Streamlit application (`app.py`) loads the model directly from the Hub repository.
3.  **Environment**: The `requirements.txt` file specifies all dependencies, which are automatically installed by the Hugging Face Spaces environment.
4.  **Continuous Deployment**: Pushing changes to the `main` branch of the Space's repository automatically triggers a new build and deployment.

---

## 📂 Repository Structure

```
.
├── app.py                    # The core Streamlit application script
├── NER_Using_BERT_updated.ipynb # Jupyter Notebook with the model training workflow
├── requirements.txt          # Python dependencies for the project
├── .gitignore                # Files and directories to be ignored by Git
└── README.md                 # This file
```

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](https://opensource.org/licenses/MIT) file for details.
