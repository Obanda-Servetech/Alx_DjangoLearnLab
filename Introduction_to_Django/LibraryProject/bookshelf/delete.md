book.delete()
print(Book.objects.all())  # Should return an empty QuerySet
["book.delete", "from bookshelf.models import Book"]