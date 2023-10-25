import os
import unittest
import sys
from io import StringIO


def creer_nouvelle_liste(nom_liste):
    if not os.path.exists("liste"):
        os.mkdir("liste")

    if not nom_liste:
        raise ValueError("Le nom de la liste ne peut pas être vide ! ! ! ")

    liste_path = os.path.join("liste", f"{nom_liste}.txt")

    if os.path.exists(liste_path):
        raise ValueError(f"La liste '{nom_liste}' existe déjà ! ! ! ")

    with open(liste_path, "w") as fichier_liste:
        print(f"La liste '{nom_liste}' a été crée dans le répertoire 'liste' ! ")

class TestCreationListe(unittest.TestCase):
    def test_creer_nouvelle_liste(self):
        
        # Tester la création d'une nouvelle liste avec un nom valide
        with self.subTest(msg="Test avec un nom valide ! ! "):
            nom_liste = "MaListe"
            creer_nouvelle_liste(nom_liste)
            self.assertTrue(os.path.exists(f"liste/{nom_liste}.txt"))
        
        # Tester la création d'une nouvelle liste avec un nom existant
        with self.subTest(msg="Test avec un nom existant ! ! "):
            nom_liste = "MaListe"
            with self.assertRaises(ValueError):
                creer_nouvelle_liste(nom_liste)

        # Tester la création d'une nouvelle liste avec un nom vide
        with self.subTest(msg="Test avec un nom vide ! ! "):
            nom_liste = ""
            with self.assertRaises(ValueError):
                creer_nouvelle_liste(nom_liste)


def afficher_liste(nom_liste):
    liste_path = os.path.join("liste", f"{nom_liste}.txt")
    if os.path.exists(liste_path):
        with open(liste_path, "r") as fichier_liste:
            contenu = fichier_liste.read()
            print(contenu)
    else:
        raise FileNotFoundError(f"La liste '{nom_liste}' n'existe pas.")
def afficher_listes_disponibles():
    if os.path.exists("liste"):
        listes_disponibles = [fichier for fichier in os.listdir("liste") if fichier.endswith(".txt")]
        if not listes_disponibles:
            print("Aucune liste n'est disponible.")
        else:
            print("Listes disponibles :")
            for liste in listes_disponibles:
                nom_base, _ = os.path.splitext(liste)
                print(nom_base)
    else:
        print("Le répertoire 'liste' n'existe pas.")




def supprimer_liste(nom_liste):
    # Verifier si le repertoire existe
    liste_path = os.path.join("liste", f"{nom_liste}.txt")
    if os.path.exists(liste_path):
        os.remove(liste_path)
        print(f"La liste '{nom_liste}' a été supprimée.")
    else:
        print(f"La liste '{nom_liste}' n'existe pas et ne peut pas être supprimée.")

class TestSupprimerListe(unittest.TestCase):
    def test_supprimer_liste(self):

        with self.subTest(msg="Test Suppression avec succes ! ! "):
            # Crée un fichier de liste de test
            nom_liste = "MaListe"
            test_liste_path = os.path.join("liste", f"{nom_liste}.txt")
            
            # Utilisez la fonction supprimer_liste pour supprimer le fichier de test
            supprimer_liste(nom_liste)

            # Vérifiez que le fichier a été supprimé
            self.assertFalse(os.path.exists(test_liste_path))

        with self.subTest(msg="Test Suppression de fichier inexistant"):
            liste_inexistant = "inexistant"

            # Utiliser la fonction supprimer_liste pour essayer de supprimer un fichier qui n'existe pas
            with self.assertRaises(ValueError):
                supprimer_liste(liste_inexistant)


if __name__ == "__main__":
    unittest.main()