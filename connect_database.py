from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import os
from dotenv import load_dotenv

load_dotenv() 


cassandra_username = os.getenv("CASSANDRA_USERNAME")
cassandra_password = os.getenv("CASSANDRA_PASSWORD")


cloud_config= {
  'secure_connect_bundle': 'secure-connect-task2.zip',
  'keyspace' : 'learn'
}
auth_provider = PlainTextAuthProvider(cassandra_username, cassandra_password)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")