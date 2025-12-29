from library import Library
from book import Book
from user import User

biblio = Library()

biblio.ajouter_livre(Book("Mathématiques pour l'ingénieur", "Gilbert Strang", "M01"))
biblio.ajouter_livre(Book("Physique générale", "David Halliday", "P01"))
biblio.ajouter_livre(Book("Chimie fondamentale", "Raymond Chang", "S01"))
biblio.ajouter_livre(Book("Biologie", "Campbell", "S02"))
biblio.ajouter_livre(Book("Algèbre linéaire", "Sheldon Axler", "M02"))

biblio.inscrire_utilisateur(User("Yacine Benali", "U01"))
biblio.inscrire_utilisateur(User("Nassima Boudiaf", "U02"))
biblio.inscrire_utilisateur(User("Rachid Khelifi", "U03"))
biblio.inscrire_utilisateur(User("Amel Harbi", "U04"))

biblio.emprunter_livre("M01", "U01")
biblio.emprunter_livre("P01", "U02")
biblio.emprunter_livre("S01", "U03")

biblio.afficher_etat()

biblio.retourner_livre("M01", "U01")
print("\nAprès retour du livre :\n")
biblio.afficher_etat()
