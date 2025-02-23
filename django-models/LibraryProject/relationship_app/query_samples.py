import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'libraryproject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def query_books_by_author(author_name):
    books = Book.objects.filter(author__name=author_name)
    for book in books:
        print(book.title)

# List all books in a library
def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    for book in books:
        print(book.title)

# Retrieve the librarian for a library
def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = library.librarian
    print(librarian.name)

# Example Usage
if __name__ == "__main__":
    query_books_by_author("Author Name")
    list_books_in_library("Library Name")
    get_librarian_for_library("Library Name")
    ["Author.objects.get(name=author_name)", "objects.filter(author=author)"]