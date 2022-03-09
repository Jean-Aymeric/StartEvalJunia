from contract.imodel import IModel
from contract.iview import IView
from contract.iactionperformer import IActionPerformer
from contract.order import Order
from time import sleep


class Controller(IActionPerformer):
    __view: IView
    __model: IModel
    __running: bool

    @property
    def View(self) -> IView:
        return self.__view

    @View.setter
    def View(self, view: IView) -> None:
        self.__view = view
        view.ActionPerformer = self
        view.Model = self.__model

    @property
    def Model(self) -> IModel:
        return self.__model

    @Model.setter
    def Model(self, model: IModel) -> None:
        self.__model = model

    def start(self) -> None:
        self.__running = True
        while self.__running:
            self.__model.live()
            sleep(self.__model.getConfiguration("timeStep"))

    def performOrder(self, order: Order) -> None:
        if order == Order.QUIT:
            self.__running = False
