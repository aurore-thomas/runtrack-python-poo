# Assesseur -> get
# Mutateur -> set

class Rectangle:
    def __init__(self):
        self.__longueur = 10
        self.__largeur = 5

    def __set_rectangle(self):
        self.__longueur = 98
        self.largeur = 67

    def get_rectangle(self):
        self.__set_rectangle()

    def display(self):
        return self.__longueur, self.__largeur

rect = Rectangle()
print(rect.display())

rect.get_rectangle()
print(rect.display())






    
