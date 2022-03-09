from __future__ import annotations
from abc import ABC, abstractmethod
from contract.igrid import IGrid
from contract.observable import Observable


class IModel(ABC, Observable):
    def __init__(self):
        Observable.__init__(self)

    @property
    def Grid(self) -> IGrid:
        ...

    @abstractmethod
    def getConfiguration(self, key: str) -> int | str:
        ...

    @abstractmethod
    def live(self) -> None:
        ...
