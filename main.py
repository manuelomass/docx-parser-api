from fastapi import FastAPI, UploadFile, File
from docx import Document

app = FastAPI()

def parse_docx(file_bytes)
    doc = Document(file_bytes)
    text = n.join([p.text.strip() for p in doc.paragraphs if p.text.strip()])
    return text

@app.post(parse_docx)
async def parse(file UploadFile = File(...))
    if not file.filename.endswith(.docx)
        return {status error, reason Invalid file type}
    
    file_bytes = await file.read()
    content = parse_docx(file_bytes)

    if content.strip().lower() == not available
        return { status skip, reason Not Available }

    # Split into chunks of 500 chars
    chunks = [content[ii+500] for i in range(0, len(content), 500)]
    return {
        status ok,
        chunks [{chunk chunk} for chunk in chunks]
    }
