from abc import ABC, abstractmethod

from contract.iObserver import IObserver
from contract.iactionperformer import IActionPerformer
from contract.imodel import IModel


class IView(IObserver, ABC):
    @abstractmethod
    def display(self) -> None:
        ...

    @property
    def ActionPerformer(self) -> IActionPerformer:
        ...

    @ActionPerformer.setter
    def ActionPerformer(self, actionPerformer: IActionPerformer) -> None:
        ...

    @property
    def Model(self) -> IModel:
        ...

    @Model.setter
    def Model(self, model: IModel) -> None:
        ...
