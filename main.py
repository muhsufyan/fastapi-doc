from fastapi import FastAPI, File, UploadFile

app = FastAPI()


@app.post("/files/")
# need File() for upload file
async def create_file(file: bytes = File()):
    return {"file_size": len(file)}

# File Parameters with UploadFile
"""
kelbhan UploadFile
* uses a "spooled" file:
A file stored in memory up to a maximum size limit, and after passing this limit it will be stored in disk.
* sehingga dpt menyimpan file yg besar tanpa mengonsumsi memory secara penuh
* atribut UploadFile dpt dilihat https://fastapi.tiangolo.com/tutorial/request-files/#uploadfile
"""
@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}

# NILAI DEFAULT PD UPLOADFILE
@app.post("/default/files/")
async def create_file(file: bytes | None = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/default/uploadfile/")
async def create_upload_file(file: UploadFile | None = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}

# ADD METADATA
@app.post("/addMetadata/files/")
    # description metadata
async def create_file(file: bytes = File(description="A file read as bytes")):
    return {"file_size": len(file)}


@app.post("/addMetadata/uploadfile/")
async def create_upload_file(
    # description metadata
    file: UploadFile = File(description="A file read as UploadFile"),
):
    return {"filename": file.filename}

# Multiple File Uploads
# upload several files at the same time. caranya  declare a list of bytes or UploadFile
@app.post("/multipleupload/files/")
# list of bytes
async def create_files(files: list[bytes] = File()):
# add metadata description
# async def create_files(files: list[bytes] = File(description="Multiple files as bytes")):
    return {"file_sizes": [len(file) for file in files]}


@app.post("/mulitpleupload/uploadfiles/")
# list of UploadFile
async def create_upload_files(files: list[UploadFile]):
# add metadata description
# async def create_files(files: list[bytes] = File(description="Multiple files as UploadFile")):
    return {"filenames": [file.filename for file in files]}

from fastapi.responses import HTMLResponse
@app.get("/")
async def main():
    content = """
<body>
    <form action="/mulitpleupload/files/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
    <form action="/mulitpleupload/uploadfiles/" enctype="multipart/form-data" method="post">
        <input name="files" type="file" multiple>
        <input type="submit">
    </form>
</body>
    """
    return HTMLResponse(content=content)