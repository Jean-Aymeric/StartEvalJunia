import json


class Configuration:
    __configurationFileName: str
    __configuration: [str]

    def __init__(self, configurationFileName: str):
        self.__configurationFileName = configurationFileName
        self.__loadConfiguration()

    @property
    def Configuration(self) -> [str]:
        return self.__configuration

    def __loadConfiguration(self):
        with open(self.__configurationFileName) as messageFile:
            self.__configuration = json.load(messageFile)
