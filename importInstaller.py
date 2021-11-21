import logger
import pip
logger = logger.get_logger(__name__)

# Installs packages required for the programm

def installImports():
    packages = ["pymongo", "random-word", "sqlite3", "certifi"]
    for package in packages:
        try:
            logger.info("Installing " + package + " package")
            __import__(package)
            logger.info(package + " Is already installed")
        except ImportError:
            pip.main(['install', package])
            logger.info(package + " Is installed successfully")