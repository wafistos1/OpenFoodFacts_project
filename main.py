""" Script to .....
"""
from product import Product
from favori import Favorite
from sql import check_database, data_init, data_exist

def main():
    """ main fonction for start a script
    """
    check_database()
    print(data_exist)

    # Initialisation our data (upload json file from api)
    if data_exist is False:
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
        favorite_choice = str(input().capitalize())
        if favorite_choice == 'Oui':
            favorite1 = Favorite()
            favorite1.get_all()
        print("Taper A pour sortir ou autres pour continuer")
        continue_choice = str(input().capitalize())
        if continue_choice == 'A':
            break

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
        while index_choice not in [1, 2, 3, 4, 5, 6]:
            try:
                index_choice = int(input("Entrez votre choix SVP: "))
            except ValueError:
                continue

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
        reponse = str(input())
        if reponse == 'Oui':
            favorite = Favorite()
            favorite.insert_data(
                produit.list_favorite[1][0],
                produit.list_favorite[0][1],
                produit.list_favorite[0][2],
                produit.list_favorite[0][3]
            )
        else:
            produit.list_favorite.clear()
        print("                                                       ")
        print("-------------------------------------------------------")
        print("                                                       ")
        print("Voulez vous continuez (Oui / Non)")
        print("                                                       ")
        exit_script = input("Entrez votre choix: ").capitalize()
    print("Aurevoir...")

if __name__ == "__main__":
    main()
