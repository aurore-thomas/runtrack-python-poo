class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde, decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def get_numero(self):
        return self.__numero
    
    def get_nom(self):
        return self.__nom
    
    def get_prenom(self):
        return self.__prenom
    
    def get_solde(self):
        return self.__solde
    
    def afficher(self):
        print(f"Numéro de compte : {self.get_numero()}")
        print(f"Nom : {self.get_nom()}")
        print(f"Prénom : {self.get_prenom()}")

    def afficherSolde(self):
        print(f"Solde actuel : {self.get_solde()}")

    def versement(self, montant):
        self.__solde += montant

    def retrait(self, montant):
        if self.__decouvert == True:
            self.__solde -= montant
            self.agios(0.01)
        else:
            if (self.__solde - montant) > 0:
                self.__solde -= montant
            else:
                print("Retrait refusé")
        
    def agios(self, agios):
        if self.__solde < 0:
            self.__solde -= (agios * self.__solde)
            print("Agios prélevé")

    def virement(self, reference, compte, montant):
        if self.get_solde() < montant:
            print("Virement impossible, solde inférieur")
        else:
            self.__solde -= montant
            compte.versement(montant)
            print(f"Virement de référence {reference} effectué")




compte1 = CompteBancaire(1, "Aigon", "Elie", 200, True)
compte1.versement(300)
compte1.retrait(100)
compte1.afficher()
compte1.afficherSolde()

compte2 = CompteBancaire(2, "Fermaud", "Yoann", -100, True)
compte2.afficher()
compte2.afficherSolde()
compte1.virement(0, compte2, 100)
compte2.afficherSolde()
