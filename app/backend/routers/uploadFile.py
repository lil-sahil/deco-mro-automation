from fastapi import APIRouter, UploadFile, File
from tempfile import NamedTemporaryFile
from fastapi.responses import StreamingResponse

from controllers.uploadFileController import Clean_File
import os
import pathlib
from io import StringIO

import tabula


router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    

    # Refer to this stackoverflow post: 
    # https://stackoverflow.com/questions/70520522/how-to-upload-file-in-fastapi-then-to-amazon-s3-and-finally-process-it
    temp = NamedTemporaryFile(delete=False)
    try:
        try:
            contents = file.file.read()
            with temp as f:
                f.write(contents)
        except Exception:
            return {"message": "There was an error uploading the file"}
        finally:
            file.file.close()
        
        cleaned_df = Clean_File(temp.name).clean_df()
        
    except Exception:
        return {"message": "There was an error processing the file"}
    finally:
        #temp.close()  # the `with` statement above takes care of closing the file
        os.remove(temp.name)  # Delete temp file

    
    file = StringIO()
    cleaned_df.to_csv(file)

    return StreamingResponse(
        iter([file.getvalue()]),
        media_type="text/csv",
        headers={"Content-Disposition": f"attachment; filename=data.csv"})
    