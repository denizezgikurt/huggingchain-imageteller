from dotenv import find_dotenv, load_dotenv
from transformers import pipeline
from langchain import PromptTemplate, LLMChain, OpenAI
from langchain.chat_models import ChatOpenAI
import requests
import os
import streamlit as st
# import sys

# sys.path.append('/Users/dkurt02/miniconda3/lib/python3.10/site-packages/dotenv/__init__.py')


load_dotenv(find_dotenv())
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

st.write("HUGGINGFACEHUB_API_TOKEN", st.secrets["HUGGINGFACEHUB_API_TOKEN"])
st.write("OPENAI_API_KEY", st.secrets["OPENAI_API_KEY"])

# img2text
def img2text(url):
    image_to_text = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

    text = image_to_text(url)[0]["generated_text"]

    print(text)
    return text

img2text("photo.jpeg")

# llm storyteller
def generate_story(scenario):
    template = """
    You are a storyteller;
    You can generate a short story based on a simple narrative, the story should be no more than 100 words;
    
    CONTEXT: {scenario}
    STORY:
    """

    prompt = PromptTemplate(template=template, input_variables=["scenario"])

    story_llm = LLMChain(llm=OpenAI(
        model_name="gpt-3.5-turbo", temperature=1), prompt=prompt, verbose=True)
    
    story = story_llm.predict(scenario=scenario)

    print(story)
    return story


scenario = img2text("photo.jpeg")
story = generate_story(scenario)
                         

# text2speech
def text2speech(message):
    API_URL = "https://api-inference.huggingface.co/models/espnet/kan-bayashi_ljspeech_vits"
    headers = {"Authorization": f"Bearer {HUGGINGFACEHUB_API_TOKEN}"}
    payloads = {
        "inputs": message
    }

    response = requests.post(API_URL, headers=headers, json=payloads)
    with open('audio.flac', 'wb') as file:
        file.write(response.content)


#UI Streamlit
def main():

    st.set_page_config(page_title="imageteller", page_icon="🤖")
    
    st.header("ImageTeller: Turn any image into a story")
    uploaded_file = st.file_uploader("choose an image", type="jpg")

    if uploaded_file is not None:
        print(uploaded_file)
        bytes_data = uploaded_file.getvalue()
        with open(uploaded_file.name, "wb") as file:
            file.write(bytes_data)
        st.image(uploaded_file, caption='Uploaded Image.',
                use_column_width=True)
        scenario = img2text(uploaded_file.name)
        story = generate_story(scenario)
        text2speech(story)

        with st.expander("scenario"):
            st.write(scenario)
        with st.expander("story"):
            st.write(story)

    st.audio("audio.flac")


if __name__ == '__main__':
    main()