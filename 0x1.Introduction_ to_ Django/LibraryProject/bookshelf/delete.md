from bookshelf.models import Book

book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
books = Book.objects.all()
print(books)
# Expected Output: Book instance deleted successfully. <QuerySet []> confirming no books present.
