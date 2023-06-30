import tkinter as tk

from Connection.LibraryServiceConnection import LibraryServiceConnection
from UI.BookContainer import *
from functools import partial


class StateManager:
    def __init__(self, window):
        self.state_functions = {
            "start": self.start_state,
            "get": self.get_state,
            "post": self.post_state,
            "delete": self.delete_state
        }
        self.window = window
        self.connection = LibraryServiceConnection()
        self.set_state("start")

    def set_state(self, layout):
        state_function = self.state_functions.get(layout)
        if state_function:
            self.clear_window()
            state_function()

    def start_state(self):
        get_button = tk.Button(self.window, text="Получить список всех книг")
        get_button.bind("<Button-1>", lambda event: self.set_state("get"))
        get_button.pack()

        post_button = tk.Button(self.window, text="Добавить новую книгу")
        post_button.bind("<Button-1>", lambda event: self.set_state("post"))
        post_button.pack()

        delete_button = tk.Button(self.window, text="Удалить книгу")
        delete_button.bind("<Button-1>", lambda event: self.set_state("delete"))
        delete_button.pack()

    def get_state(self):
        xml = self.connection.make_request("get_all")
        books = deseriazile_books_from_xml(xml)
        container = BookContainer(self.window, books)
        container.display_books_container()

        back_button = tk.Button(self.window, text="На главный экран")
        back_button.bind("<Button-1>", lambda event: self.set_state("start"))
        back_button.pack()

    def post_state(self):
        self.window.grid()
        id_label = tk.Label(self.window, text="ID")
        id_label.grid(row=0, column=0, sticky=tk.E)

        id_entry = tk.Entry(self.window)
        id_entry.grid(row=0, column=1, sticky=tk.E)

        author_label = tk.Label(self.window, text="Автор")
        author_label.grid(row=1, column=0, sticky=tk.E)

        author_entry = tk.Entry(self.window)
        author_entry.grid(row=1, column=1, sticky=tk.E)

        title_label = tk.Label(self.window, text="Название")
        title_label.grid(row=2, column=0, sticky=tk.E)

        title_entry = tk.Entry(self.window)
        title_entry.grid(row=2, column=1, sticky=tk.E)

        genre_label = tk.Label(self.window, text="Жанр")
        genre_label.grid(row=3, column=0, sticky=tk.E)

        genre_entry = tk.Entry(self.window)
        genre_entry.grid(row=3, column=1, sticky=tk.E)

        price_label = tk.Label(self.window, text="Цена")
        price_label.grid(row=4, column=0, sticky=tk.E)

        price_entry = tk.Entry(self.window)
        price_entry.grid(row=4, column=1, sticky=tk.E)

        publish_date_label = tk.Label(self.window, text="Дата публикации")
        publish_date_label.grid(row=5, column=0, sticky=tk.E)

        publish_date_entry = tk.Entry(self.window)
        publish_date_entry.grid(row=5, column=1, sticky=tk.E)

        description_label = tk.Label(self.window, text="Описание")
        description_label.grid(row=6, column=0, sticky=tk.E)

        description_entry = tk.Entry(self.window)
        description_entry.grid(row=6, column=1, sticky=tk.E)

        commit_button = tk.Button(self.window, text="Сохранить")
        commit_button.bind("<Button-1>",
                           lambda event, id=id_entry, author=author_entry,
                           title=title_entry, genre=genre_entry,
                           price=price_entry, publish_date=publish_date_entry,
                           description=description_entry: self.connection.make_request
                           ("post_book",
                            {'id': id.get(), 'author': author.get(),
                             'title': title.get(), 'genre': genre.get(),
                             'price': price.get(), 'publish_date': publish_date.get(),
                             'description': description.get()
                             }))
        commit_button.grid(row=7, column=0, sticky=tk.W+tk.E, columnspan=2)

        back_button = tk.Button(self.window, text="На главный экран")
        back_button.bind("<Button-1>", lambda event: self.set_state("start"))
        back_button.grid(row=8, column=0, sticky=tk.W+tk.E, columnspan=2)

    def delete_state(self):
        self.window.grid()
        id_label = tk.Label(self.window, text="ID")
        id_label.grid(row=0, column=0, sticky=tk.E)

        id_entry = tk.Entry(self.window)
        id_entry.grid(row=0, column=1, sticky=tk.E)
        commit_button = tk.Button(self.window, text="Удалить")
        commit_button.bind("<Button-1>",
                           lambda event, id=id_entry: self.connection.
                           make_request("delete_book", {'id': id.get()}))
        commit_button.grid(row=1, column=0, sticky=tk.W+tk.E, columnspan=2)
        back_button = tk.Button(self.window, text="На главный экран")
        back_button.bind("<Button-1>", lambda event: self.set_state("start"))
        back_button.grid(row=2, column=0, sticky=tk.W + tk.E, columnspan=2)

    def clear_window(self):
        for widget in self.window.winfo_children():
            widget.destroy()

