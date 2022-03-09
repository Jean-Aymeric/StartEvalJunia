from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class SwapLive(ILiveBehavior):
    def live(self, cell: ICell) -> None:
        cell.State = not cell.State
