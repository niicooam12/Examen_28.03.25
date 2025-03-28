from punto import Punto
from rectangulo import Rectangulo

p1 = Punto(2, 3)
p2 = Punto(5, 5)
p3 = Punto(-3, -1)
p4 = Punto(0, 0)

print("Coordenadas de los puntos:")
print(f"Punto 1: {p1}")
print(f"Punto 2: {p2}")
print(f"Punto 3: {p3}")
print(f"Punto 4: {p4}")

print("\n Ubicación de los puntos:")
print(f"El punto A esta en {p1}")
print(f"El punto C esta en {p3}")
print(f"El punto D esta en {p4}")

print("\n Distancia entre los puntos:")
print(f"La distancia entre A y B es: {p1.distancia(p2)}")
print(f"La distancia entre A y C es: {p1.distancia(p3)}")
print(f"La distancia entre A y D es: {p1.distancia(p4)}")

distancias = {"P1": p1.distancia(p4), "P2": p2.distancia(p4), "P3": p3.distancia(p4)}
distancia_mas_lejana = max(distancias, key=distancias.get)
print(f"La distancia mas lejana es: {distancia_mas_lejana}")

rectangulo = Rectangulo(p1, p2)

print("\n Dimensiones del rectangulo:")
print(f"Base: {rectangulo.calcular_base()}")
print(f"Altura: {rectangulo.calcular_altura()}")    
print(f"Area: {rectangulo.calcular_area()}")