import os
import logging
from datetime import datetime


FILE_DIR = 'logs'
FILE_DIR = os.path.join(os.getcwd(),FILE_DIR)

os.makedirs(FILE_DIR,exist_ok=True)

CURRENT_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
FILE_DIR_NAME = f"log_{CURRENT_TIME}.log"

FILE_PATH = os.path.join(FILE_DIR,FILE_DIR_NAME)

logging.basicConfig(
    filename=FILE_PATH,
    filemode='w',
    format='[%(asctime)s] - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)