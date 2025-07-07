class Library:
    total_books = 0
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        Library.total_books += 1
    @staticmethod
    def validate_isbn(isbn):
        return isbn.isdigit() and len(isbn) == 10
    @classmethod
    def from_string(cls, book_str):
        title, author, isbn = book_str.split(',')
        if cls.validate_isbn(isbn.strip()):
            return cls(title.strip(), author.strip(), isbn.strip())
        else:
            raise ValueError("Invalid ISBN. ISBN must be exactly 10 digits.")
    @classmethod
    def get_total_books(cls):
        return cls.total_books

books = []

while True:
    print("\nMenu:\n1. Add Book\n2. View Total Books\n3. Exit")
    choice = input("Enter choice: ")

    if choice == '1':
        book_str = input("Enter book details (title,author,isbn): ")
        try:
            book = Library.from_string(book_str)
            books.append(book)
            print(f"Book '{book.title}' added.")
        except ValueError as e:
            print(e)
    elif choice == '2':
        print(f"Total books in library: {Library.get_total_books()}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
