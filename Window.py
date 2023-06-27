import tkinter as tk


class Window(tk.Tk):
    def __init__(self, books):
        super().__init__()
        self.title('Books service')
        self.books = books
        self.load_items()

    def load_items(self):
        for row, book in enumerate(self.books):
            container = BookContainer(self, book)
            container.grid(row=row, column=0, sticky='w')


class BookContainer(tk.Frame):
    def __init__(self, master, book):
        super().__init__(master, padx=10, pady=10)

        self.title_label = tk.Label(self, text=book.title)
        self.title_label.pack()

        self.author_label = tk.Label(self, text=book.author, fg="grey")
        self.author_label.pack()
