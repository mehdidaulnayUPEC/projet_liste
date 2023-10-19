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


def afficher_liste():
    
    if os.path.exists("liste"):
         # Listez les fichiers disponibles dans le répertoire "liste"
        listes_disponibles = [fichier for fichier in os.listdir("liste") if fichier.endswith(".txt")]
        
        if not listes_disponibles:
            print("Aucune liste n'est disponible.")
        else:
            print("Listes disponibles :")
            for liste in listes_disponibles:
                print(liste)

            nom_liste = input("Quelle liste voulez-vous afficher : ").strip()
            liste_path = os.path.join("liste", f"{nom_liste}.txt")
        try:
            with open(liste_path, "r") as fichier_liste:
                contenu = fichier_liste.read()
                print(contenu)
                
        except FileNotFoundError:
            print(f"La liste '{nom_liste}' n'existe pas.")
    else:
        print("Le répertoire 'liste' n'existe pas.")


def modifier_liste():
     if os.path.exists("liste"):
         nom_liste = input("Quelle liste voulez-vous modifier : ").strip() #strip permet de supprimer les espaces inutiles
         liste_path = os.path.join("liste", f"{nom_liste}.txt")

         if os.path.exists(liste_path):
             print(f"Contenu actuel de la liste '{nom_liste}' : \n ")

             # Lire le contenu actuel du fichier
             with open(liste_path, "r") as fichier_liste:
                     contenu = fichier_liste.read()
                     print(contenu)

             # Demander à l'utilisateur de saisir la modification
             nouveau_contenu = input(f"Entrez la modification pour la liste '{nom_liste}': \n")

             # Écrire le nouveau contenu dans le fichier
             with open(liste_path, "w") as fichier_liste:
                 fichier_liste.write(nouveau_contenu)

             print(f"Le contenu de la liste '{nom_liste}' a été modifiée avec succès.")

         else :
             print(f"La liste '{nom_liste}' n'existe pas. Vous devez d'abord créer des fichiers.")

     else :
         print("Pour modifier, il faut d'abord créer des fichiers.")


def supprimer_liste():
    if os.path.exists("liste"):
        nom_liste = input("Quelle liste voulez-vous supprimer : ").strip() #strip permet de supprimer les espaces inutiles
        liste_path = os.path.join("liste", f"{nom_liste}.txt")

        if os.path.exists(liste_path): # Vérifie si le fichier de la liste existe
            reponse = input(f"Voulez-vous supprimer le fichier '{nom_liste}'?\n (Oui/Non)  ").strip().lower() # Demande à l'utilisateur s'il veut supprimer la liste
            
            if reponse == "oui":
                # Supprimer le fichier de la liste
                os.remove(liste_path)
                print(f"La liste '{nom_liste}' a été supprimée.")
            else:
                print ("La saisie n'est pas valide")

        else:
            print ("Le fichier dans le répertoire liste n'existe pas.")

    else :
        print ("Le répertoire des listes n'existes pas, Vous devez creer une liste au préalable")


if __name__ == "__main__":
    while True:
        affiche_menu()  # Afficher le menu
        choix = input("Choisissez une option : ").strip().upper()  # Obtenir la saisie de l'utilisateur et la convertir en majuscules
        if choix == 'N':
            creer_nouvelle_liste()  #Appeler la fonction pour créer une nouvelle liste
        elif choix == 'A':
            afficher_liste() # Appeler la fonction pour afficher une liste
        elif choix == 'S':
            supprimer_liste() #Appeler la fonction pour supprimer une liste
        elif choix == 'E':
            modifier_liste()  #Appeler la fonction pour modifier une liste
        elif choix == 'Q':
            break  # Quitter le programme
        else:
            print("Option invalide. Veuillez choisir une option valide.")