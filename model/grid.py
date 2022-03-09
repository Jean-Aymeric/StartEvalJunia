from typing import List
from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell
from contract.igrid import IGrid
from model.cell import Cell
from model.liveBehavior.randomLive import RandomLive
from model.liveBehavior.swapLive import SwapLive


class Grid(IGrid):
    __cells: List[List[Cell]]
    __width: int
    __height: int
    __liveBehavior: ILiveBehavior

    def __init__(self, width: int, height: int, kindOfCell: str):
        self.__width = width
        self.__height = height
        self.__cells = [[None] * width for _ in range(height)]
        if kindOfCell == "swap":
            self.__liveBehavior = SwapLive()
        elif kindOfCell == "random":
            self.__liveBehavior = RandomLive()
        for y in range(height):
            for x in range(width):
                self.__cells[y][x] = Cell(self.__liveBehavior)

    def cellXY(self, x: int, y: int) -> ICell:
        return self.__cells[y][x]

    @property
    def Width(self) -> int:
        return self.__width

    @property
    def Height(self) -> int:
        return self.__height

    def live(self) -> None:
        for y in range(self.__height):
            for x in range(self.__width):
                self.__cells[y][x].live()
