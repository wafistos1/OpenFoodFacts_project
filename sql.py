import mysql.connector
from mysql.connector import errorcode
from database import my_cursor, connexion, upload_data

DB_NAME = 'OpenFood'
data_exist = False

TABLES = {}
TABLES['Product'] = (
    "CREATE TABLE `Product` ("
    "  `id` int(11) NOT NULL AUTO_INCREMENT,"
    "  `name` varchar(450) NOT NULL UNIQUE,"
    "  `url` varchar(450) NOT NULL,"
    "  `grade` varchar(40) ,"
    "  `id_category` int(40) ,"
    "  `store` varchar(540) ,"
    "  PRIMARY KEY (`id`)"
    ") ENGINE=InnoDB")

TABLES['Category'] = (
    "CREATE TABLE `Category` ("
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

# definition of the function that creates the database
def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

def check_database():
    """Method checks if a database is created if not it creates it
    """ 
    global data_exist
    try:
        my_cursor.execute("USE {}".format(DB_NAME))
    except mysql.connector.Error as err:
        print(f"Database {DB_NAME} does not exists.")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            create_database(my_cursor)
            print(f"Database {DB_NAME} created successfully.")
            connexion.database = DB_NAME
            data_exist = True
            print(data_exist)
            print('Ok')
        else:
            print(err)
            exit(1)

# Function that creates a database if it does not exist
def data_init():
    check_database()

    # Create different tables
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

    # The categories of my table
    categoy_index = ('Boissons', 'Produits laitiers','Biscuits' , 'Petit-déjeuners', 'Plats préparés', 'Produits à tartiner')
    id_cat = 1



    # browse categories and insert data
    for index in categoy_index:
        # Upload json file from api
        data_for_insert = upload_data(index, 1)

        # Insert data in Product table
        taille = len(data_for_insert['products'])

        print(taille)

        add_Product = (
            "INSERT IGNORE INTO Product "
            "(name, url, grade, id_category, store)"
            "VALUES (%s,  %s, %s, %s, %s)"
            )

        #The loop that inserts the data into my tables
        for i in range(taille):

            try:
                store = data_for_insert['products'][i]['stores']
                name = data_for_insert['products'][i]['product_name']
                # category = data_for_insert['products'][i]['categories']
                grade = data_for_insert['products'][i]['nutrition_grades_tags'][0]
                url = data_for_insert['products'][i]['url']
                id_category = id_cat

            except(KeyError, TypeError):
                continue

            finally:
                food_data_Product = (name, url, grade, id_category, store)
                my_cursor.execute(add_Product, food_data_Product )
                connexion.commit()
        
        id_cat += 1
        query2 =(
        "INSERT IGNORE INTO Category (id, name) VALUE (%s, %s)"
        )
        data_categories = [
            (1, "Boissons"),
            (2, 'Produits laitiers'),
            (3, 'Biscuits'),
            (4, 'Petit-déjeuners'),
            (5, 'Plats préparés'),
            (6, 'Produits à tartiner')
        ]

        for i in data_categories:
            my_cursor.execute(query2, i)

#my_cursor.close()
#connexion.close()
