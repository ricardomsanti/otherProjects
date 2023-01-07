from pymongo import MongoClient                


class TinderDb:

    def __init__(self):
        self.db_client = MongoClient("localhost", 27017)
        self.db = self.db_client.get_database("TINDER_DROID")

#DATABASE METHODS


    def getCol(self,colleciton=None):
        collection = self.db.get_collection(collection)
        return collection
    
    def addData(self, data=None, collection=None):
        collection.insert_one(data)
        print("Data inserted successfully")

    def uploadUserData(self, uploads = 0):        
            client = tc.TinderCLI().client
            session = client.get_session(self.myToken)
            recon = client.get_recommendations(session)
            recon_dict = json.loads(recon.content)
            meta = recon_dict["meta"]
            dataDict = list(recon_dict["data"]["results"])        
            print("Total number of recomendations loaded: {} \n".format(len(dataDict)))
            for x, y in enumerate(dataDict):
                print("Uploading user{}".format(x))
                addData(y)
            total = uploads + len(dataDict)
            print(f"Total number of records uploaded: {total}")
            time.sleep(10)
            uploadUserData(myToken=myToken, uploads=total)

