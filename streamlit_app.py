import streamlit as st
import os 
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="AIzaSyAvhUN0Nd2-HNvfFYHCWPj449g9iNGCwYo")

model=genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(input_text, image_data, prompt): #
    response= model.generate_content([input_text, image_data[0], prompt])
    return response.text

def input_image_details(uploaded_file): #to fetch the image
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue() #retrieves data of the file (we work with files as a byte array)
        image_parts=[
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file was uploaded.")

st.set_page_config(page_title="AI Invoice Generator")
st.sidebar.header("RoboBill")
st.sidebar.write("Made in Vietnam")
st.sidebar.write("Powered by Google GEMINI API")
st.header("Robobill")
st.subheader("Made in South Korea")
st.subheader("Manage your expenses with Robobill")
input = st.text_input("What do you want me to do?", key="input")
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "png", "jpeg"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
ssubmit = st.button("Submit")


input_prompt = """
You can identify and classify objects into calculators, electronics, keys, clothes, bottles, jewellery. You identify and return either calculator, electronics, keys, clothes, water bottles.
"""

if ssubmit:
    image_data = input_image_details(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input)
    st.subheader("Here's what you need to know!")
    st.write(response)
