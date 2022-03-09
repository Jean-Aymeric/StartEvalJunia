from abc import abstractmethod, ABC


class IObserver(ABC):
    @abstractmethod
    def update(self, subject) -> None:
        ...
