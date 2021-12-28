import os
from configs import Config
from PhixyBot.helpers.database.database import Database

db = Database(Config.MONGODB_URI, Config.BOT_USERNAME)
