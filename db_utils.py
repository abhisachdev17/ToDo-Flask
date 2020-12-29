import os 
import sqlite3
import uuid 

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path = DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con

def db_init():
    
    con = db_connect()
    cur = con.cursor()

    try:
        item_table = """ 
        CREATE TABLE items (
        id text PRIMARY KEY,
        item text NOT NULL,
        status text NOT NULL)"""

        cur.execute(item_table)

        print("Database Setup Complete.. ")
    except Exception as e:
        print(e)

# add an item in the database with a random guid as the key
def add_item(item, status):
    try:
        k = str(uuid.uuid4())
        conn = db_connect()
        c = conn.cursor()

        c.execute('insert into items(id, item, status) values(?,?,?)', (k,item,status))

        conn.commit()

        return {"key":k , "item":item, "status": status}
    except Exception as e:
        print(e)
        return None
    