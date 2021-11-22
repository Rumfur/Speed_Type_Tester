from os.path import exists
from logger import get_logger

logger = get_logger(__name__)

def writeConfig(): # Writes config file lines
    file = open("config.txt", "a")
    file.write("[MONGODB\nusername: Pukitis\npassword: Student007\ncluster: speedtypecluster\ndatabase: SpeedTypeCluster]")
    file.close()

def checkConfig():
    if not(exists("config.txt")):
        file = open("config.txt","x") # Makes config file, if doesn't exist
        writeConfig()

def readConfig():
    data = {}
    try:
        file = open("config.txt", "r") # Reads config file
    except:
        print("Config file not found!")
        logger.critical("Config file not found!")
    try:
        for line in file:
            if line == "[MONGODB]\n":
                continue
            values = line.split("=")
            data[values[0].strip()] = values[1].strip()
        logger.info("Config file read successfully")
        return data
    except:
        print("Problem reading file lines")
