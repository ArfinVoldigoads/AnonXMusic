import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("29537688"))
API_HASH = getenv("7e3c3b76aba0a6403026f1c93ef30c95")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("6958177303:AAE-Sbu6LUy0dyCZ5UtGfj1h0pbjar3zT9Y")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://memek:memek@cluster0.xktxnyr.mongodb.net/?retryWrites=true&w=majority", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002109156275", None))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv("6649432492", 6649432492))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/Itz-Jaan/AnonXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/arfinmaou")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/gcanimecommunity")

# Setel ini ke True jika Anda ingin asisten meninggalkan obrolan secara otomatis setelah jeda tertentu
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", True))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("BQDNvmIAsys5NXzikbCNbMHtXa2RirBBdy-mf2YQ1PJCi8h_LZU2UXAN0qt1N0NLMMRaiBzfnZDQGnEp_-axW4N9lFsIt635Ij6-4S8d3QJwfoy56TAkOBSr86vljWTxSZlG0XTkFd8FfgnNSbotdBBzbBCAt1jELCersFMkQyOaSiPMGFG0fevEWk8EqIGRDbRE9z2urxiLB-T_pM7elJA9GnFuydqiv7bFVR502nsomgsOOcAj3qANtpQgeF7xrrgGMgCgUYrZj0bkHc0h_YKEG8SPlZDorjJXyQIHpAWzhi0a1-j5b3SSP-IZHHxcUb6Flh8ACM6VbPFYjJ-DD9HYP1ZkFQAAAAGgl2UkAA", None)
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
    "START_IMG_URL", "https://telegra.ph/file/15ac171ea63db8e6b5032.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/c48c37518c166b969c9f1.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/524ec2eb84a875f5f920d.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1f66979eed0cbcbb3f792.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/02b6b52c5664a5891ad2e.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/7919e9f963181debaa8cd.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/c88fa8872d6fc749bf555.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/02b6b52c5664a5891ad2e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/524ec2eb84a875f5f920d.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/524ec2eb84a875f5f920d.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/d86085b284af6bb06c3cd.jpg"


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
