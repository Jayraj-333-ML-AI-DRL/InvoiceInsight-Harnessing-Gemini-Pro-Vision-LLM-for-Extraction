# Importing necessary libraries
from dotenv import load_dotenv  # For loading environment variables from .env file
import os
import streamlit as st
from PIL import Image
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Function to get completion from OpenAI's chat API
def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    """
    Get completion from OpenAI's chat API.
    
    Args:
        messages (list): List of messages exchanged between system and user.
        model (str): Model name to use for completion.
        temperature (float): Sampling temperature for text generation.
        max_tokens (int): Maximum number of tokens to generate.

    Returns:
        str: Generated completion message.
    """
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

# Function to convert data into message format for model input
def convert_data_message(input, image_data, user_prompt):
    """
    Convert data into message format for model input.
    
    Args:
        input (str): System input message.
        image_data (list): List containing image data.
        user_prompt (str): User input prompt.

    Returns:
        list: List of messages formatted for model input.
    """
    system_message = str(input) + str(image_data)
    user_message = user_prompt
    
    messages =  [  
        {'role':'system', 'content': system_message},    
        {'role':'user', 'content': user_message},  
    ]
    return messages
 
# Function to set up image data from the uploaded file
def input_image_setup(uploaded_file):
    """
    Set up image data from the uploaded file.
    
    Args:
        uploaded_file (BytesIO): Uploaded image file.

    Returns:
        list: List containing image data.
    """
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
    messages = convert_data_message(input_prompt,image_data,user_input)
    # Get the model response
    response = get_completion_from_messages(messages)

    # Display the response
    st.subheader("The response is")
    st.write(response)
