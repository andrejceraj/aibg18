from .bots import *


class BotFactory:
    @staticmethod
    def create_bot(bot_type, player_name, player_id):
        type = bot_type.lower()
        bot = None

        # Adding new type of bots
        if type == "random":
            print("initializing random bot...")
            bot = RandomBot(player_name, player_id)
        elif type == "":
            return None

        return bot

