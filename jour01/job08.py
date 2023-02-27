import math

class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon(self, rayon):
        self.rayon = rayon

    def afficherInfos(self, rayon):
        print("La circonférence est : ", Cercle(rayon).circonference())
        print("L'aire est : ", Cercle(rayon).aire())
        print("Le diamètre est : ", Cercle(rayon).diametre())


    def circonference(self):
        circ = 2 * self.rayon * math.pi
        return circ

    def aire(self):
        surface = (self.rayon ** 2) * math.pi
        return surface

    def diametre(self):
        dia = self.rayon * 2
        return dia

print(Cercle(4).afficherInfos(4))
print(Cercle(7).afficherInfos(7))