# MultiLanguage Invoice Extractor

This is a Streamlit web application designed to extract information from invoices using a pre-trained generative AI model provided by GenAI or OpenAI. The application allows users to upload an image of an invoice and provide a prompt, and then the model generates a response based on the image and prompt.

## Setup

To run this application, you need to follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Obtain an API key from GenAI/OPENAI and set it as an environment variable named `GENAI_APIKEY`/'`OPENAI_API_KEY`'.
4. Run the `app.py` file using Streamlit: `streamlit run app.py` or `app_1.py` if you're using OpenAI.

## Usage

Once the application is running, you can interact with it as follows:

1. **Input Prompt**: Enter a prompt that describes the information you want to extract from the invoice.

2. **Choose Image**: Upload an image file (JPEG or PNG format) of the invoice you want to process.

3. **Tell me about invoice**: Click this button to trigger the processing of the uploaded invoice and prompt.

4. **Response**: The application will display the response generated by the model based on the uploaded image and prompt.

## Notes

- Ensure that the uploaded image contains a clear representation of an invoice for accurate extraction.
- The response provided by the model may vary depending on the quality and content of the uploaded image and the input prompt.

## Dependencies

- Python 3.x
- Streamlit
- PIL (Python Imaging Library)
- dotenv
- google.generativeai / OpenAI

## About

This project utilizes Streamlit, a popular Python library for building interactive web applications, and the GenAI / OpenAI API for generating content based on images and prompts. It demonstrates the potential of AI in automating tasks such as invoice processing and information extraction.
