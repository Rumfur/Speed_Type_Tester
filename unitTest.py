import os
import certifi
import pymongo
from random_word import RandomWords
from configparser import ConfigParser

print("Starting unit test")
print("----------------------------------------")

print("Checking if config file exists -->")
assert os.path.isfile("config.txt") == True
print("OK")
print("----------")

config = ConfigParser()
config.read("config.txt") # Opens the config file

print("Checking if programm receaves words from RandomWords API -->")
r = RandomWords()
words = r.get_random_words(hasDictionaryDef="true", limit=5)
assert (len(words) > 0) == True
print("OK")
print("----------")

print("Checking if config file has mongo database values -->")
assert config.has_option("MONGODB", "username") == True
assert config.has_option("MONGODB", "password") == True
assert config.has_option("MONGODB", "cluster") == True
assert config.has_option("MONGODB", "database") == True
print("OK")
print("----------")

print("Checking if it is possible to connect to Mongo database with the config values -->")
ca = certifi.where()
user = config.get("MONGODB", "username")
password = config.get("MONGODB", "password")
cluster = config.get("MONGODB", "cluster")
database = config.get("MONGODB", "dataBase")
connection = pymongo.MongoClient(f"mongodb+srv://{user}:{password}@{cluster}.jk8qi.mongodb.net/{database}?retryWrites=true&w=majority", tlsCAFile=ca)
serverData = connection.admin.command("ismaster")
assert serverData["ismaster"] == True
print("OK")
print("----------")

print("Checking if log file exists -->")
assert os.path.isfile("logFile.log") == True
print("OK")
print("----------")

print("Test complete -> Everything is OK")
print("----------------------------------------")