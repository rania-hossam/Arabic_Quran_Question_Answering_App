import streamlit as st
import torch
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

# Streamlit app title
st.title("Quran Question Answering System")

# Base model architecture
base_model_name = "wissamantoun/araelectra-base-artydiqa"

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained(base_model_name)

# Path to the saved model weights
model_save_path = '/content/drive/MyDrive/QURAN_ARABIC_MODEL_FINE_TUNNING/MODEL_WEIGHTS.pth'

# Initialize the model with the base architecture and load your fine-tuned model weights
model = AutoModelForQuestionAnswering.from_pretrained(base_model_name)
model.load_state_dict(torch.load(model_save_path, map_location=torch.device('cpu')))
model.eval()  # Set the model to evaluation mode

# User inputs
context = st.text_area("Context", "Enter the context here...")
question = st.text_input("Question", "Enter your question here...")

# Answer button
if st.button("Get Answer"):
    if context and question:
        # Tokenize the input
        inputs = tokenizer.encode_plus(question, context, add_special_tokens=True, return_tensors="pt")
        input_ids = inputs["input_ids"]
        attention_mask = inputs["attention_mask"]

        # Perform inference
        with torch.no_grad():
            outputs = model(input_ids, attention_mask=attention_mask)
            answer_start_scores, answer_end_scores = outputs.start_logits, outputs.end_logits

            # Get the most likely beginning and end of answer
            answer_start = torch.argmax(answer_start_scores)
            answer_end = torch.argmax(answer_end_scores) + 1

            # Convert the tokens to the answer string
            answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[0][answer_start:answer_end]))

        # Display the answer
        st.write("Answer:", answer)
    else:
        st.write("Please provide both a context and a question.")
