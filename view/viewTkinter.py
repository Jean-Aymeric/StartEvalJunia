from contract.iview import IView
from contract.imodel import IModel
from contract.observable import Observable
from contract.iactionperformer import IActionPerformer
from contract.order import Order
import tkinter.messagebox
from typing import List


class ViewTkinter(IView):
    __model: IModel
    __window: tkinter.Tk
    __canvas: tkinter.Canvas
    __actionPerformer: IActionPerformer
    __zoom: int
    __grid: List[List[int]]

    def __init__(self):
        ...

    @property
    def ActionPerformer(self) -> IActionPerformer:
        return self.__actionPerformer

    @ActionPerformer.setter
    def ActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        self.__actionPerformer = actionPerformer

    @property
    def Model(self) -> IModel:
        return self.__model

    @Model.setter
    def Model(self, model: IModel) -> None:
        self.__model = model
        self.__model.register(self)
        self.__zoom = self.__model.getConfiguration("zoom")
        self.__createWindow()
        self.__createGrid()

    def __createWindow(self):
        self.__window = tkinter.Tk()
        self.__window.title(self.__model.getConfiguration("title"))
        self.__window.geometry(str(self.__realToWindow(self.__model.getConfiguration("width")))
                               + "x"
                               + str(self.__realToWindow(self.__model.getConfiguration("height"))))
        self.__window.protocol("WM_DELETE_WINDOW", self.__onClosing)
        self.__window.resizable(False, False)

    def __createGrid(self):
        self.__canvas = tkinter.Canvas(self.__window)
        self.__canvas.configure(bg=self.__model.getConfiguration("backgroundColor"))
        self.__canvas.pack(fill="both", expand=True)
        self.__grid = [[0] * self.__model.Grid.Width for _ in range(self.__model.Grid.Height)]
        for y in range(self.__model.Grid.Height):
            for x in range(self.__model.Grid.Width):
                cellColor = self.__model.getConfiguration("deadColor")
                if self.__model.Grid.cellXY(x, y).State:
                    cellColor = self.__model.getConfiguration("livingColor")
                self.__grid[y][x] = self.__canvas.create_rectangle(self.__realToWindow(x),
                                                                   self.__realToWindow(y),
                                                                   self.__realToWindow(x) + self.__zoom,
                                                                   self.__realToWindow(y) + self.__zoom,
                                                                   fill=cellColor,
                                                                   outline=self.__model.getConfiguration("deadColor"))

    def display(self) -> None:
        self.__window.deiconify()
        self.__window.update()

    def __onClosing(self):
        self.__window.destroy()
        self.__actionPerformer.performOrder(Order.QUIT)

    def __realToWindow(self, coordinate: int) -> int:
        return coordinate * self.__zoom

    def __windowToReal(self, coordinate: int) -> int:
        return int(coordinate / self.__zoom)

    def update(self, subject: Observable) -> None:
        for y in range(self.__model.Grid.Height):
            for x in range(self.__model.Grid.Width):
                cellColor = self.__model.getConfiguration("deadColor")
                if self.__model.Grid.cellXY(x, y).State:
                    cellColor = self.__model.getConfiguration("livingColor")
                self.__canvas.itemconfig(self.__grid[y][x], fill=cellColor)
        self.__window.update()
