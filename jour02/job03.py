class Livre:
    def __init__(self):
        self.__titre = "La vie invisible d'Addie Larue"
        self.__auteur = "V.E. Schwab"
        self.__pages = 500
        self.__disponible = True

    def __set_livre(self):
        new_title = input("Quel est le nouveau livre ? ")
        new_author = input("Qui l'a écrit ? ")
        new_lenght = input("Combien de pages comporte-t-il ? ")
        self.__titre = new_title
        self.__auteur = new_author
        if int(new_lenght) <= 0:
            print("Votre livre n'a pas un nombre de pages correct")
        else:
            self.__pages = new_lenght

    def get_livre(self):
        self.__set_livre()

    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification() == True:
            self.__disponible = False
        else:
            print("Le livre n'est pas disponible !")

    def rendre(self):
        if self.verification() == False:
            self.__disponible = True
        else:
            print("Le livre a déjà été rendu !")

    def display(self):
        print("Titre : ", self.__titre)
        print("Auteur : ", self.__auteur)
        print("Nb de pages : ", self.__pages)
        print("Disponible : ", self.verification())

dracula = Livre()
dracula.emprunter()
dracula.display()
dracula.rendre()
dracula.display()
    