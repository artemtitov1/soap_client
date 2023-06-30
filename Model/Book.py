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
