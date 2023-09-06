import pymongo
def conn():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    return conn
print(conn())