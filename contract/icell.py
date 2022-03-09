from abc import ABC, abstractmethod
from model.liveBehavior.iLiveBehavior import ILiveBehavior


class ICell(ABC):
    @abstractmethod
    def __init__(self, liveBehavior: ILiveBehavior):
        ...

    @property
    def State(self) -> bool:
        ...

    @State.setter
    def State(self, state: bool) -> None:
        ...
