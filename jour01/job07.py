class Personnage:
    def __init__(self):
        self.x = 0
        self.y = 0

    def gauche(self):
        self.x -= 1
        return self.x
    
    def droite(self):
        self.x += 1
        return self.x

    def bas(self):
        self.y -= 1
        return self.y
    
    def haut(self):
        self.y += 1
        return self.y
    
    def position(self):
        return (self.x, self.y)
    

p1 = Personnage()
p1.gauche()
print(p1.position())
