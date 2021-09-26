#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
from logging.handlers import RotatingFileHandler
import os
import time
from pyrogram import Client

from bot.config import Config


# TODO: is there a better way?
SESSION_NAME = ANYTHING
LOG_CHANNEL = "botlogas"
DOWNLOAD_LOCATION = Config.DOWNLOAD_LOCATION
MAX_FILE_SIZE = Config.MAX_FILE_SIZE
TG_MAX_FILE_SIZE = Config.TG_MAX_FILE_SIZE
FREE_USER_MAX_FILE_SIZE = Config.FREE_USER_MAX_FILE_SIZE
MAX_MESSAGE_LENGTH = Config.MAX_MESSAGE_LENGTH
FINISHED_PROGRESS_STR = Config.FINISHED_PROGRESS_STR
UN_FINISHED_PROGRESS_STR = Config.UN_FINISHED_PROGRESS_STR
SHOULD_USE_BUTTONS = Config.SHOULD_USE_BUTTONS
BOT_START_TIME = time.time()
LOG_FILE_ZZGEVC = Config.LOG_FILE_ZZGEVC
BOT_USERNAME = "bot_pip_pop_pup_bot"
UPDATES_CHANNEL = "botlogas"
data = []
cmd1 = [] 
crf = []
watermark = []
# senpai I am changing app string WHY???????
pid_list = []
app = Client(
        SESSION_NAME,
        bot_token="2044970438:AAHbZnDgsfv4dvSY4mQVDYDvw3fj5",
        api_id=3281305,
        api_hash="a9e62ec83fe3c22379e3e19195c8b3f6",
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
