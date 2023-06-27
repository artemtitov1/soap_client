import xml.etree.ElementTree as Et


class Book(object):
    def __init__(self, id, author, title, genre,
                 price, publish_date, description):
        self.id = id
        self.author = author
        self.title = title
        self.genre = genre
        self.price = price
        self.publish_date = publish_date
        self.description = description


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
