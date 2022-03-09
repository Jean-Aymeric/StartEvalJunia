import random
from model.liveBehavior.iLiveBehavior import ILiveBehavior
from contract.icell import ICell


class RandomLive(ILiveBehavior):
    def live(self, cell: ICell) -> None:
        if random.randint(0, 1) == 1:
            cell.State = True
        else:
            cell.State = False
