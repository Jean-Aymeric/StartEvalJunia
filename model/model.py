from __future__ import annotations
from contract.igrid import IGrid
from contract.imodel import IModel
from model.configuration import Configuration
from model.grid import Grid
from contract.igrid import IGrid


class Model(IModel):
    __configuration: Configuration
    __grid: Grid

    def __init__(self, configurationFileName: str):
        IModel.__init__(self)
        self.__configuration = Configuration(configurationFileName)
        self.__grid = Grid(self.__configuration.Configuration["width"],
                           self.__configuration.Configuration["height"],
                           self.getConfiguration("kindOfCell"))

    @property
    def Grid(self) -> IGrid:
        return self.__grid

    def getConfiguration(self, key: str) -> int | str:
        return self.__configuration.Configuration[key]

    def live(self) -> None:
        self.__grid.live()
        self._notify()
