from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = 'mongodb://localhost:27017/'

server_api = ServerApi('1')
client = MongoClient(uri,server_api = server_api)

try:
    # The ping command is cheap and does not require auth.
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
db = client.crud_pyp
collection = db["todo_data"]