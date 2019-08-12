"""Module that tries to connect to the database and loads the
    data from the API into a JSON file
"""
import requests
import mysql.connector
from mysql.connector import errorcode
from constants import HOST, USER, PASSWORD

# Creation a connexion to database
try:
    connexion = mysql.connector.connect(host=HOST, user=USER, passwd=PASSWORD)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

my_cursor = connexion.cursor(buffered=True)

json_data = None

def upload_data(category, page):
    api_search = 'https://world.openfoodfacts.org/cgi/search.pl?/get'
    payload = {
        'search_terms': '',
        'json': 1,
        'page_size': 100,
        'page': page,
        'categories': category
        }
    json_data = requests.get(api_search, params=payload).json()
    #taille = len(json_data['products'])
    return json_data
