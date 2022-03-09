from contract.iObserver import IObserver


class Observable:
    __observers: [IObserver]

    def __init__(self):
        self.__observers = []

    def register(self, observer: IObserver) -> None:
        self.__observers.append(observer)

    def unregister(self, observer: IObserver) -> None:
        self.__observers.remove(observer)

    def _notify(self) -> None:
        for observer in self.__observers:
            observer.update(self)
