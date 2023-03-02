class Personne:
    def __init__(self):
        self.age = 14

    def afficherAge(self):
        print(f"J'ai {self.age} ans")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        if age > 0:
            self.age = age
        else:
            print("L'age ne peut pas être négatif")

class Eleve(Personne):
    def __init__(self):
        Personne.__init__(self)

    def allerEnCours(self):
        print("Je vais en cours")
    
    # def afficherAge(self):
    #     return super().afficherAge()

class Professeur(Personne):
    def __init__(self, matiereEnseignee):
        Personne.__init__(self)
        self.__matiereEnseignee = matiereEnseignee
        
    def enseigner(self):
        print("Le cours va commencer")

    
eleve = Eleve()
eleve.bonjour()
eleve.allerEnCours()
eleve.modifierAge(15)
eleve.afficherAge()

professeur = Professeur("Physique")
professeur.bonjour()
professeur.enseigner()
