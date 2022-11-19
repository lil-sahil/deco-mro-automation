from fastapi import APIRouter, UploadFile, File
from fastapi import Response
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
import os
from io import StringIO




router = APIRouter()

@router.get("/get_file")
async def get_file():
    # uploads_dir = pathlib.Path(os.getcwd(), "uploads")
    # file_name = pathlib.Path(uploads_dir, file.filename)
    print(os.getcwd())

    headers = {'Access-Control-Expose-Headers': 'Content-Disposition'}
    
    return FileResponse(
        "test.csv",filename="hello.csv", headers=headers)
    