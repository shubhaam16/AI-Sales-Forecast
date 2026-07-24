import os 
import shutil
from pathlib import Path

from fastapi import UploadFile

class LocalStorage:
    BASE_UPLOAD_DIR = "uploads"

    @classmethod
    def save_file(cls,project_id:str,file:UploadFile) -> str:
        """
        Save uploaded file inside:
        uploads/<project_id>/

        Returns the saved file path.
        """
        project_directory=Path(cls.BASE_UPLOAD_DIR)/project_id
        project_directory.mkdir(parents=True,exist_ok =True)
        file_path = project_directory/file.filename
        with open(file_path,"wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return str(file_path)
    
    @classmethod
    def delete_file(cls,file_path:str):
        if os.path.exists(file_path):
            os.remove(file_path)