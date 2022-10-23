import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("18641113"))
API_HASH = getenv("bc5fea81e7bf9f3c0784a0a7d35f9c71")
BOT_USERNAME = getenv("Darlzzzmusic_bot")
ARQ_API_KEY = getenv("XQBIJV-QGSIOH-ROVLWH-PWARNF-ARQ")
BOT_TOKEN = getenv("5673232199:AAFDwlz2T7U22NONiyJWKOBNuWgKaC_xnLY")
DURATION_LIMIT = int(getenv("DURATION_LIMIT"))
SESSION_NAME = getenv("AQCRbpMZRCun02ZdJ6j8wQ4pkOMy8P5mBYxiJEavLlWjgDsQljShUh94PHzCMtNMk7WtfRmqq9UVee8p2c8TNOcYu3No4UAynYEBS1fE2nRfo60-PMVEI6MB_X3CUNOQ4KkkdOje2tx2cdGUNFMiomERDrwSDolOiljbHrfSutRHpSjLacXl3m7HlUOFeCa-uMSuhLJ8-kX5_VVjHBhnsDZSCyT7duS0YZRAfnO2Ikq6KCx0bmHXWZXyEQKRRJRdOWkQU08XJwB6Ny-PfLmHd8K4U8vB2keU9CpPFWT_i7vlVMFlWn1ROROK9kT_P_4Bcs1smaDKK55oCdHJGVVtU0r_AAAAAU7LTEIA", "session")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("5323266323").split()))
aiohttpsession = aiohttp.ClientSession()
