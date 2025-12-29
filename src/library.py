from book import Book
from user import User
from loan import Loan

class Library:
    def __init__(self):
        self.livres = []
        self.utilisateurs = []
        self.emprunts = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def supprimer_livre(self, isbn):
        self.livres = [l for l in self.livres if l.isbn != isbn]

    def inscrire_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def emprunter_livre(self, isbn, identifiant):
        livre = next((l for l in self.livres if l.isbn == isbn and l.disponible), None)
        utilisateur = next((u for u in self.utilisateurs if u.identifiant == identifiant), None)
        if livre and utilisateur:
            emprunt = Loan(livre, utilisateur)
            self.emprunts.append(emprunt)
            return emprunt
        return None

    def retourner_livre(self, isbn, identifiant):
        emprunt = next((e for e in self.emprunts if e.livre.isbn == isbn and e.utilisateur.identifiant == identifiant), None)
        if emprunt:
            emprunt.retour()
            self.emprunts.remove(emprunt)

    def afficher_etat(self):
        print("Livres :")
        for livre in self.livres:
            print(livre)
        print("\nEmprunts actifs :")
        for emprunt in self.emprunts:
            print(f"{emprunt.utilisateur.nom} a emprunté {emprunt.livre.titre}")
