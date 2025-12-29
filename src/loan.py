class Loan:
    def __init__(self, livre, utilisateur):
        self.livre = livre
        self.utilisateur = utilisateur
        livre.disponible = False
        utilisateur.emprunts.append(self)

    def retour(self):
        self.livre.disponible = True
        self.utilisateur.emprunts.remove(self)
