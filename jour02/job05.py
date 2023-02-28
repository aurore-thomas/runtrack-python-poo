class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50

    def __set_marque(self):
        self.__marque = input("Entrez la marque : ")

    def __set_modele(self):
        self.__modele = input("Entrez le modèle : ")

    def __set_annee(self):
        self.__annee = input("Entrez l'année : ")

    def __set_kilometrage(self):
        self.__kilometrage = input("Entrez le kilométrage : ")

    def get_marque(self):
        self.__set_marque()

    def get_modele(self):
        self.__set_modele()

    def get_annee(self):
        self.__set_annee()

    def get_kilometrage(self):
        self.__set_kilometrage()

    def demarrer(self):
        if self.verifier_plein() > 5:
            self.__en_marche = True
    
    def arreter(self):
        self.__en_marche = False

    def verifier_plein(self):
        return self.__reservoir
    
    def display(self):
        print("Modèle : ", self.__modele)
        print("Marque : ", self.__marque)
        print("Année : ", self.__annee)
        print("Kilométrage : ", self.__kilometrage)
        print("Etat : ", self.__en_marche)

p1 = Voiture("Renault", "Clio 2", 2000, 123_000)
# p1.get_voiture()

p1.demarrer()
p1.display()