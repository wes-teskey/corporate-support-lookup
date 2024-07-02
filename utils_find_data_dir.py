# utils.py

import os
import sys

def find_data_directory():
    """
    Find and return the path to the data directory.
    
    This function assumes that:
    1. It's being called from a script in the 'src' directory.
    2. The 'data' directory is at the same level as 'src'.
    
    Returns:
    str: Absolute path to the data directory.
    """
    # Get the directory of the current script
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Go up one level to the parent directory
    parent_dir = os.path.dirname(current_dir)
    
    # Construct the path to the data directory
    data_dir = os.path.join(parent_dir, 'data')
    
    # Check if the data directory exists
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory not found at {data_dir}")
    
    return data_dir

# You can test the function here
if __name__ == "__main__":
    try:
        data_path = find_data_directory()
        print(f"Data directory found at: {data_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
