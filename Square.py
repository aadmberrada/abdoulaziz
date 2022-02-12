class Square:
    def __init__(self, cote) -> None:
        self.cote = cote

    def surface(self):
        surface = self.cote**2
        return surface
    
    def perimetre(self):
        perimetre = 4*self.cote
        return perimetre