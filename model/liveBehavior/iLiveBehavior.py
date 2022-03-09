from abc import ABC, abstractmethod


class ILiveBehavior(ABC):
    @abstractmethod
    def live(self, cell) -> None:
        ...
