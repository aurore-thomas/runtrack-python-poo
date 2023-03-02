class Tache:
    def __init__(self, titre, description, statut):
        self.titre = titre
        self.description = description
        self.statut = statut

    def get_titre(self):
        return self.titre
    
    def get_description(self):
        return self.description
    
    def get_statut(self):
        return self.statut

    
class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for i in self.taches:
            if str(titre) == self.taches[i]:
               self.taches.remove(i) 

    def marquerCommeFinie(self, titre):
        if titre.statut == "A faire":
            titre.statut = "Terminé"

    def afficherListe(self):
        print("Liste de taches : ")
        for tache in self.taches:
            print(f"    - {tache.titre} : {tache.description}, {tache.statut}")

    def filtrerListe(self):
        self.a_faire = []
        self.termine = []
        for tache in self.taches:
            if tache.status ==  "A faire":
                self.a_faire.append(self.tache)
            elif tache.status == "Terminé":
                self.termine.append(self.tache)
        self.taches = self.a_faire + self.termine

t1 = Tache("Menage", "Laver sols", "A faire")
t2 = Tache("Jardin", "Planter tomates", "Terminé")
t3 = Tache("Linge", "Laver linge", "A faire")

l1 = ListeDeTaches()
l1.ajouterTache(t1)
l1.ajouterTache(t2)
l1.ajouterTache(t3)
l1.afficherListe()
print(l1.taches)