
import streamlit as st
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
import numpy as np

# --- CONFIGURATION ---
MODEL_REPO_ID = "Nomi78600/bert-ner-squad"
st.set_page_config(page_title="NER with BERT", page_icon="🤖", layout="wide")

# --- MODEL LOADING ---
@st.cache_resource
def load_model_and_tokenizer(repo_id):
    """Load the fine-tuned model and tokenizer from the Hugging Face Hub."""
    try:
        tokenizer = AutoTokenizer.from_pretrained(repo_id)
        model = AutoModelForTokenClassification.from_pretrained(repo_id)
        return tokenizer, model
    except OSError:
        st.error(f"Error loading model: Could not find repository '{repo_id}' on the Hugging Face Hub. Please check the name.")
        return None, None
    except Exception as e:
        st.error(f"An unexpected error occurred while loading the model: {e}")
        return None, None

# Load the model from the Hub
with st.spinner(f"Loading model '{MODEL_REPO_ID}' from Hugging Face Hub..."):
    tokenizer, model = load_model_and_tokenizer(MODEL_REPO_ID)

if model is None:
    st.error("Application failed to load the model. Please check the logs.")
    st.stop()

# --- NER VISUALIZATION ---
ENTITY_COLORS = {
    "PER": "#ffc107",  # Yellow
    "ORG": "#007bff",  # Blue
    "LOC": "#28a745",  # Green
    "MISC": "#dc3545", # Red
    "O": "#adb5bd"    # Gray for non-entities, though we won't highlight them
}
LABEL_NAMES = model.config.id2label

def get_entity_html(text, label):
    """Generates HTML for a single entity with a colored background."""
    entity_type = label.split('-')[-1]
    color = ENTITY_COLORS.get(entity_type, "#adb5bd")
    return f'<span style="background-color: {color}; color: white; padding: 0.2em 0.4em; margin: 0 0.2em; border-radius: 0.3em; font-weight: bold;">{text} <span style="font-size: 0.8em; opacity: 0.7;">{entity_type}</span></span>'

def visualize_ner(text, predictions):
    """Combines tokens and predictions into a visualized HTML string."""
    html_output = ""
    current_word = ""
    current_label = "O"

    for token, label in zip(text.split(), predictions):
        # If the label is a B-tag, start a new entity
        if label.startswith("B-"):
            # If there was a previous entity, add it to the output
            if current_word:
                if current_label != "O":
                    html_output += get_entity_html(current_word, current_label)
                else:
                    html_output += current_word + " "
            current_word = token + " "
            current_label = label
        # If it's an I-tag and matches the current entity type, continue it
        elif label.startswith("I-") and current_label.split('-')[-1] == label.split('-')[-1]:
            current_word += token + " "
        # Otherwise, it's a new word or an O-tag
        else:
            # Add the completed entity or word to the output
            if current_word:
                if current_label != "O":
                    html_output += get_entity_html(current_word.strip(), current_label) + " "
                else:
                    html_output += current_word
            
            # Reset for the current token
            current_word = token + " "
            current_label = "O" # Default to O if the label isn't B- or I-

    # Add the last processed word/entity
    if current_word:
        if current_label != "O":
            html_output += get_entity_html(current_word.strip(), current_label)
        else:
            html_output += current_word

    return html_output.strip()


# --- STREAMLIT APP LAYOUT ---
st.title("Named Entity Recognition (NER) with BERT")
st.markdown("Enter text below to identify entities like Persons (PER), Organizations (ORG), Locations (LOC), and Miscellaneous (MISC).")

text_input = st.text_area("Input Text", height=150, placeholder="Example: Elon Musk, the CEO of SpaceX, announced a new mission to Mars from their headquarters in California.")

if st.button("Analyze Text"):
    if not text_input:
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing..."):
            # 1. Tokenization
            inputs = tokenizer(text_input, return_tensors="pt", truncation=True, padding=True, is_split_into_words=False)
            
            # 2. Model Prediction
            with torch.no_grad():
                outputs = model(**inputs)
            
            predictions = np.argmax(outputs.logits.detach().numpy(), axis=2)
            
            # 3. Post-processing
            predicted_labels = []
            tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])
            
            for token, pred_id in zip(tokens, predictions[0]):
                if token not in (tokenizer.cls_token, tokenizer.sep_token, tokenizer.pad_token):
                    predicted_labels.append(LABEL_NAMES[pred_id])

            # This is a simplified alignment. For a more robust solution, we'd align subwords to words.
            # For this app, we'll assume a simple space-based tokenization for visualization.
            words = text_input.split()
            # Heuristic: Assign the first label of a word to the whole word.
            aligned_predictions = []
            label_idx = 0
            for word in words:
                word_tokens = tokenizer.tokenize(word)
                if label_idx < len(predicted_labels):
                    aligned_predictions.append(predicted_labels[label_idx])
                    label_idx += len(word_tokens)
                else:
                    aligned_predictions.append("O")


            # 4. Visualization
            st.subheader("Analysis Results")
            
            # A more robust visualization that handles subword tokenization better
            final_tokens = []
            final_labels = []
            word_ids = inputs.word_ids()
            
            previous_word_id = None
            for i, token_id in enumerate(inputs['input_ids'][0]):
                if token_id not in (tokenizer.cls_token_id, tokenizer.sep_token_id, tokenizer.pad_token_id):
                    word_id = word_ids[i]
                    if word_id is not None and word_id != previous_word_id:
                        start, end = inputs.token_to_chars(i)
                        word = text_input[start:end]
                        final_tokens.append(word)
                        final_labels.append(LABEL_NAMES[predictions[0][i]])
                    previous_word_id = word_id
            
            # Grouping entities
            grouped_entities = []
            current_entity = {"text": "", "label": ""}
            for token, label in zip(final_tokens, final_labels):
                if label.startswith("B-"):
                    if current_entity["text"]:
                        grouped_entities.append(current_entity)
                    current_entity = {"text": token, "label": label.split("-")[1]}
                elif label.startswith("I-") and current_entity["label"] == label.split("-")[1]:
                    current_entity["text"] += " " + token
                else:
                    if current_entity["text"]:
                        grouped_entities.append(current_entity)
                        current_entity = {"text": "", "label": ""}
                    # We don't add O-tagged words to the list of entities
            
            if current_entity["text"]:
                grouped_entities.append(current_entity)

            # Displaying the text with highlighted entities
            display_text = text_input
            for entity in reversed(grouped_entities): # Reverse to avoid index shifting
                entity_html = get_entity_html(entity["text"], entity["label"])
                # This is a simple text replace, might fail on overlapping entities
                display_text = display_text.replace(entity["text"], entity_html, 1)

            st.markdown(display_text, unsafe_allow_html=True)

            # Displaying entities as a list
            st.subheader("Extracted Entities")
            if grouped_entities:
                for entity in grouped_entities:
                    st.markdown(f"- **{entity['text']}** (`{entity['label']}`)")
            else:
                st.info("No entities were found in the text.")
