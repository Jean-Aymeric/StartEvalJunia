from abc import ABC, abstractmethod
from contract.icell import ICell


class IGrid(ABC):
    @abstractmethod
    def cellXY(self, x: int, y: int) -> ICell:
        ...

    @property
    def Width(self) -> int:
        ...

    @property
    def Height(self) -> int:
        ...
