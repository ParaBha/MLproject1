'''Logging is a means of tracking events that happen when some software runs.'''
import logging
import os
from datetime import datetime
#Generates a log file name with the current date & time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
#os.getcwd() → Gets the current working directory.
#"logs" → Subfolder for logs.
#LOG_FILE → Adds the file name to the path.
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
#os.makedirs → Creates the directory (and parents if needed).
#exist_ok=True → Avoids error if the folder already exists.
os.makedirs(logs_path,exist_ok=True)

#Properly constructs the file path to the log file.
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format= "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO

)


