class Book:
    def __init__ (self, title, author):
        self.title = title
        self.author = author

    def __lt__(self, nextTitle):
        return self.title < nextTitle.title

def sort_books(books):
    return sorted(books)


if __name__ == "__main__":
    books = [
        Book("The Old Man and the Sea", "Ernest Hemingway"),
        Book("Pride and Prejudice", "Jane Austen"),
        Book("The Great Gatsby", "F. Scott Fitzgerald"),
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee")
    ]

    print("Unsorted Books:")
    for book in books:
        print(f"{book.title} by {book.author}")
    sorted_books = sort_books(books)
    print("Sorted Books:")
    for book in sorted_books:
        print(f"{book.title} by {book.author}")


