from flask import Flask, render_template
import random 
import string 
import sqlite3

app = Flask(__name__) 

@app.route('/') 
def main(): 
    return render_template('index.html')

@app.route('/shrink', methods=['POST'])
def shrink():
    #https://google.com/340i930f9s0dfsf
    #https://linker.dev/
    #generate short id
    #map it to real url in db
    new_url = "lynker.dev/" + generate_random_id(3)
    return new_url
  




def generate_random_id(id_length):
    id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=id_length))
    return id


# def create_connection(db_file):
#     """ create a database connection to the SQLite database
#         specified by db_file
#     :param db_file: database file
#     :return: Connection object or None
#     """
#     conn = None
#     try:
#         conn = sqlite3.connect(db_file)
#     except Error as e:
#         print(e)
 
#     return conn


if __name__ == '__main__': 
    app.run(port=3001,debug=True)