from punto import Punto

class Rectangulo:
    def __init__(self, coord1=Punto(), coord2=Punto()):
        self.coord1 = coord1
        self.coord2 = coord2

    def calcular_base(self):
        return abs(self.coord1.x - self.coord2.x)
    
    def calcular_altura(self):
        return abs(self.coord1.y - self.coord2.y)
    
    def calcular_area(self):
        return self.calcular_base() * self.calcular_altura()    