from LibraryServiceConnection import LibraryServiceConnection
from Book import deseriazile_books_from_xml
from Window import Window

# test object
book = {
    'id': '1',
    'author': 'author',
    'title': 'title',
    'genre': 'genre',
    'price': 'price',
    'publish_date': '01.01.01',
    'description': 'description'
}

conn = LibraryServiceConnection()

xml = conn.make_request("post_book",
                        book)

books = deseriazile_books_from_xml(xml)

window = Window(books)
window.mainloop()
