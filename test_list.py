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


if __name__ == "__main__":
    unittest.main()
