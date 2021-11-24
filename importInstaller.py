import os
from logger import get_logger
logger = get_logger(__name__)

# Installs packages required for the programm

def installImports():
    packages = ["pymongo", "random-word","pyyaml", "sqlite3", "certifi"]
    for package in packages:
        try:
            logger.info("Installing " + package + " package")
            __import__(package)
            logger.info(package + " Is already installed")
        except ImportError:
            os.system("python -m pip install " + package)
            logger.info(package + " Is installed successfully")