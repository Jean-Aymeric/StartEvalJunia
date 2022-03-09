import random

from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class Cell(ICell):
    __state: bool
    __liveBehavior: ILiveBehavior

    def __init__(self, liveBehavior: ILiveBehavior):
        self.__liveBehavior = liveBehavior
        if random.randint(0, 1) == 1:
            self.__state = True
        else:
            self.__state = False

    @property
    def State(self) -> bool:
        return self.__state

    @State.setter
    def State(self, state: bool) -> None:
        self.__state = state

    def live(self) -> None:
        self.__liveBehavior.live(self)
