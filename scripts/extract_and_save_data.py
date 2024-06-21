import requests
import urllib.parse

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

from configs_db import *

def  connect_mongo(uri):
    parse_password = urllib.parse.quote(PASSWORD_MONGODB)
    # # Create a new client and connect to the server
    client = MongoClient(uri, server_api=ServerApi('1'))

    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
    return client
    

def create_connect_db(client, db_name):
    db = client[db_name]
    return db


def create_connect_collection(db, col_name):
    collection = db[col_name]
    return collection

def extract_api_data(url):
    return requests.get(url).json()

def  insert_data(col, data):
    docs = col.insert_many(data)
    n_docs_inseridos = len(docs.inserted_ids)
    return n_docs_inseridos

if __name__ == "__main__":
    parse_password = urllib.parse.quote(PASSWORD_MONGODB)
    uri = f"mongodb+srv://{USERNAME_MONGODB}:{parse_password}@cluster-pipeline.jcgyaej.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-pipeline"
    client = connect_mongo(uri=uri)
    db = create_connect_db(client=client, db_name="db_produtos_teste")
    col = create_connect_collection(db=db, col_name="produtos")

    data = extract_api_data(url="https://labdados.com/produtos")
    print(f"\n Quantidade de dados extraídos: {len(data)} ")
    n_datas = insert_data(col=col, data=data)
    print(f"\n Quantidade de documentos inseridos: {n_datas} ")
    client.close()





