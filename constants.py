""" Module to stock All constantes of our programme"""
import platform
DATABASE_NAME = 'OpenFood'
HOST = '127.0.0.1'
USER = 'root'
PASSWORD = 'djamel2013'
NUMBER_PRODUCT_PAGE = 50
NUMBER_VAFORITE_PAGE = 20
NUMBER_VAFORITE = 10

# Check os system
clear = ''
if platform.system() == 'Linux' or platform.system() == '':
    clear = 'clear'
else:
    clear = 'cls'

NUMBER_PRODUCT = 100
data_categories = [
            (1, "Boissons"),
            (2, 'Produits laitiers'),
            (3, 'Biscuits'),
            (4, 'Petit-déjeuners'),
            (5, 'Plats préparés'),
            (6, 'Produits à tartiner')
        ]