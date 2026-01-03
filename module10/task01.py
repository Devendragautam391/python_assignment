class Publication:
    def __init__(self, name):
        self.name = name

class Book(Publication):
    def __init__(self, name, author, pages):
        super().__init__(name)
        self.author = author
        self.pages= pages

    def print_information(self):
        print(f"Book: {self.name}, Author: {self.author}, Pages: {self.pages}")

class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_information(self):
        print(f"Magazine: {self.name}, Chief Editor: {self.editor}")

m1 = Magazine("Donald Duck", "Aki Hyyppä")
b1 = Book("Compartment No.6", "Rosa Liksom", 192)

m1.print_information()
b1.print_information()
