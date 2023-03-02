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

class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")

    
p1 = Personne()
p1.modifierAge(50)
p1.afficherAge()

p2 = Eleve()
p2.afficherAge()
p2.modifierAge(24)
p2.afficherAge()