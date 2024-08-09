import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

def list_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()
    return books

def retrieve_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)
    return librarian

# Example usage
if __name__ == '__main__':
    author_name = 'Author Name'
    library_name = 'Library Name'

    print(f"Books by {author_name}:")
    for book in query_books_by_author(author_name):
        print(book.title)

    print(f"\nBooks in {library_name}:")
    for book in list_books_in_library(library_name):
        print(book.title)

    librarian = retrieve_librarian_for_library(library_name)
    print(f"\nLibrarian for {library_name}: {librarian.name}")
