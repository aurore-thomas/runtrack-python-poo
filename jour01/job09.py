class Produit():
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT + (self.prixHT * self.TVA)
    
    def afficher(self):
        pass

    def ChangeName(self, nom):
        self.nom = nom

    def ChangePrice(self, prixHT):
        self.prixHT = prixHT

    def ShowName(self):
        return self.nom
    
    def ShowPrice(self):
        return self.prixHT


tomate = Produit("tomate", 2, 0.5)
aubergine = Produit("aubergine", 5, 0.3)
print(tomate.CalculerPrixTTC())
print(aubergine.CalculerPrixTTC())

tomate.ChangeName("TOMATO")
tomate.ChangePrice(24)
print(tomate.ShowName(), tomate.ShowPrice(), tomate.CalculerPrixTTC())

aubergine.ChangeName("EGGPLANT")
aubergine.ChangePrice(80)
print(aubergine.ShowName(), aubergine.ShowPrice(), aubergine.CalculerPrixTTC())