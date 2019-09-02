"""Module that creates the database and tables
"""
import mysql.connector
from mysql.connector import errorcode
from category import Category
from product import Product
from favori import Favorite
from database import my_cursor, connexion, upload_data
from constants import DATABASE_NAME, data_categories


TABLES = {}  # miniscule


# definition of the function that creates the database
def create_database(cursor):
    """Function that creates the database and returns 1 if there is an error
    """
    try:
        cursor.execute(
            f"CREATE DATABASE {DATABASE_NAME} DEFAULT CHARACTER SET 'utf8'")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)


def check_database():
    """Method checks if a database is created if not it creates it
    """
    try:
        my_cursor.execute(f"USE {DATABASE_NAME}")
        return False
    except mysql.connector.Error as err:
        print(f"Database {DATABASE_NAME} does not exists.")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(my_cursor)
            print(f"Database {DATABASE_NAME} created successfully.")
            connexion.database = DATABASE_NAME
            return True
        return False


# Function that creates a tables
def data_init():
    """Function that creates the different tables
    """
    # Create Category table (SQL REQUEST)
    categorie = Category()
    product = Product()
    favorite = Favorite()
    TABLES = {
        'Category': categorie.create(),
        'Product': product.create(),
        'Favorite': favorite.create()
    }
    # Create all table of DB
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f"Creating table {table_name}: ", end='')
            my_cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:

            print("OK")

    # Insert 6 categories in my category table(manually)
    categorie.insert_data()
    # The categories of my table
    categoy_index = list()
    for item in data_categories:
        categoy_index.append(item[1])

        # browse categories and insert data
    for index in enumerate(categoy_index):
        # Upload json file from api
        data_for_insert = upload_data(index[1], 1)
        # Insert data in Product table
        taille = len(data_for_insert['products'])
        print(f'{index[1]} - produits: {taille}')

        # The loop that inserts the data into my tables
        for i in range(taille):
            try:
                store = data_for_insert['products'][i]['stores']
                name = data_for_insert['products'][i]['product_name']
                grade = data_for_insert['products'][i]['nutrition_grades_tags'][0]
                url = data_for_insert['products'][i]['url']
                id_category = index[0] + 1
            except(KeyError, TypeError):
                continue
            finally:
                product.insert_data(name, url, grade, id_category, store)
