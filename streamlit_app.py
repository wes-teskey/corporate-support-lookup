# streamlit_app.py

import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils_find_data_dir import find_data_directory
from PIL import Image

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Get the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    st.error("Error: OPENAI_API_KEY not found in .env file")
    st.stop()

# Initialize the OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

# Find the data directory
data_dir = find_data_directory()

# Load the FAISS index
index_path = os.path.join(data_dir, "customer_support_faiss_index")
db = FAISS.load_local(index_path, embeddings)

def search_policy(query):
    results = db.similarity_search_with_score(query, k=1)
    if results:
        doc, score = results[0]
        return doc.page_content, doc.metadata["source"], score
    return None, None, None

def get_image_path(md_filename):
    image_filename = md_filename.replace('.md', '.png')
    image_path = os.path.join(data_dir, image_filename)
    if os.path.exists(image_path):
        return image_path
    return None

st.set_page_config(layout="wide")

st.title("The Oil and Gas AI Company")

# Define your custom CSS to increase the font size of the input text
custom_css = """
<style>
    /* Change the font size of the input text */
    input {
        font-size: 30px !important;
    }
    /* Optionally, change the font size of the label */
    .stTextInput > label {
        font-size: 30px !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)
query = st.text_input("What are you looking for:", key="search_input")
search_button = st.button("Search")

if search_button and query:
    policy_content, source_file, score = search_policy(query)
    
    if policy_content and source_file:
        # Extract title from the markdown content
        title = policy_content.split('\n', 1)[0].strip('# ')
        
        # Display title
        st.markdown(f"# {title}")
        
        # Display image
        image_path = get_image_path(source_file)
        if image_path:
            image = Image.open(image_path)
            st.image(image, width=600)#use_column_width=True)
        
        # Display the rest of the content
        content_without_title = policy_content.split('\n', 1)[1]
        st.markdown(f"<div style='font-size: 30px; height: 400px; overflow-y: scroll;'>{'\n' + content_without_title}</div>", unsafe_allow_html=True)
    else:
        st.warning("No matching policy found.")