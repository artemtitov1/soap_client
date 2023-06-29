from zeep import Client, Settings
from zeep.plugins import HistoryPlugin
from lxml import etree
import argparse


class LibraryServiceConnection:
    client: Client
    history = HistoryPlugin()

    def __init__(self):
        argparser = argparse.ArgumentParser()
        argparser.add_argument("--addr", type=str, help="Path to library web-service")
        argparser.add_argument("-a", type=str, help="Get all books")
        argparser.add_argument("-i", type=str, help="Get certain book by id")
        args = argparser.parse_args()
        self.client = Client(args.addr + "?WSDL", plugins=[self.history], settings=Settings(strict=False))

    def __getattr__(self, method_name):
        return lambda: self.make_request(method_name)

    def make_request(self, method_name, param={}):
        method = getattr(self, method_name, None)
        if callable(method):
            method(**param)
            xml_string = etree.tostring(self.history.last_received["envelope"], encoding="unicode", pretty_print=True)
            print(xml_string)
            return xml_string
        else:
            print(f"Method '{method_name}' not found")

    def get_all(self):
        self.client.service.GetAllBooks()

    def get_by_id(self, id):
        self.client.service.GetByID(id)

    def get_by_title(self, title):
        self.client.service.GetByTitle(title)

    def delete_book(self, id):
        self.client.service.DeleteBook(id)

    def post_book(self, id, author, title, genre, price, publish_date, description):
        book = {'id': id,
                'author': author,
                'title': title,
                'genre': genre,
                'price': price,
                'publish_date': publish_date,
                'description': description
                }
        self.client.service.PostBook(book)
