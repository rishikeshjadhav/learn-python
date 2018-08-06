import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
# Create and configure logger
logging.basicConfig(filename="D:\\Projects\\Learnings\\POC\\Python\\06_logs.log",
                    level=logging.DEBUG, format=LOG_FORMAT)
logger = logging.getLogger()

logger.info("Hello world in logging")

print(logger.level)
