from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from .utils.DirectoryBrowser import DirectoryBrowser


app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


Browser = DirectoryBrowser(file_path="/code/app/directory.json")


@ app.get("/{full_path:path}")
def return_path(full_path: str):
    """ Returns """
    path = f"/{full_path}"
    data = Browser.filter(path)
    if data:
        return JSONResponse(data, status_code=200)
    return JSONResponse({"message": "Not found"}, status_code=400)
