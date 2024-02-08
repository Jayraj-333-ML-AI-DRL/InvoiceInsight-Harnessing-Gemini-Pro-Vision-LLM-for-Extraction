# Importing necessary libraries
from dotenv import load_dotenv  # For loading environment variables from .env file
import os
import streamlit as st
from PIL import Image
import google.generativeai as Genai

# Load environment variables from .env file
load_dotenv()

# Configure GenAI API with the API key from environment variables
Genai.configure(api_key=os.getenv("GENAI_APIKEY"))

# Load the Gemini Vision model
model = Genai.GenerativeModel('gemini-pro-vision')

# Function to get the model response based on input, image, and user prompt
def get_model_response(input, image, user_prompt):
    response = model.generate_content(input, image[0], user_prompt)
    return response

# Function to set up image data from the uploaded file
def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        # Prepare image data in parts with MIME type and bytes data
        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the MIME type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        # Raise error if no file uploaded
        raise FileNotFoundError("No file uploaded") 

# Set page configuration
st.set_page_config(
    page_title="My Streamlit App",
)

# Streamlit UI elements
st.header("MultiLanguage Invoice Extractor")

# Text input for user prompt
user_input = st.text_input("Input prompt: ", key="input")

# File uploader for choosing the image of the invoice
uploaded_file = st.file_uploader("Choose image of the invoice", type=[".jpg", "png"])

# Display the uploaded image if available
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

# Button to trigger processing of the invoice
submit = st.button("Tell me about invoice")

# Input prompt for the model
input_prompt = """You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image"""

# Process the invoice when the submit button is clicked
if submit:
    # Setup image data for processing
    image_data = input_image_setup(uploaded_file)
    
    # Get the model response
    response = get_model_response(input_prompt, image_data, user_input)
    
    # Display the response
    st.subheader("The response is")
    st.write(response)
