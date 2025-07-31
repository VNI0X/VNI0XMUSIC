import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 1500))

LOGGER_ID = int(getenv("LOGGER_ID", None))

OWNER_ID = int(getenv("OWNER_ID", 7417167870))

MUSIC_BOT_NAME = int(getenv("SANATAN DHARM MUSIC"))

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv("https://github.com/VNI0X/VNI0XMUSIC")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "Master")
GIT_TOKEN = getenv("GIT_TOKEN")

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/HEROKU_CLUB")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "6be9f0b34c384ad097cc71b1c1fc5e8b")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "2607415f99944cc6b24fa98018fb8c09")

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))

#_________________________[ YouTube API setup ]_________________________
BASE_API_URL = getenv("BASE_API_URL", "https://pro.spotifytech.shop")
BASE_API_KEY = getenv("BASE_API_KEY", "8de65623506d05c51fcf90ee3e97102f")
#________________________________________________________________________

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/1557a544d9b4f051f99c7-57891fa1d7578f5b79.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/uwstab.jpg"
)
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


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
