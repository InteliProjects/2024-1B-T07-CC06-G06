import os
from fastapi import UploadFile

# Function to save an uploaded file to a specified location
def save_file(file_location: str, file: UploadFile):
    # Create the directory for the file if it doesn't exist
    os.makedirs(os.path.dirname(file_location), exist_ok=True)
    # Open the file in write-binary mode and write the uploaded file's contents
    with open(file_location, "wb") as buffer:
        buffer.write(file.file.read())
