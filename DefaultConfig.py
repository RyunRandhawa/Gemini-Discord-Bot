import configparser

config = configparser.ConfigParser()
config.read('config.ini')

DISCORD_OWNER_ID = config['DEFAULT']['discord_owner_id']
DISCORD_TOKEN = config['DEFAULT']['discord_token']
GEMINI_SDK = config['DEFAULT']['gemini_sdk']