from fastapi import APIRouter, UploadFile, File
from fastapi import Response
from fastapi.responses import StreamingResponse
from fastapi.responses import FileResponse
from controllers.uploadFileController import Clean_File
import os
import pathlib
from io import StringIO

import tabula


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), response_class = StreamingResponse):
    # uploads_dir = pathlib.Path(os.getcwd(), "uploads")
    # file_name = pathlib.Path(uploads_dir, file.filename)
    print(os.getcwd())

    cleaned_df = Clean_File(file.filename).clean_df()

    cleaned_df.to_csv('test.csv')
    
    file = StringIO()
    cleaned_df.to_csv(file)

    return StreamingResponse(
        iter([file.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"})
    