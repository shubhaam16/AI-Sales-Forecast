from pathlib import Path
from fastapi import HTTPException,UploadFile 

class FileValidator:
    """
    handles validation for the uploaded files 
    """
    """Allow file extension"""
    
    ALLOWED_EXTENSIONS ={".csv",".xlsx",".xls"}

    # Max file limit size (10 mb)

    MAX_FILE_SIZE= 10*1024*1024

    @classmethod
    async def validate (cls,file:UploadFile):
        cls.validate_filename(file)
        cls.validate_extension(file)
        await cls.validate_size(file)

    @classmethod
    def validate_filename(cls,file:UploadFile):
        if not file.filename:
            raise HTTPException(
                status_code=400,
                detail="filename is missing"
            )
        
    @classmethod
    def validate_extension(cls,file:UploadFile):
        extension = Path(file.filename).suffix.lower()
        if extension not in cls.ALLOWED_EXTENSIONS:
            raise HTTPException(
                status_code=400,
                detail=f"Unsupported file type: {extension}"
            )
    @classmethod
    async def validate_size(cls, file: UploadFile):

        contents = await file.read()

        if len(contents) > cls.MAX_FILE_SIZE:
            raise HTTPException(
                status_code=400,
                detail="File size exceeds 10 MB."
            )
        
        await file.seek(0)