# Projet : Bibliothèque Numérique

## Description
Système de gestion d'une bibliothèque numérique en Python (POO) permettant :
- Ajouter/supprimer des livres
- Inscrire des utilisateurs
- Gérer les emprunts et retours
- Afficher l’état de la bibliothèque

## Structure
bibliotheque_numerique/
│
├── src/
│   ├── book.py
│   ├── user.py
│   ├── loan.py
│   └── library.py
│
├── uml/
│   ├── class_diagram.puml
│   └── class_diagram.png
│
├── README.md
├── git_commands.txt

## Classes principales
- **Book** : livre (titre, auteur, ISBN, disponibilité)  
- **User** : utilisateur (nom, ID, emprunts)  
- **Loan** : emprunt (livre, utilisateur, date)  
- **Library** : gère livres, utilisateurs et emprunts  

## Utilisation
```python
from src.book import Book
from src.user import User
from src.library import Library

lib = Library()
b1 = Book("Livre 1", "Auteur A", "123")
u1 = User("Ahmed", 1)
lib.add_book(b1)
lib.register_user(u1)
lib.borrow_book(u1, b1)
lib.display_status()
