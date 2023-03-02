class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def __set_longueur(self):
        self.__longueur = int(input("Nouvelle longueur ? "))

    def get_longueur(self):
        return self.__set_longueur()
    
    def __set_largeur(self):
        self.__largeur = int(input("Nouvelle largeur ? "))

    def get_largeur(self):
        return self.__set_largeur()

    def perimetre(self):
        perimetre = (2*self.__longueur) + (2*self.__largeur)
        print(f"Le périmètre est de {perimetre} mètres")

    def surface(self):
        aire = self.__longueur * self.__largeur
        print(f"L'aire est de {aire} m²")
        return aire

class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        volume = self.surface() * self.__hauteur
        print(f"Le volume est de {volume} mètres cube")
    

# rectangle = Rectangle(6, 9)
# rectangle.perimetre()
# rectangle.get_largeur()
# rectangle.surface()

pave_droit = Parallélépipède(2, 6, 3)
pave_droit.volume()