from fastapi import FastAPI, UploadFile, Form, File
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

import shutil
import uuid
import os

from services.parser import parse_message
from services.word_filler import fill_word_template


app = FastAPI(title="Word Document Filling API")


@app.post("/api/upload-and-fill")
async def upload_and_fill(
    file: UploadFile = File(...),
    message: str = Form(...)
):
    """
    API:
    - Upload a Word (.docx) template containing placeholders
    - Provide information in natural language
    - Receive a filled Word document
    """

    template_path = f"{uuid.uuid4()}_template.docx"
    output_path = f"{uuid.uuid4()}_output.docx"

    
    with open(template_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    
    data = parse_message(message)

    
    fill_word_template(template_path, output_path, data)

    return FileResponse(
        output_path,
        media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        filename="filled_document.docx"
    )


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app.mount(
    "/frontend",
    StaticFiles(directory=os.path.join(BASE_DIR, "frontend"), html=True),
    name="frontend"
)
