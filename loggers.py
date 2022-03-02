import logging

formatter = logging.Formatter(
    "[%(asctime)s] %(name)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
# set the mode to "w" to overwrite the log file each time the bot starts
file_handler = logging.FileHandler("logs/bot.log", "w", delay=True)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

logger = logging.getLogger("imarch-bot")
logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(stream_handler)
