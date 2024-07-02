# corporate-support-lookup
A lookup website to find company documents for customer support inquiries.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed the latest version of Python. You can download it from [here](https://www.python.org/downloads/).
- You have a package manager for Python, such as `pip`.
- Install node.js from https://nodejs.org/en if not already installed
- Install mermaid CLI from the command prompt: npm install -g @mermaid-js/mermaid-cli

## Setting Up a Virtual Environment

1. **Navigate to the project directory:**
cd path\to\your\project

2. **Create and activate virtual environment (example shown for windows):**
python -m venv venv
venv\Scripts\activate

3. **Install the required packages (shown for windows):**

pip install -r requirements.txt

## Windows Users: Resolving Microsoft Visual C++ 14.0 Build Tools Error

If you encounter an error related to chroma not being installed, 
please follow the steps below to resolve it:

### Step-by-Step Guide to Fix the Issue

#### Download the Microsoft C++ Build Tools:
1. Go to the [Microsoft C++ Build Tools download page](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. Click on the "Download Build Tools" button to download the installer.

#### Install the Build Tools:
1. Run the installer you downloaded (`vs_buildtools.exe`).
2. In the installer, choose the "Workloads" tab.
3. Select "Desktop development with C++".
4. Make sure to check the "C++ Build Tools" option.
5. Click on the "Install" button to begin the installation process. This may take some time depending on your internet speed and system performance.

#### Verify Installation:
After the installation is complete, verify the installation

## Description of Key Directories and Files

- **`data\`**: Contains all data-related files (make sure this is empty before running the py files)
- **`src\`**: Contains the source code of the project.
- **`venv\`**: Contains the virtual environment for the project.
- **`.env`**: Contains environment variables, including API keys.

### Environment Variables
The .env file in the root directory contains the following environment variable:

ANTHROPIC_API_KEY: The API key for accessing Anthropic services

OPENAI_API_KEY: The API key for accessing OpenAI services.

Caution: Using the above API keys can be really expensive. Please be mindful of your usage to avoid unexpected costs.

### Creating the `data\` Directory

Before running the project, ensure that the `data\` directory is created at the same level as the `src\` directory and that the data directory is empty before running the py files

## Usage
Run the following py files in the order given

generate_company_docs.py to create ficticious customer service documents

setup_faiss_vector_db.py to create the database for lookup

main.py to run the streamlit app in a web browser

If you want images to be displayed in the streamlit app when running main.py,
then find appropriate png images, and save them using the same name as the 
relevant md files in the `data\` directory. For example, if you had a pump-spec.md
file in the `data\` directory, and you save a pump-spec.png file in the `data\` directory,
the pump-spec.png file would be displayed in the streamlit app when the pump-spec.md
file was selected.