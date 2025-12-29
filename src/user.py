class User:
    def __init__(self, nom, identifiant):
        self.nom = nom
        self.identifiant = identifiant
        self.emprunts = []

    def __str__(self):
        return f"{self.nom} (ID: {self.identifiant})"
