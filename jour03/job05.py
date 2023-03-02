class Personnage:
    def __init__(self, nom, pv):
        self.nom = nom
        self.pv = pv

    def get_name(self):
        return self.nom
    
    def get_pv(self):
        return self.pv

    def attaquer(self, cible):
        pv_lost = cible.get_pv()
        





