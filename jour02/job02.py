class Livre:
    def __init__(self):
        self.__titre = "La vie invisible d'Addie Larue"
        self.__auteur = "V.E. Schwab"
        self.__pages = 500

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

    def display(self):
        print("Titre : ", self.__titre)
        print("Auteur : ", self.__auteur)
        print("Nb de pages : ", self.__pages)

dracula = Livre()
dracula.display()

dracula.get_livre()
dracula.display()

    

    