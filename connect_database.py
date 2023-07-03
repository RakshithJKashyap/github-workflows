from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from dotenv import load_dotenv

load_dotenv() 

cassandra_username = os.getenv("CASSANDRA_USERNAME")
cassandra_password = os.getenv("CASSANDRA_PASSWORD")

def get_session():
    cloud_config= {
                    'secure_connect_bundle': 'secure-connect-crud.zip',
                    'keyspace' : 'learn'
                }
    cassandra_username = os.getenv("CASSANDRA_USERNAME")
    cassandra_password = os.getenv("CASSANDRA_PASSWORD")
    auth_provider = PlainTextAuthProvider(cassandra_username, cassandra_password)
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    return session

