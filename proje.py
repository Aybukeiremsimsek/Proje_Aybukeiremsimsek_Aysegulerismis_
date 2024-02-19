class Library:
    def __init__(self):
        self.file = open("books.txt", "a+")

    def __del__(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.readlines()
        for book in books:
            book_info = book.strip().split(',')
            print("Title:", book_info[0])
            print("Author:", book_info[1])
            print("Release Date:", book_info[2])
            print("Number of Pages:", book_info[3])
            print()

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        release_date = input("Enter release date: ")
        num_pages = input("Enter number of pages: ")
        book_info = f"{title},{author},{release_date},{num_pages}\n"
        self.file.write(book_info)
        print("Book added successfully.")

    def remove_book(self):
        title = input("Enter the title of the book you want to remove: ")
        self.file.seek(0)
        books = self.file.readlines()
        new_books = []
        for book in books:
            if title not in book:
                new_books.append(book)
        self.file.seek(0)
        self.file.truncate()
        self.file.writelines(new_books)
        print("Book removed successfully.")


def main():
    lib = Library()
    while True:
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            lib.list_books()
        elif choice == '2':
            lib.add_book()
        elif choice == '3':
            lib.remove_book()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
                main()
