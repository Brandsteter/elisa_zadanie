#Setup file for a test interface table

import psycopg2
from config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME


conn = psycopg2.connect(host=DB_HOST,
                        dbname=DB_NAME,
                        user=DB_USER,
                        password=DB_PASSWORD,
                        port=DB_PORT)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS interface (
            id SERIAL PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description VARCHAR(255),
            config JSON,
            port_channel_id INT,
            max_frame_size INT
);  
""")

conn.commit()

cur.close()
conn.close()