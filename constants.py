# File to stock All constantes of our programme

#
def validate_entering(debut, fin):
    index = None
    while True:
        try:
            index = int(input('Entrez votre choix: '))
            assert debut <= index <= fin
        except ValueError:
            print('SVP entrez un entier valide')
        except AssertionError:
            print(f"SVP entrez un entier entre [{debut}-{fin}]")
        else:
            break

    return index


def yes_no():
    index = None
    while index not in ['Oui', 'Non']:
        try:
            index = (input('Entrez votre choix:(Oui/Non) ').capitalize())
        except ValueError:
            print('SVP entrez un mot valide')
    return index

