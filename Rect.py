class Rectangle:
    def __init__(self, longueur, largeur) -> None:
        self.longueur = longueur
        self.largeur = largeur

    def surface(self):
        surface = self.largeur*self.longueur
        return surface
    
    def perimetre(self):
        perimetre = 2*(self.largeur + self.longueur)
        return perimetre
    
        