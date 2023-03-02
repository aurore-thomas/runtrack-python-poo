class Ville:
    def __init__(self, name, population):
        self.__name = name
        self.__population = population
    
    def __set_population(self):
        self.__population += 1

    def get_population(self):
        return self.__set_population()
    
    def get_name(self):
        return self.__name
    
    def display(self):
        print("Nom de la ville : ", self.__name)
        print("Nombre d'habitants : ", self.__population)

class Personne:
    def __init__(self, name, age, city):
        self.__name = name
        self.__age = age
        self.__city = city
        self.ajouterPopulation()

    def ajouterPopulation(self):
        self.__city.get_population()

    def information(self):
        print("Nom de l'habitant : ", self.__name)
        print("Age de l'habitant : ", self.__age)

v1 = Ville("Paris", 1_000_000)
v2 = Ville("Marseille", 861_635)
# v1.display()
# v2.display()

p1 = Personne("John", 45, v1)
p2 = Personne("Myrtille", 4, v1)
p3 = Personne("Chloé", 18, v2)
# p1.information()
v1.display()
v2.display()


    
