import pymongo

def getDb():
    myclient = pymongo.MongoClient("mongodb+srv://user1:user1@cluster0.njygwxb.mongodb.net/?retryWrites=true&w=majority")
    mydb = myclient["mydatabase"]
    mycol = mydb["history"]    
    return mycol