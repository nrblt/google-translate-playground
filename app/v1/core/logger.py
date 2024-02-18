import logging
import os
from datetime import datetime

class DateFileHandler(logging.FileHandler):
    def __init__(self, filename, mode='a', encoding=None, delay=False):
        today = datetime.now().strftime("%Y-%m-%d")
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        self.filename = os.path.join(os.path.dirname(filename), f"{today}.log")
        logging.FileHandler.__init__(self, self.filename, mode, encoding, delay)

def setup_logger():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    file_handler = DateFileHandler('logs/')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    logger = logging.getLogger('')
    logger.addHandler(file_handler)

setup_logger()
