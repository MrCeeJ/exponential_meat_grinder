import os
import sub_module  # Important, do not remove!

from bot.exponential_meat_grinder import ExponentialMeatGrinder
from sc2 import Race
from sc2.player import Bot

from bot_loader import GameStarter, BotDefinitions
from version import update_version_txt


def add_definitions(definitions: BotDefinitions):
    # definitions.add_bot(
    #     "protossbot", lambda params: Bot(Race.Protoss, ProtossBot(BotDefinitions.index_check(params, 0, "default"))), None
    # )
    definitions.add_bot(
        "terranbot", lambda params: Bot(Race.Terran, ExponentialMeatGrinder("2")), None
    )
    # definitions.add_bot(
    #     "zergbot", lambda params: Bot(Race.Zerg, ZergBot()),
    #     None
    # )


def main():
    update_version_txt()
    root_dir = os.path.dirname(os.path.abspath(__file__))
    ladder_bots_path = os.path.join("Bots")
    ladder_bots_path = os.path.join(root_dir, ladder_bots_path)
    definitions: BotDefinitions = BotDefinitions(ladder_bots_path)
    add_definitions(definitions)
    starter = GameStarter(definitions)
    starter.play()


if __name__ == "__main__":
    main()
