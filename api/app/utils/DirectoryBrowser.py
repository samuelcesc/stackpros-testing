import json

from typing import Union


class DirectoryBrowser:
    """ Simple directory browser class """

    def __init__(self) -> None:
        self.paths = self.__decode_routes_from_file()

    def filter(self, key) -> Union[list, dict, None]:
        """ Returns a file object or directory dictionary based on it's key"""
        if key in self.paths:
            return self.paths[key]
        return None

    def decode_routes(self, current_route: str, contents: dict) -> dict:
        """ Private method to decode routes """
        output = {}

        for key in contents:
            if 'type' in contents[key] and contents[key]['type'] == 'file':
                next_path = f"{current_route}/{key}"
                output[next_path] = {
                    "type": contents[key]['type'],
                    "name": key
                }
            else:
                parent_directory_contents = []
                directory_contents = contents[key]['children']
                for child in directory_contents:
                    parent_directory_contents.append({
                        "type": directory_contents[child]['type'],
                        "name": child
                    })
                output[current_route] = parent_directory_contents
                self.decode_routes(
                    f"{current_route}", directory_contents
                )
        return output

    def __decode_routes_from_file(self) -> dict:
        """This transforms the format given to a routes format"""
        file = open('directory.json', encoding='utf-8')

        contents = json.load(file)

        data = self.decode_routes(
            current_route='', contents=contents['children'])

        # print(data)

        file.close()

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
