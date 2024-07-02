# setup_faiss_vector_db.py

import os
import sys
from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.schema.document import Document
from utils_find_data_dir import find_data_directory

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Get the API key
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
if not OPENAI_API_KEY:
    print("Error: OPENAI_API_KEY not found in .env file")
    sys.exit(1)

# Initialize the OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")

def setup_faiss_db():
    try:
        data_dir = find_data_directory()
        
        # Get all .md files in the data directory 
        txt_files = [f for f in os.listdir(data_dir) if f.endswith('.md')]
        
        documents = []
        for txt_file in txt_files:
            file_path = os.path.join(data_dir, txt_file)
            with open(file_path, 'r') as f:
                content = f.read()
                documents.append(Document(page_content=content, metadata={"source": txt_file}))
        
        print(f"Creating FAISS index for {len(documents)} documents...")
        
        # Create the FAISS index
        db = FAISS.from_documents(documents, embeddings)
        
        # Save the FAISS index
        index_path = os.path.join(data_dir, "policy_faiss_index")
        db.save_local(index_path)
        
        print(f"FAISS index saved to {index_path}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    setup_faiss_db()
