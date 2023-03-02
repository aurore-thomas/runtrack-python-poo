class Forme:
    def __init__(self) -> None:
        pass
        
    def aire(self):
        return 0
    
class Rectangle(Forme):
    def __init__(self, longueur, largeur) -> None:
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur

    def aire(self):
        return(self.longueur * self.largeur)
    
p1 = Rectangle(3, 6)
print(p1.aire())