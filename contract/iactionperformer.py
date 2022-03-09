from abc import ABC, abstractmethod
from contract.order import Order


class IActionPerformer(ABC):
    @abstractmethod
    def performOrder(self, order: Order) -> None:
        ...
