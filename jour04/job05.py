import math

class Forme:
    def __init__(self) -> None:
        pass
        
    def aire(self):
        return 0
    
class Cercle(Forme):
    def __init__(self, rayon):
        Forme.__init__(self)
        self.rayon = rayon

    def aire(self):
        return((self.rayon **2) * math.pi)
    
c1 = Cercle(5)
print(c1.aire())