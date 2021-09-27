#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client


# TODO: is there a better way?
AUTH_USERS = [1391975600, 1666551439]

#TG_BOT_TOKEN = "2044970438:AAHbZnDgsfv4dvSY4mQVDYDvw3fj5-Z3SWM"
TG_BOT_TOKEN = "2041120036:AAGWMuUon98HOb-moDkmodYSD2x4b_WcYyw" 
APP_ID = 3281305
API_HASH = "a9e62ec83fe3c22379e3e19195c8b3f6"
SESSION_NAME = "AHCompressorBot"
#LOG_CHANNEL = "botlogas"
LOG_CHANNEL = "fgaofdjksf"
DOWNLOAD_LOCATION = "/app/downloads"
FREE_USER_MAX_FILE_SIZE = 2097152000
MAX_MESSAGE_LENGTH = 4096
FINISHED_PROGRESS_STR = "▓"
UN_FINISHED_PROGRESS_STR = "░"
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = "Log.txt"
BOT_USERNAME = "vid_encoder_rorona_bot" 
UPDATES_CHANNEL = "botlogas"
data = []
# cmd1 = [] 
crf = []
watermark = []
# senpai I am changing app string WHY???????
pid_list = []
app = Client(
        SESSION_NAME,
        bot_token=TG_BOT_TOKEN,
        api_id=APP_ID,
        api_hash=API_HASH,
        workers=2
    )
if os.path.exists(LOG_FILE_ZZGEVC):
    with open(LOG_FILE_ZZGEVC, "r+") as f_d:
        f_d.truncate(0)

# the logging things
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(
            LOG_FILE_ZZGEVC,
            maxBytes=FREE_USER_MAX_FILE_SIZE,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)
