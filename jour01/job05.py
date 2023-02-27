class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return print("Les valeurs de x et y sont : ", self.x, "et", self.y)
    
    def afficherX(self):
        return print("La valeur de x est : ", self.x)
    
    def afficherY(self):
        return print("La valeur de y est : ", self.y)
    
    def changerX(self):
        self.x = 10
        return print("La nouvelle valeur de x est : ", self.x)
    
    def changerY(self):
        self.y = 10
        return print("La nouvelle valeur de y est : ", self.y)


Point(1, 2).afficherLesPoints()
Point(5, 4).afficherX()
Point(2, 7).afficherY()
Point(1, 9).changerX()
Point(1, 9).changerY()