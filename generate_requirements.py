# generate_requirements.py

import os
import subprocess
import sys

def install_pipreqs():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pipreqs"])
        print("pipreqs installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install pipreqs. Please install it manually using 'pip install pipreqs'")
        sys.exit(1)

def generate_requirements():
    # Get the project root directory (assuming this script is in the project root)
    project_root = os.path.dirname(os.path.abspath(__file__))
    
    try:
        # Run pipreqs
        subprocess.check_call(["pipreqs", project_root, "--force"])
        print(f"requirements.txt generated successfully in {project_root}")
    except subprocess.CalledProcessError:
        print("Failed to generate requirements.txt. Please check if pipreqs is installed correctly.")
        sys.exit(1)
    except FileNotFoundError:
        print("pipreqs not found. Installing pipreqs...")
        install_pipreqs()
        # Try generating requirements again
        generate_requirements()

if __name__ == "__main__":
    generate_requirements()
