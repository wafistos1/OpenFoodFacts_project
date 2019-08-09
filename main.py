""" Script to .....
"""
from product import Product
from favori import Favorite
from sql import check_database, data_init, data_exist
from constants import validate_entering, yes_no

def main():
    """ main fonction for start a script
    """

    # Initialisation our data (upload json file from api)
    if check_database():
        data_init()
    exit_script = 'Oui'
    while exit_script == 'Oui':
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("****                                               ****")
        print("****   Bienvenue dans le programme openfood        ****")
        print("****                                               ****")
        print("-------------------------------------------------------")
        print("-------------------------------------------------------")
        print("****   Vous voulez afficher les favoris?   ****")
        print("****   (Oui / Non)                                 ****")
        favorite_choice = yes_no()
        if favorite_choice == 'Oui':
            favorite1 = Favorite()
            favorite1.get_all()

        print("-------------------------------------------------------")
        print("****                                               ****")
        print("****   Vous Cherchez un nouveau produit            ****")
        print("****   Choisissez une categorie de produit         ****")
        print("****                                               ****")
        print("-------------------------------------------------------")
        print("1- Boissons")
        print("2- Produits laitiers")
        print("3- biscuits")
        print("4- Petit-déjeuners")
        print("5- Plats préparés")
        print("6- Produits à tartiner")
        print("                                                       ")
        print("-------------------------------------------------------")
        index_choice = None
        index_choice = validate_entering(1, 6)
        produit = Product()
        print("-------------------------------------------------------")
        print("Veuillez patienter...")
        print("-------------------------------------------------------")
        print("                                                       ")
        print("Liste des produits disponible")
        print("                                                       ")
        print("-------------------------------------------------------")
        produit.get_product(index_choice)
        print("                                                       ")
        print("-------------------------------------------------------")
        produit.search_product(index_choice)
        print("-------------------------------------------------------")
        print("Voulez vous sauvgarde ce produit? (Oui/Non)")
        print("                                                       ")
        reponse = yes_no()
        if reponse == 'Oui':
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[1][0],
                produit.list_favorite[0][1],
                produit.list_favorite[0][2],
                produit.list_favorite[0][3]
            )
            print("Votre produit a ete bien enregister")
        else:
            produit.list_favorite.clear()
        print("                                                       ")
        print("-------------------------------------------------------")
        print("                                                       ")
        print("Voulez vous continuez (Oui / Non)")
        print("                                                       ")
        exit_script = yes_no()
    print("Aurevoir...")

if __name__ == "__main__":
    main()
