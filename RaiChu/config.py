## Coder are here

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "BQA8qEh0nyCCLjjYZs2GYVG4OQ8KHryavX1N1d_K_pfI7crsBFdlK-ia2j2DG5I54Q1T-NMj9Q1y7YLpO9kt5a7gKCqM8lgo6480xjBPTEFPt8KNxgoRnWxQMbemeAXU6oE-UDst_FhKDuHOJWShIWco5k2E2OUIjXQMsiNjk9n5hLiEur5jJ97RHIhOZ7x8pZv4jCPVhHBb_wKh7uxtHoqoQgEkDtDCZg6d35fLBxlIZslANaHW1uysPzj-Ps9NwxEipNFP46CnJLs6BzUg4nZlTvRbsjuVuEqoBauxEYd_ZZZ6ctfMuxStrXdPFOkZUidShCIBOY2nuM89dF5MRhsMAAAAAVzBZK8A")
BOT_TOKEN = getenv("BOT_TOKEN"5636376647:AAGonbe_4imQIiAahoZCif1XW5xYZ2-BL_c" )
BOT_NAME = getenv("BOT_NAME"Harahmahi_musicbot" )
API_ID = int(getenv("API_ID", "24782565"))
API_HASH = getenv("API_HASH", "cc4dff9c4deb8b1432cb59194124ddcb")
OWNER_NAME = getenv("OWNER_NAME", "harsh xd")
ALIVE_NAME = getenv("ALIVE_NAME", "Null")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "Harsh")
BOT_USERNAME = getenv("BOT_USERNAME"@Harahmahi_musicbot" )
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "null")
GROUP_SUPPORT = getenv(("GROUP_SUPPORT", "alone_support")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","alone_support")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/AMANTYA1/RaiChu-MusicV2")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2310d5bdf25ea3b3ae4d1.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/2310d5bdf25ea3b3ae4d1.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/2310d5bdf25ea3b3ae4d1.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/2310d5bdf25ea3b3ae4d1.jpg")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/d8f8fc1de9110b93ca94c.jpg")
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://telegra.ph/file/58da23d726b601dc3b18e.jpg")
