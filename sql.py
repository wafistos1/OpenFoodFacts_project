import mysql.connector
from mysql.connector import errorcode
from database import my_cursor, connexion

DB_NAME = 'OpenFood'

TABLES = {}
TABLES['Product'] = (
    "CREATE TABLE `Product` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(450) NOT NULL,"
    "  `url` varchar(450) NOT NULL,"
    "  `grade` varchar(4) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['Category'] = (
    "CREATE TABLE `Category` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(450) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['Store'] = (
    "CREATE TABLE `Store` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(450) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


TABLES['Favorite'] = (
    "CREATE TABLE `Favorite` ("
    "  `id` int(11) NOT NULL,"
    "   `product` varchar(450) NOT NULL,"
    "   `substitute` varchar(450) NOT NULL,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")


# Function that creates a database if it does not exist 
def create_database(my_cursor):
    try:
        my_cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

try:
    my_cursor.execute("USE {}".format(DB_NAME))
except mysql.connector.Error as err:
    print("Database {} does not exists.".format(DB_NAME))
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        create_database(my_cursor)
        print("Database {} created successfully.".format(DB_NAME))
        connexion.database = DB_NAME
    else:
        print(err)
        exit(1)

# Create different tables
for table_name in TABLES:
    table_description = TABLES[table_name]
    try:
        print("Creating table {}: ".format(table_name), end='')
        my_cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)
    else:
        print("OK")

my_cursor.close()
connexion.close()

