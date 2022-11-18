from fastapi import APIRouter, UploadFile, File
from controllers.uploadFileController import clean_file


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    print(file.filename)
    cleaned_csv = clean_file(file.filename)
    return {1}