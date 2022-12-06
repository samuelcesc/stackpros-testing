import json

from typing import Union


class DirectoryBrowser:
    """ Simple directory browser class """

    def __init__(self) -> None:
        self.output = {}
        self.paths = self.__decode_routes_from_file()

    def filter(self, key) -> Union[list, dict, None]:
        """ Returns a file object or directory dictionary based on it's key"""
        if key in self.paths:
            return self.paths[key]
        return None

    def _decode_routes(self, current_route: str, contents: dict) -> dict:
        """ Private method to decode routes """

        for key in contents:
            current_path = f"{current_route}/{key}"
            if 'type' in contents[key] and contents[key]['type'] == 'file':
                self.output[current_path] = {
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
                self.output[current_path] = parent_directory_contents
                self._decode_routes(
                    f"{current_path}", directory_contents
                )
        return self.output

    def __decode_routes_from_file(self) -> dict:
        """This transforms the format given to a routes format"""
        file = open('directory.json', encoding='utf-8')

        contents = json.load(file)

        data = self._decode_routes(
            current_route='', contents=contents['children'])

        file.close()

        return data
