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
  [C]    Rajouter du contenue à une Liste
  [Q]    Quitter le programme
****************************************""")
    

def creer_nouvelle_liste():
    # Crée le répertoire "liste" s'il n'existe pas
    if not os.path.exists("liste"):
        os.mkdir("liste")

    while True:
        nom_liste = input("Entrez le nom de la nouvelle liste : ").strip() #strip permet de supprimer les espaces inutiles

        if not nom_liste:
            print("Le Nom ne doit pas etre vide ! ! ! \nVeuillez saisir un nom. \n")
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
                nom_base, _ = os.path.splitext(liste)
                print(nom_base)

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


def rajouter_liste():
    if os.path.exists("liste"):
        # Afficher les listes disponibles
        listes_disponibles = [fichier for fichier in os.listdir("liste") if fichier.endswith(".txt")]

        if not listes_disponibles:
            print("Aucune liste n'est disponible.")
        else:
            print("Voici les listes que vous pouvez modifier :")
            for liste in listes_disponibles:
                nom_base, _ = os.path.splitext(liste)
                print(nom_base)

        nom_liste = input("Quelle liste voulez-vous modifier : ").strip()
        liste_path = os.path.join("liste", f"{nom_liste}.txt")

        if os.path.exists(liste_path):
            print(f"Contenu actuel de la liste '{nom_liste}' : \n ")

            # Lire le contenu actuel du fichier
            with open(liste_path, "r") as fichier_liste:
                contenu = fichier_liste.read()
                print(contenu)

            # Demander à l'utilisateur de saisir la modification
            nouvelle_entree = input(f"Entrez la nouvelle entrée pour la liste '{nom_liste}': \n")

            # Vérifier si la nouvelle entrée n'existe pas déjà dans le contenu
            if nouvelle_entree not in contenu:
                # Ajouter la nouvelle entrée au contenu existant
                contenu += "\n" + nouvelle_entree  # Ajouter un saut de ligne pour séparer les entrées

                # Écrire le nouveau contenu dans le fichier en mode append
                with open(liste_path, "a") as fichier_liste:
                    fichier_liste.write("\n" + nouvelle_entree)

                print(f"La nouvelle entrée a été ajoutée à la liste '{nom_liste}' avec succès.")
            else:
                print("Cette entrée existe déjà dans la liste.")

        else:
            print(f"La liste '{nom_liste}' n'existe pas. Vous devez d'abord créer des fichiers.")

    else:
        print("Le répertoire 'liste' n'existe pas.")



def texte_en_vert(texte):
    return f"\033[32m{texte}\033[0m"

def modifier_liste():
    if os.path.exists("liste"):
        listes_disponibles = [fichier for fichier in os.listdir("liste") if fichier.endswith(".txt")]

        if not listes_disponibles:
            print("Aucune liste n'est disponible.")
        else:
            print("Voici les listes que vous pouvez modifier :")
            for liste in listes_disponibles:
                nom_base, _ = os.path.splitext(liste)
                print(nom_base)

            nom_liste = input("Quelle liste voulez-vous modifier :").strip()
            liste_path = os.path.join("liste", f"{nom_liste}.txt")

            if os.path.exists(liste_path):
                print(f"Contenu actuel de la liste '{nom_liste}' : \n")

                with open(liste_path, "r") as fichier_liste:
                    contenu = fichier_liste.read()
                    print(contenu)

                choix = input("Que souhaitez-vous faire?\n[A] Supprimer un élément\n[M] Mettre en Vert un élément\nChoisissez [A] ou [M]: ").strip().upper()

                if choix == 'A':
                    element_a_supprimer = input("Entrez l'élément que vous souhaitez supprimer de la liste : ")
                    if element_a_supprimer in contenu:
                        contenu = contenu.replace(element_a_supprimer, '')
                        with open(liste_path, "w") as fichier_liste:
                            fichier_liste.write(contenu)
                        print(f"L'élément '{element_a_supprimer}' a été supprimé de la liste '{nom_liste}' avec succès.")
                    else:
                        print(f"L'élément '{element_a_supprimer}' n'existe pas dans la liste.")

                elif choix == 'M':
                    num_ligne = input("Entrez le numéro de la ligne à mettre en vert : ")
                    if num_ligne.isdigit():
                        num_ligne = int(num_ligne)
                        if 1 <= num_ligne <= len(contenu.split('\n')):
                            lignes = contenu.split('\n')
                            lignes[num_ligne - 1] = texte_en_vert(lignes[num_ligne - 1])
                            contenu = '\n'.join(lignes)
                            with open(liste_path, "w") as fichier_liste:
                                fichier_liste.write(contenu)
                            print(f"La ligne {num_ligne} a été mise en vert dans la liste '{nom_liste}' avec succès.")
                        else:
                            print("Numéro de ligne invalide.")
                    else:
                        print("Veuillez entrer un numéro de ligne valide.")

                else:
                    print("Option invalide. Veuillez choisir [A] ou [M].")
            else:
                print(f"Le fichier '{nom_liste}' dans le répertoire 'liste' n'existe pas.")
    else:
        print("Le répertoire 'liste' n'existe pas. Vous devez d'abord créer des fichiers.")


def supprimer_liste():
    if os.path.exists("liste"):
        listes_disponibles = [fichier for fichier in os.listdir("liste") if fichier.endswith(".txt")]

        if not listes_disponibles:
            print("Aucune liste n'est disponible.")
        else:
            print("Voici les listes qui peuvent etre supprimer : ")
            for liste in listes_disponibles:
                nom_base, _ = os.path.splitext(liste)
                print(nom_base)

            nom_liste = input("Quelle liste voulez-vous supprimer : ").strip()
            liste_path = os.path.join("liste", f"{nom_liste}.txt")

            if os.path.exists(liste_path):
                reponse = input(f"Voulez-vous supprimer le fichier '{nom_liste}'?\n (Oui/Non)  ").strip().lower()

                if reponse == "oui":
                    os.remove(liste_path)
                    print(f"La liste '{nom_liste}' a été supprimée.")
                else:
                    print("La saisie n'est pas valide")

            else:
                print(f"Le fichier '{nom_liste}' dans le répertoire 'liste' n'existe pas.")
    else:
        print("Le répertoire 'liste' n'existe pas. Vous devez d'abord créer des fichiers.")


if __name__ == "__main__":
    while True:
        affiche_menu()  # Afficher le menu
        choix = input("Choisissez une option : ").strip().upper()  # Obtenir la saisie de l'utilisateur et la convertir en majuscules
        if choix == 'M':
         affiche_menu()
        elif choix == 'N':
            creer_nouvelle_liste()  #Appeler la fonction pour créer une nouvelle liste
        elif choix == 'A':
            afficher_liste() # Appeler la fonction pour afficher une liste
        elif choix == 'S':
            supprimer_liste() #Appeler la fonction pour supprimer une liste
        elif choix == 'E':
            modifier_liste()  #Appeler la fonction pour modifier une liste
        elif choix == 'C':
            rajouter_liste()  #Appeler la fonction pour ajouter du contenu à une liste
        elif choix == 'Q':
            break  # Quitter le programme
        else:
            print("Option invalide ! ! ! \nVeuillez choisir une option valide.")