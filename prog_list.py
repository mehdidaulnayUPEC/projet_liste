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