from math import ceil

from sharpy.plans.acts import GridBuilding
from sc2 import UnitTypeId


class AutoBarracks(GridBuilding):
    """Builds barracks automatically when needed based on left over minerals or command centre count."""

    def __init__(self):
        super().__init__(UnitTypeId.BARRACKS, 0)

    async def execute(self):
        self.to_count = await self.barracks_count_calc()
        return await super().execute()

    async def barracks_count_calc(self) -> int:
        townhall_count = self.cache.own(
            {UnitTypeId.COMMANDCENTER, UnitTypeId.PLANETARYFORTRESS, UnitTypeId.ORBITALCOMMAND}
        ).amount
        barracks_count = self.cache.own(
            {UnitTypeId.BARRACKS, UnitTypeId.BARRACKSREACTOR, UnitTypeId.BARRACKSTECHREACTOR}).amount
        mineral_count = self.ai.minerals

        if mineral_count >= 400:
            self.print(f"Minerals too high, requesting barracks {mineral_count}")
            return barracks_count + 2
        elif barracks_count < townhall_count * 3:
            return barracks_count + 1
        else:
            return barracks_count
