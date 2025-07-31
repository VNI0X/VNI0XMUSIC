import os
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters  

load_dotenv()

BANNED_USERS = filters.user()



# Get this value from my.telegram.org/apps
API_ID = int(os.getenv("API_ID", 0))
API_HASH = os.getenv("API_HASH", "")

# Get your token from @BotFather on Telegram
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
MUSIC_BOT_NAME = os.getenv("MUSIC_BOT_NAME", "")
PRIVATE_BOT_MODE = os.getenv("PRIVATE_BOT_MODE", "False")

# Duration limit
DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", "900"))

# Chat ID of a group for logging bot's activities
LOGGER_ID = int(os.getenv("LOGGER_ID", "0"))

# Get this value from @MissRose_Bot by using /id
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Heroku
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME", "")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY", "")

# GitHub
UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/VNI0X/VNI0XMUSIC")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", "")

# Optional API config
BASE_API_KEY = os.getenv("BASE_API_KEY", "your-api-key")
BASE_API_URL = os.getenv("BASE_API_URL", "https://your-api-url.com")

# Support
SUPPORT_CHANNEL = os.getenv("SUPPORT_CHANNEL", "https://t.me/HEROKU_CLUB")
SUPPORT_CHAT = os.getenv("SUPPORT_CHAT", "https://t.me/NOBITA_SUPPORT")

# Auto leaving settings
AUTO_LEAVING_ASSISTANT = os.getenv("AUTO_LEAVING_ASSISTANT", "False").lower() == "true"

# Auto Gcast (Broadcast)
AUTO_GCAST = os.getenv("AUTO_GCAST", "False").lower() == "true"
AUTO_GCAST_MSG = os.getenv("AUTO_GCAST_MSG", "")

# Spotify credentials
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")

# Playlist limits
SERVER_PLAYLIST_LIMIT = int(os.getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", "25"))

# Song duration download limit (in seconds)
SONG_DOWNLOAD_DURATION = int(os.getenv("SONG_DOWNLOAD_DURATION", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(os.getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# File size limits (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))  # 100MB
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))  # 1GB

# String sessions
STRING1 = os.getenv("STRING_SESSION", None)
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# Internal variables (do not touch)
BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}



START_IMG_URL = getenv(
    "START_IMG_URL", "https://files.catbox.moe/fw3g7v.webp"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://files.catbox.moe/bd8iwy.webp"
)
PLAYLIST_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
STATS_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ndak2c.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/cvbagx.jpeg"
STREAM_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/cvbagx.jpeg"


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
