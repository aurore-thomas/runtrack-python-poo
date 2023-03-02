class Vehicule:
    def __init__(self, marque, annee, prix):
        self.marque = marque
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print(f"""Marque : {self.marque}
        Année : {self.annee}
        Prix : {self.prix} """)

    def demarrer(self):
        print("Attention, je roule !")

class Voiture(Vehicule):
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.portes = 4

    def informationsVehicule(self):
        print(super().informationsVehicule())
        print(f"Nombre de portes : {self.portes}")
    
    def demarrer(self):
        print("Je monte dans la voiture")
        return super().demarrer()

class Moto(Vehicule):
    def __init__(self, marque, annee, prix):
        Vehicule.__init__(self, marque, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        print (super().informationsVehicule())
        print(f"Roue = {self.roue}")

    def demarrer(self):
        print("Je monte sur la moto")
        return super().demarrer()

v1 = Voiture("Renault", 2000, 1500)
v1.informationsVehicule()
v1.demarrer()

m1 = Moto("Ducati", 1990, 20_000)
m1.informationsVehicule()
m1.demarrer()