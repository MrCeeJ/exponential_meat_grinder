from math import ceil

from sharpy.plans.acts import Expand
from sc2 import UnitTypeId


class AutoExpand(Expand):
    """Builds bases automatically when needed based on current worker count."""

    def __init__(self):
        super().__init__(0)

    async def execute(self):
        self.to_count = await self.base_count_calc()
        return await super().execute()

    async def base_count_calc(self) -> int:
        worker_count = self.cache.own(UnitTypeId.SCV).amount
        if worker_count < 16:
            return 1
        elif worker_count < 30:
            return 2
        elif worker_count < 40:
            return 3
        elif worker_count < 50:
            return 4
        else:
            return ceil(worker_count / 15)
