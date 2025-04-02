from Examen.punto import Punto
from Examen.rectangulo import Rectangulo

class Lanzador:
    def __init__(self):
        """Inicializa los puntos y ejecuta las funciones automáticamente."""
        self.p1 = Punto(2, 3)
        self.p2 = Punto(5, 5)
        self.p3 = Punto(-3, -1)
        self.p4 = Punto(0, 0)

        # Ejecutar automáticamente las funciones al instanciar
        self.ejecutar()

    def mostrar_coordenadas(self):
        print("Coordenadas de los puntos:")
        print(f"Punto 1: {self.p1}")
        print(f"Punto 2: {self.p2}")
        print(f"Punto 3: {self.p3}")
        print(f"Punto 4: {self.p4}")

    def mostrar_ubicaciones(self):
        print("\nUbicación de los puntos:")
        print(f"El punto A está en {self.p1}")
        print(f"El punto C está en {self.p3}")
        print(f"El punto D está en {self.p4}")

    def calcular_distancias(self):
        print("\nDistancia entre los puntos:")
        print(f"La distancia entre A y B es: {self.p1.distancia(self.p2)}")
        print(f"La distancia entre A y C es: {self.p1.distancia(self.p3)}")
        print(f"La distancia entre A y D es: {self.p1.distancia(self.p4)}")

        distancias = {
            "P1": self.p1.distancia(self.p4),
            "P2": self.p2.distancia(self.p4),
            "P3": self.p3.distancia(self.p4),
        }
        distancia_mas_lejana = max(distancias, key=distancias.get)
        print(f"La distancia más lejana es: {distancia_mas_lejana}")

    def crear_rectangulo(self):
        rectangulo = Rectangulo(self.p1, self.p2)
        print("\nDimensiones del rectángulo:")
        print(f"Base: {rectangulo.calcular_base()}")
        print(f"Altura: {rectangulo.calcular_altura()}")    
        print(f"Área: {rectangulo.calcular_area()}")

    def ejecutar(self):
        """Ejecuta todas las funciones automáticamente al instanciar la clase."""
        self.mostrar_coordenadas()
        self.mostrar_ubicaciones()
        self.calcular_distancias()
        self.crear_rectangulo()

if __name__ == "__main__":
    Lanzador()  # Instancia la clase y ejecuta todo
