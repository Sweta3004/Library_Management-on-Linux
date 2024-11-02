from database import Database

def main():
    db = Database()
    while True:
        print("Library Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            db.add_book(title, author)
        elif choice == '2':
            books = db.view_books()
            for book in books:
                print(f"Title: {book[0]}, Author: {book[1]}")
        elif choice == '3':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
