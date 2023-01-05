import tinder_cli as tc
import json
import pandas as pdfrom 
import bson
import time
from pymongo import MongoClient                
import requests as r
import os
import subprocess as s
import random as ran
import pandas as pd
import pprint

class TinderDroid:
    def __init__(self, myToken=None):
        self.myToken= myToken
        self.defaulPath = os.getcwd()
        self.db_client = MongoClient("localhost", 27017)
        self.db = self.db_client.get_database("TINDER_DROID")

#DATABASE METHODS

    def getCol(self,collName="USER_DATA"):
        collection = self.db.get_collection(collName)
        return collection
    
    def addData(self, data=None, collection=None):
        collection.insert_one(data)
        print("Data inserted successfully")

    def getData(self,collName="USER_DATA"):
        collection = self.getCol(collName)
        userData = []
        rawList = collection.find()
        userData = [dict(user) for user in rawList]
        for x in userData:
            self.displayData(x)

    def displayData(self,dataDict=None, indent=0):
        for key, value in dataDict.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                self.displayData(value, indent+1)
            else:
                print('\t' * (indent+1) + str(value))
        print("=======================================================================================================================================")    




                
                

            
#WEB METHODS
    def getClient(self):
        client = tc.TinderCLI().client
        return client

    def getSession(self):
        client = self.getClient()
        token = self.myToken
        session = client.get_session(token)
        return session

    def getUserData(self):
        session = self.getSession()
        client = self.getClient()
        users = client.get_recommendations(session)
        recon_dict = json.loads(users.content)
        meta = recon_dict["meta"]
        userData = list(recon_dict["data"]["results"])        
        return userData

    def start(self):
        action = input("""
TINDER DROID STARTED
=======================================================================================================================================
Choose the desired action:
1 - STORE 
2 - LIKE
3 - SAVE
4 - LOAD
                """)
        if action =="1":
            self.storeUserData()
        elif action =="2":
            self.likeUserData()
        elif action =="3":
            self.saveUserPhotos()
        elif action == "4":
            self.getData()
        

    def storeUserData(self, uploads = 0):        
        userData= self.getUserData()
        collection = self.getCol("USER_DATA_MALE")
        print("Total number of recomendations loaded: {} \n".format(len(userData)))
        for x, y in enumerate(userData):
            print("Uploading user{}".format(x))
            self.addData(y, collection)
        total = uploads + len(userData)
        print(f"Total number of records uploaded: {total}")
        time.sleep(1)
        self.storeUserData(uploads=total)



    def likeUserData(self, likes=0):
        userData= self.getUserData()
        collection = self.getCol("USER_DATA")
        client = self.getClient()
        session = self.getSession()
        print("=================================================================")
        print(f"Total number of loaded profiles: {len(userData)}")
        for x in userData:
            self.addData(x, collection=collection)
            data = x["user"]
            id = data["_id"]
            client.like_user(session,id)
            print(f"Profile id {id} liked")
        print("Total likes: {}".format(len(userData)))
        print("=================================================================")
        time.sleep(1)
        self.likeUserData(likes=len(userData))

        



    def likeStorage(self):
        client = self.getClient()
        session = self.getSession()
        collection = self.getCol("USER_DATA")
        userData = []
        rawList = collection.find()
        userData = [dict(user) for user in rawList]
        liked = 1
        print("=================================================================")
        print(f"Total number of loaded profiles: {len(userData)}")
        for x in userData:
            data = x["user"]
            id = data["_id"]
            client.like_user(session,id)
            liked += 1  
            progress = float(float(liked)/len(userData))
            print("Profile id {} liked------Progress {}/{}".format(id, liked,len(userData)))
        print("Total likes: {}".format(len(userData)))
        print("=================================================================")
        
        


    def saveUserPhotos(self, profiles=0, photos= 0):
        
        userData= self.getUserData()
        profiles += len(userData)
        client = self.getClient()
        session = self.getSession()
        print("=================================================================")
        print(f"Total number of loaded profiles: {len(userData)}")
        for x in userData:
            data = x["user"]
            imgs = data["photos"]
            photos += len(imgs)
            for x in imgs:
                img_url=(x["url"])
                self.savePhoto(url=img_url)
            
        print("Total files saved: {}".format(photos))
        print("=================================================================")
        time.sleep(3)
        self.saveUserPhotos(profiles=profiles, photos=photos)

    def savePhoto(self, url=None):
        response = r.get(url)
        numbers = [x for x in range(100000)]
        dir = os.getcwd()
        file_name = dir + "/photos/" +str(ran.sample(numbers,1))+".jpg"
        file = open(file_name, "wb")
        file.write(response.content)
        file.close()
            


        
tinder_token = "c2854327-400c-4273-a735-433f3295da57"
td = TinderDroid(myToken=tinder_token)
td.likeUserData()
