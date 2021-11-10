import shutil, os
from typing import List
from fastapi import FastAPI, UploadFile, File

# Permitir CORS
# https://stackoverflow.com/questions/65635346/how-can-i-enable-cors-in-fastapi

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

# # https://fastapi.tiangolo.com/tutorial/cors/?h=%20cors#use-corsmiddleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"mesage": "Hello World"}


@app.post("/upload/file")
async def root(file: UploadFile = File(...)): 
    # IMPORTANTE: nombre del parámetro, en este caso file tiene que coincidir con el nombre
    # del objeto agregado al FormData en el front end.
    with open(os.path.join("uploaded", file.filename), "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)


    return {"file_name": file.filename}


@app.post("/upload/files")
async def root(files: List[UploadFile] = File(...)):

    for file in files:
        with open(os.path.join("uploaded", file.filename), "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)


    return {"message": "Upload successful"}

# pip install fastapi
# pip install "uvicorn[standard]"
# pip install python-multipart


# uvicorn main:app --reload