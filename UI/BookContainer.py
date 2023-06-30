import tkinter as tk
import xml.etree.ElementTree as Et
from Model.Book import Book


class BookContainer(tk.Frame):
    def __init__(self, master, books):
        super().__init__(master, padx=10, pady=10)
        self.books = books

    def display_books_container(self):
        for row, book in enumerate(self.books):
            title_label = tk.Label(self, text=book.title)
            title_label.grid(row=row, column=0, sticky='w')

            author_label = tk.Label(self, text=book.author, fg="grey")
            author_label.grid(row=row, column=1, sticky='w')

            self.pack()


def deseriazile_books_from_xml(xml):
    namespace = '{http://tempuri.org/}'
    root = Et.fromstring(xml)
    books = []
    elements = root.findall(f".//{namespace}Book")
    for book in elements:
        id = book.findtext(f"{namespace}id")
        author = book.findtext(f"{namespace}author")
        title = book.findtext(f"{namespace}title")
        genre = book.findtext(f"{namespace}genre")
        price = book.findtext(f"{namespace}price")
        publish_date = book.findtext(f"{namespace}publish_date")
        description = book.findtext(f"{namespace}description")
        new = Book(id, author, title, genre, price, publish_date, description)
        books.append(new)
    return books
