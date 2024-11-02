import sqlite3

class Database:
    def __init__(self):
        self.connection = sqlite3.connect('library.db')
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                "CREATE TABLE IF NOT EXISTS books (title TEXT, author TEXT)"
            )

    def add_book(self, title, author):
        with self.connection:
            self.connection.execute("INSERT INTO books (title, author) VALUES (?, ?)", (title, author))

    def view_books(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()
