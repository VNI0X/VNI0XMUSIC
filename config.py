import re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Required Configuration
API_ID = int(getenv("API_ID", 0))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
MONGO_DB_URI = getenv("MONGO_DB_URI", "")
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1500))
LOGGER_ID = int(getenv("LOGGER_ID", 0))
OWNER_ID = int(getenv("OWNER_ID", 0))

# String - Not Integer
MUSIC_BOT_NAME = getenv("SANATAN_DHARM_MUSIC", "Sanatan Music Bot")

# Heroku Settings
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = getenv("HEROKU_API_KEY", "")

# Git Settings
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/VNI0X/VNI0XMUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", "")

# Support URLs
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HEROKU_CLUB")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

# Boolean flag
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "True").lower() == "true"

# Spotify
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "")

# File size limits
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

# YouTube API
BASE_API_URL = getenv("BASE_API_URL", "https://pro.spotifytech.shop")
BASE_API_KEY = getenv("BASE_API_KEY", "")

# Pyrogram Sessions
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", "")
STRING3 = getenv("STRING_SESSION3", "")
STRING4 = getenv("STRING_SESSION4", "")
STRING5 = getenv("STRING_SESSION5", "")

# Others
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

# Image URLs
START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/1557a544d9b4f051f99c7-57891fa1d7578f5b79.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://files.catbox.moe/uwstab.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"
STATS_IMG_URL = "https://files.catbox.moe/uwstab.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/7ut9uj.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/7ut9uj.jpg"
STREAM_IMG_URL = "https://envs.sh/SnH.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/7ut9uj.jpg"

# Time conversion
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# URL Validation
if SUPPORT_CHANNEL and not re.match(r"^(?:http|https)://", SUPPORT_CHANNEL):
    raise SystemExit("[ERROR] - Your SUPPORT_CHANNEL url is wrong. Must start with https://")

if SUPPORT_CHAT and not re.match(r"^(?:http|https)://", SUPPORT_CHAT):
    raise SystemExit("[ERROR] - Your SUPPORT_CHAT url is wrong. Must start with https://")
