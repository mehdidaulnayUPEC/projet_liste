#!/usr/bin/python3
import unittest
import os

def affiche_menu():
    """Fonction permettant d'afficher le menu"""
    print("""
****************************************
Menu principal
  [M]    Menu principal
  [A]    Afficher une Liste
  [N]    Nouvelle Liste
  [S]    Supprimer une Liste
  [E]    Modifier une Liste
  [Q]    Quitter le programme
****************************************""")
    
def creer_nouvelle_liste():
    # Crée le répertoire "liste" s'il n'existe pas
    if not os.path.exists("liste"):
        os.mkdir("liste")

    while True:
        nom_liste = input("Entrez le nom de la nouvelle liste : ").strip() #strip permet de supprimer les espaces inutiles

        if not nom_liste:
            print("Le Nom ne doit pas etre vide ! ! ! \n Veuillez saisir un nom. \n")
        else:
            liste_path = os.path.join("liste", f"{nom_liste}.txt")

            # Vérifier si la liste existe déjà
            if os.path.exists(liste_path):
                print(f"La liste '{nom_liste}' existe déjà.")
            else:
                # Créer un fichier pour la nouvelle liste
                with open(liste_path, "w") as fichier_liste:
                    print(f"La liste '{nom_liste}' a été créée dans le répertoire 'liste'.")
                break # sortir de la boucle une fois validé


#Mehdi verifier exstance du fichier 
if os.path.exists(liste_path):
    print(f"Le fichier '{nom_liste}.txt' a été créé avec succès.")
else:
    print(f"Le fichier '{nom_liste}.txt' n'a pas été créé.")
    

def liste_existe_deja(nom_liste):
    liste_path = os.path.join("liste", f"{nom_liste}.txt")
    return os.path.exists(liste_path)

#fin



if __name__ == "__main__":
    while True:
        affiche_menu()  # Afficher le menu
        choix = input("Choisissez une option : ").strip().upper()  # Obtenir la saisie de l'utilisateur et la convertir en majuscules
        if choix == 'N':
            creer_nouvelle_liste()  # Appeler la fonction pour créer une nouvelle liste
        elif choix == 'A':
            # Appeler la fonction pour afficher une liste
            pass  # Remplacez "pass" par le code approprié
        elif choix == 'S':
            # Appeler la fonction pour supprimer une liste
            pass  # Remplacez "pass" par le code approprié
        elif choix == 'E':
            # Appeler la fonction pour modifier une liste
            pass  # Remplacez "pass" par le code approprié
        elif choix == 'Q':
            break  # Quitter le programme
        else:
            print("Option invalide. Veuillez choisir une option valide.")