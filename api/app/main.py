from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse


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


class DirectoryBrowser:
    """ Simple directory browser class """

    def __init__(self) -> None:
        self.paths = self.__decode_routes_from_file()

    def filter(self, key) -> Union[list, dict, None]:
        """ Returns a file object or directory dictionary based on it's key"""
        if key in self.paths:
            return self.paths[key]
        return None

    def __decode_routes_from_file(self) -> dict:
        """This transforms the format given to a routes format"""
        # file = open('directory.json', encoding='utf-8')

        # data = json.load(file)

        # file.close()

        return {
            '/': [{"type": "dir", "name": "home"}],
            '/home': [{"type": "dir", "name": "myname"}],
            '/home/myname':  [
                {"type": "file", "name": "filea.txt"},
                {"type": "file", "name": "fileb.txt"},
                {"type": "dir", "name": "projects"}
            ],
            '/home/myname/filea.txt': {"type": "file", "name": "filea.txt"},
            '/home/myname/fileb.txt': {"type": "file", "name": "fileb.txt"},
            '/home/myname/projects': [{"type": "dir", "name": "mysupersecretproject"}],
            '/home/myname/projects/mysupersecretproject': [
                {"type": "file", "name": "mysupersecretfile"}
            ],
            '/home/myname/projects/mysupersecretproject/mysupersecretfile': {
                "type": "file",
                "name": "mysupersecretfile"
            }
        }


Browser = DirectoryBrowser()


@ app.get("/{full_path:path}")
def return_path(full_path: str):
    """ Returns """
    path = f"/{full_path}"
    data = Browser.filter(path)
    if data:
        return JSONResponse(data, status_code=200)
    return JSONResponse({"message": "Not found"}, status_code=400)
