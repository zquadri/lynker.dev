from flask import Flask, render_template, request, redirect
import random
import string
import sqlite3
from flask import jsonify
from urllib.parse import urlparse

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


app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/shrink', methods=['POST'])
def shrink():
    # connect to db
    conn = sqlite3.connect('lynker.db')
    c = conn.cursor()
    body = request.json
    url = body['url']
    c.execute('SELECT link_id FROM links WHERE original_link = ?', [url])
    results = c.fetchone()
    l_id = ''
    if(results == None):
        l_id = generate_random_id(3)
        print(l_id, url)
        c.execute('''
        INSERT INTO links (link_id, original_link) VALUES (?,?)
        ''', (l_id, url))
        conn.commit()

    else:
        l_id = results[0]

    return "lynker.dev/" + l_id


@app.route('/<l_id>')
def link_redirect(l_id):
    print(l_id)
    conn = sqlite3.connect('lynker.db')
    c = conn.cursor()
    c.execute('SELECT original_link FROM links WHERE link_id = ?', [l_id])
    results = c.fetchone()
    print(results)
    url = results[0]
    print(url)
    if(url.startswith("http://") or url.startswith("https://")):
        return redirect(url)
    return redirect("http://" + url)


# @app.route('/expand', methods=['GET'])
# def expand():


def generate_random_id(id_length):
    id = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=id_length))
    return id


if __name__ == '__main__':
    app.run(port=3001, debug=True)
