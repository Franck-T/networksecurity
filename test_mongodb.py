
from pymongo.mongo_client import MongoClient
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

load_dotenv()

MONGODB_ADMIN_USER = os.getenv("MONGODB_ADMIN_USER")
MONGODB_ADMIN_PASSWORD = os.getenv("MONGODB_ADMIN_PASSWORD")

username = quote_plus(str(MONGODB_ADMIN_USER))     # Encodes special chars safely
password = quote_plus(str(MONGODB_ADMIN_PASSWORD)) # Encodes special chars safely

MONGODB_URI=f"mongodb+srv://{username}:{password}@mongo-db-cluster.gnr2zgp.mongodb.net/?appName=mongo-db-cluster"

#print("Username:", username)
#print("Password:", password)
#print("MONGODB_URI:", MONGODB_URI)

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)