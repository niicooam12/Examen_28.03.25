import math

class Punto:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        if self.x == 0 and self.y == 0:
            return "Origen de coordenadas"
        elif self.x == 0:
            return "Estas sobre el eje Y"
        elif self.y == 0:
            return "Estas sobre el eje X"
        elif self.x > 0 and self.y > 0:
            return "Estas en el cuadrante 1"
        elif self.x < 0 and self.y > 0:
            return "Estas en el cuadrante 2"    
        elif self.x < 0 and self.y < 0:
            return "Estas en el cuadrante 3"
        elif self.x > 0 and self.y < 0:
            return "Estas en el cuadrante 4"   
        
        def diferencia(self, otro):
            return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)
        
        def distancia(self, otro):
            return math.sqrt((self.x - otro.x)**2 + (self.y - otro.y)**2)