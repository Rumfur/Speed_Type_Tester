from os.path import exists
import logging
import sqlite3

conn = sqlite3.connect('speedTypeDB.db')
curs = conn.cursor()
#cur.execute('DROP TABLE IF EXISTS email')


logger = logging.getLogger(logging.basicConfig(filename='logFile.log', encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))

def writeConfig(): # Writes config file lines
    file = open("config.txt", "a")
    file.write("Testing writing!\n")
    file.write("I wonder what i'll write here.")
    file.close()

def checkConfig():
    if not(exists("config.txt")):
        file = open("config.txt","x") # Makes config file, if doesn't exist
        writeConfig()

def readConfig():
    file = open("config.txt", "r") # Reads config file
    return file.read()

checkConfig()
logger.info(readConfig())
print("Hello world")
