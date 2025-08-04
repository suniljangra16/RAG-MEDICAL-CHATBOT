import logging
import os
from datetime import datetime

LOGS='logs'
os.makedirs(LOGS,exist_ok=True)


LOG_FILE=os.path.join(LOGS,f"log_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s -%(message)s',
    filename=LOG_FILE

)

def get_logger(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    return logger