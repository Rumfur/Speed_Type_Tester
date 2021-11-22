from os import system
import sqlite3
import certifi
import pymongo
from logger import *
from configMaker import *

logger = get_logger(__name__)

checkConfig()

# local database
conn = sqlite3.connect("speedTypeDB.db")
cur = conn.cursor()

def createLocalDBTables():
    try:
        cur.execute("CREATE TABLE results (NR INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, username TEXT NOT NULL, typeSpeed DOUBLE, mistakes INTEGER)")
        logger.info("Created \"results\" table")
    except:
        logger.info("\"results\" table allready created")

def addDataLocalDB(Username, typeSpeed, mistakes):
    try:
        cur.execute(
            "INSERT INTO results (Username, typeSpeed, mistakes) VALUES (?, ?, ?)", (Username, typeSpeed, mistakes))
        conn.commit()
        logger.info("Data was successfully added to a local database")
    except:
        cur.execute('DELETE FROM results')
        logger.info("Failed to add data to a local database")

# online database

config = readConfig()
ca = certifi.where()
user = config["username"]
password = config["password"]
cluster = config["cluster"]
database = config["database"]
ca = certifi.where()
myclient = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{cluster}.jk8qi.mongodb.net/{database}?retryWrites=true&w=majority", tlsCAFile=ca)
mydb = myclient[config["database"]]
mycol = mydb[config["database"]]

def addDataPymongo(Username, typeSpeed, mistakes):
    mydict = {"Username": Username, "typeSpeed": typeSpeed, "mistakes": mistakes}
    try:
        x = mycol.insert_one(mydict)
        logger.info("Data was successfully added to Pymongo")
    except:
        print("Couldnt add data to Pymongo")
        logger.critical("Data was not added to Pymongo")
        logger.exception("")

def getPymongoData():
    data = mycol.find({})
    logger.info("Data was successfully read from Pymongo")
    return data

def readPymongoData():
    data = getPymongoData()
    for i in data:
        print(i)

def MigrateData():
    cur.execute('DELETE FROM results')
    data = getPymongoData()
    for i in data:
        addDataLocalDB(i.get("Username"), i.get("typeSpeed"), i.get("mistakes"))
    logger.info("Data was successfully migrated to local database")