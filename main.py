from LibraryServiceConnection import LibraryServiceConnection
from Book import deseriazile_books_from_xml
from Window import Window

conn = LibraryServiceConnection()
xml = conn.make_request("get_all")

books = deseriazile_books_from_xml(xml)

window = Window(books)
window.mainloop()
