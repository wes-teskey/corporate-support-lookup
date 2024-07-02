# generate_policy_descriptions.py

import os
import sys
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from company_docs_list import get_docs_list
from utils_find_data_dir import find_data_directory

# Load environment variables from .env file in the parent directory
dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(dotenv_path)

# Get the API key
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
if not ANTHROPIC_API_KEY:
    print("Error: ANTHROPIC_API_KEY not found in .env file")
    sys.exit(1)

# Initialize the ChatAnthropic model
llm = ChatAnthropic(
    model="claude-3-5-sonnet-20240620",
    temperature=0.7,
    max_tokens=1024,
    timeout=None,
    max_retries=2,
)

def generate_document_description(doc_name):
    """Generate a detailed document description using Claude API."""
    messages = [
        (
            "system",
            "You are a Senior Customer Support Documentation Specialist tasked with drafting customer support documents. "
            "You have full authority to create these documents as there are no current existing procedures. "
            "Your task is to draft a detailed and professional documents as md files."
            "These are template documents, so the names of equipment and procedures should be invented or made up by you."
        ),
        (
            "human",
            f"Please draft an appropriate customer support document for '{doc_name}' in about 500 words as an md file. "
            "The document should be detailed, professional."
            "This is a template document, so the names of equipment and procedures should be invented or made up by you."
        ),
    ]
    
    response = llm.invoke(messages)
    return response.content

def main():
    try:
        data_dir = find_data_directory()
        docs = get_docs_list()

        for i, doc in enumerate(docs, 1):
            print(f"Generating document {i}/{len(docs)}: {doc}")
            
            # Generate the document description
            description = generate_document_description(doc)
            
            # Create a file name (replace spaces with underscores and make lowercase)
            file_name = doc.replace(" ", "_").replace("/", "_").lower() + ".md"
            file_path = os.path.join(data_dir, file_name)
            
            # Save the description to a file
            with open(file_path, 'w') as f:
                f.write(description)
            
            print(f"Saved document description to {file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
