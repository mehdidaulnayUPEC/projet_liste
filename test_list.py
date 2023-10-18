import os
import unittest


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
        
#verifier existance fichier de la nvl liste
class TestCreationListe(unittest.TestCase):
    def test_verifier_fichier_cree(self):
        nom_liste = "MaListe"
        creer_nouvelle_liste(nom_liste)
        liste_path = os.path.join("liste", f"{nom_liste}.txt")
        self.assertTrue(os.path.exists(liste_path), f"Le fichier '{nom_liste}.txt' a été créé avec succès.")


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


if __name__ == "__main__":
    unittest.main()
