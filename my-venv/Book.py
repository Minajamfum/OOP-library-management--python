class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.isAvailable = True

    @property
    def is_Available(self):
        return self.isAvailable

    @is_Available.setter
    def is_Available(self, currentStatus):
        self.isAvailable = currentStatus
