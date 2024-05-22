
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://admin:1234@igor--dev-2024.3bvgbxa.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

db = client.myProdutos
produtosCollection = db['produtos']


# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)