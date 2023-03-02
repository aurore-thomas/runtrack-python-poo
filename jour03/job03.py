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

    def ajouterTache(self, titre, description):
        self.nouvelle_tache = Tache(titre, description, "En cours")
        self.taches.append(self.nouvelle_tache)

    def supprimerTache(self, titre):
        for i in self.taches:
            if str(titre) == self.taches[i]:
               self.taches.remove(i) 

    def marquerCommeFinie(self, titre):
        for i in self.taches:
            if str(titre) == self.taches[i]:
                pass

    def afficherListe(self):
        pass
        # for tache in self.taches:
        #     print(f"{self.}")

    def filtrerListe(self):
        pass