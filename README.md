# Fine-Tuned BERT for Named Entity Recognition (NER)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-streamlit-app-url.streamlit.app) 

This project contains a complete end-to-end workflow for fine-tuning a `bert-base-cased` model for Named Entity Recognition (NER) on the CoNLL-2003 dataset. The fine-tuned model is served via an interactive web application built with Streamlit.

The application identifies four types of named entities in user-provided text:

- **PER**: Person
- **ORG**: Organization
- **LOC**: Location
- **MISC**: Miscellaneous

## 🚀 Live Demo

A live version of this application is deployed on Streamlit Community Cloud.

**[➡️ Access the Live Application Here](https://your-streamlit-app-url.streamlit.app)** `<!-- Replace with your actual Streamlit URL -->`

---

## 📸 Application Screenshot

*(It is highly recommended to add a screenshot or GIF of your application in action here. This significantly improves the presentation of your project.)*


---

## ✨ Features

- **Interactive UI**: A clean and simple user interface powered by Streamlit.
- **Real-time NER**: Input any text and get immediate NER predictions.
- **Entity Highlighting**: Identified entities are highlighted with color-coded labels directly in the input text for easy visualization.
- **Extracted Entity List**: A clear list of all recognized entities and their types is displayed below the analysis.
- **Fine-Tuned Model**: Utilizes a BERT model specifically fine-tuned on a standard NER dataset for high accuracy.

---

## 🛠️ Technologies Used

- **Backend & Modeling**: Python, PyTorch
- **NLP Framework**: Hugging Face (`transformers`, `datasets`, `accelerate`)
- **Web Framework**: Streamlit
- **Dataset**: CoNLL-2003
- **Base Model**: `bert-base-cased`

---

## ⚙️ Setup and Local Installation

To run this project on your local machine, please follow these steps:

### Prerequisites

- Python 3.8+
- Git and Git LFS ([Git LFS Installation Guide](https://git-lfs.github.com/))

### Installation Steps

1. **Clone the repository:**
   Open your terminal and clone the repository, then navigate into the project directory.

   ```bash
   git clone https://github.com/780Noman/NER_Using_BERT.git
   cd NER_Using_BERT
   ```
2. **Set up a virtual environment (Recommended):**

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate it
   # On Windows:
   .\venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install dependencies:**
   The required packages are listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   *Note: If you encounter issues with the large model file, ensure Git LFS is installed and pull the LFS files.*

   ```bash
   git lfs pull
   ```
4. **Run the Streamlit Application:**

   ```bash
   streamlit run app.py
   ```

   Your web browser should open with the application running locally at `http://localhost:8501`.

---

## 🚢 Deployment

This application is deployed on **Streamlit Community Cloud**. The deployment process leverages Git LFS to handle the large model file (model.safetensors). The Streamlit Cloud platform automatically detects the `requirements.txt` file and installs all necessary dependencies to run the application.

---
