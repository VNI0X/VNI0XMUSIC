from VNI0XMUSIC.core.bot import Hotty
from VNI0XMUSIC.core.dir import dirr
from VNI0XMUSIC.core.git import git
from VNI0XMUSIC.core.userbot import Userbot
from VNI0XMUSIC.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "NOBITA_SONG_BOT"  # connect music api key "Dont change it"
