import psycopg2
import os

from config import password
from config import database
from config import user

# Connect to the database
try:
    connection = psycopg2.connect(database=database, user=user, password=password)
except Exception as e:
    print(e)
    exit()

current_path = os.getcwd()
channel_folder_list = os.listdir(current_path)

# Query the database, leaving you with a "cursor"--an object you can
# use to iterate over the rows generated by your query.
try:
    cursor = connection.cursor()

    for folder in channel_folder_list:
        if folder.startswith('geo'): 
            file_path = current_path + "/{0}".format(folder)
            for fname in os.listdir(file_path):
                if fname.endswith("csv"):
                    
                    query = '''CREATE TABLE {0} (
                    id INTEGER,
                    channel_name TEXT)'''.format{fname}
                    cursor.execute(query)
except Exception as e:
    print(e)
    exit()






