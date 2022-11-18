from fastapi import APIRouter, UploadFile, File
from controllers.uploadFileController import clean_file


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    cleaned_csv = clean_file(file)
    return {cleaned_csv}