import psycopg2
import json
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME, FILE_PATH
from functions import store_interface

#List of interface for storage
interfaces = ["Port-channel", "TenGigabitEthernet", "GigabitEthernet"]

#Works with Localhost and BDI too
#interfaces = ["Port-channel", "TenGigabitEthernet", "GigabitEthernet", "Loopback", "BDI"]

conn = psycopg2.connect(host=DB_HOST,
                        dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        port=DB_PORT)
cur = conn.cursor()

#FILE
file_path = FILE_PATH
with open(file_path, 'r') as file:
  config_data = json.load(file)

for interface in interfaces:
  store_interface(cur, config_data, interface)

conn.commit()

cur.close()
conn.close()
