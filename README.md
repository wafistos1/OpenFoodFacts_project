
#
# Projet5 "Utilisez les données publiques de l'OpenFoodFacts"
_


## Ce programme interagirait avec la base Open Food Facts pour en récupérer les aliments, les comparer et proposer à l'utilisateur un substitut plus sain.

## Pour commencer
- Ce programme ce compose des elements suivants

### Menu pricipal

- Utilisateur doit selectionner un choix parmi le menu en tapant le nombre corespondant  

### Menu Afficher Favoris 

- Le programme affiche tous les favoris qui sont dans la base de donnes

### Menu Rechercher un produit

- Le programme affiche un menu des categories qui existes et demande a l'utilisateur de faire un choix

- Le programme affiche tous les produits qui sont dans la base de donnes relative a la gategorie choisi preablement, apres le programme demande a l'utilisateur de faire un choix du produit qui veut en suite le programme affiche le substitut du produit choisi
et enfin le programme demande a l'utilisateur si il veut sauvgarder
le produit substitut dans la base de donnees  

### Menu Update ma base de donnees

- Le programme fait une mise a jours de la base de donnees en faisant un check a API OpenFactFood  

### Menu Quitter
- L'utilisateur choisi de quitter le programme  

### Pré-requis

Ce qu'il est requis pour commencer avec mon programme.

- Installer Python3 
- Installer les dependances avec le fichier `requirements.txt`
- Entrer le `USER` et `PASSWORD` de ta base de donnees SQL dans le   fichier`constants.py` 

## Démarrage

Pour lancer votre projet
 
- Taper dans un terminal `python3 main.py` 

## Les differents options du script(modification et personnalisation)

- Utilisateur pourra si il le veut personnaliser le programme.   
voici toutes les fonctionnalites personnalisable  
    * Affichage (nombre de produit a affiche)de la liste des produits       dans la categorie selectionnee en changeant la constante           
    `NUMBER_PRODUCT_PAGE`qui se trouve dans le fichier 
    `constants.py`
    * Affichage (nombre de substituts a affiche) en changeant la constante 
    `NUMBER_VAFORITE_PAGE`qui se trouve dans le fichier 
    `constants.py`
    * `NUMBER_PRODUCT`  Nombre de produits qu'on doit charger de l'API max 1000 produits
    * `data_categories` Une listes des noms des categories a partir du quel vous voulez chercher des produits 
        il suffit juste de modifiez ou ajouter une ou plusieurs nom de categories
        par defaut il y'a six(06) categories. 
    

## Fabriqué avec

Les programmes/logiciels/ressources utilisé pour développer le projet


* [mysql-connector](https://dev.mysql.com/doc/connector-python/en/) - un pilote Python autonome pour communiquer avec les serveurs MySQL
* [Visual-Studio-code](https://code.visualstudio.com) - Editeur de textes


## Auteurs
auteur(s) du projet 
* **Ouafi MAMERI** _WAFI_ [mameri.wafi@gmail.com](https://github.com/wafistos1/Projet5)


_(https://github.com/wafistos1/Projet5 ``/openclassrooms``)_

