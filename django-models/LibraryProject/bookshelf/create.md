from bookshelf.models import Book
Book.objects.create", "title", "author", "George Orwell
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
