class Joueur:
    def __init__(self, nom, numero, position, but, passe, carton_jaune, carton_rouge):
        self.nom = nom
        self.numero = numero
        self.position = position
        self.but = but
        self.passe = passe
        self.carton_jaune = carton_jaune
        self.carton_rouge = carton_rouge

    def marquerUnBut(self):
        self.but +=1

    def effectuerUnePasseDecisive(self):
        self.passe +=1

    def recevoirUnCartonJaune(self):
        self.carton_jaune +=1
        if self.carton_jaune == 3:
            self.recevoirUnCartonRouge()

    def recevoirUnCartonRouge(self):
        self.carton_rouge +=1

    def afficherStatistiques(self):
        print(f"""Joueur : {self.nom}, Numéro : {self.numero}
    Position : {self.position}
    Buts : {self.but}, Passes décisives : {self.passe}
    Cartons jaunes : {self.carton_jaune}, Cartons rouges : {self.carton_rouge}""")


class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.liste = []

    def ajouterJoueur(self, joueur):
        self.liste.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        for joueur in self.liste:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self):
        # Méthode inutile puisque afficher le fait déjà 
        pass 

p1 = Joueur("Jean", 1, (23, 67), 2, 1, 1, 0)
p1.recevoirUnCartonRouge()
# p1.afficherStatistiques()

p2 = Joueur("Jacques", 2, (45,98), 2, 5, 0, 0)
p3 = Joueur("Jules", 3, (65, 76), 0, 0, 2, 0)

equipe = Equipe("SansNom")
equipe.ajouterJoueur(p1)
equipe.ajouterJoueur(p2)
equipe.ajouterJoueur(p3)
p3.recevoirUnCartonJaune()
equipe.AfficherStatistiquesJoueurs()