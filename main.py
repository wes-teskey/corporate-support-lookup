# main.py

import os
import sys
from dotenv import load_dotenv
import subprocess
import signal

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

# Check for required environment variables
required_env_vars = ['OPENAI_API_KEY']
missing_vars = [var for var in required_env_vars if not os.getenv(var)]
if missing_vars:
    print(f"Error: The following required environment variables are missing: {', '.join(missing_vars)}")
    sys.exit(1)


def run_streamlit():
    
    # Run the Streamlit app
    try:
        process = subprocess.Popen(["streamlit", "run", "streamlit_app.py"])
        process.wait()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running the Streamlit app: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print("Error: Streamlit is not installed or not in the system PATH.")
        print("Please install Streamlit using: pip install streamlit")
        sys.exit(1)

if __name__ == "__main__":
    # Set up signal handling
    signal.signal(signal.SIGINT, lambda sig, frame: sys.exit(0))
    
    run_streamlit()