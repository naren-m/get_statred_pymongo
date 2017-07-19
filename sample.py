# Sample usage of mongo client
# Reference http://api.mongodb.com/python/current/tutorial.html

from pymongo import MongoClient
import datetime
import pprint

def getMongoClient():
    return MongoClient('localhost', 27017)

def getDatabase(client, dbName):
    return client[dbName]

def getCollection(db, collectionName):
    collection = db[collectionName]
    return collection

def getCollectionNamesFromDB(db):
    return db.collection_names(include_system_collections=False)

def insertOneDocToCollection(collection, doc):
    return collection.insert_one(doc)

def insertManyDocsToCollection(collection, docs):
    return collection.insert_many(docs)

def findDocs(collection, whereCondition):
    return collection.find(whereCondition)

def main():
    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
            
    new_posts = [{"author": "Mike",
                "text": "Another post!",
                "tags": ["bulk", "insert"],
                "date": datetime.datetime(2009, 11, 12, 11, 14)},
                {"author": "Eliot",
                "title": "MongoDB is fun",
                "text": "and pretty easy too!",
                "date": datetime.datetime(2009, 11, 10, 10, 45)}]


    client = getMongoClient()

    db = getDatabase(client, "TestDB")

    collection = getCollection(db, "POSTS")

    print getCollectionNamesFromDB(db)

    insertOneDocToCollection(collection, post)

    insertManyDocsToCollection(collection, new_posts)

    for post in collection.find():
        pprint.pprint(post)

    # Count of all posts
    print "Count of all posts", collection.count()

    # Count of posts by Mike
    whereCondition = {"author": "Mike"}   
    print "Count of posts by Mike", findDocs(collection, whereCondition).count()

    # Range Queries 
    d = datetime.datetime(2009, 11, 12, 12)
    whereCondition = {"date": {"$lt": d}}
    for post in findDocs(collection, whereCondition).sort("author"):
        pprint.pprint(post)

    client.close()

if __name__ == '__main__':
    main()
