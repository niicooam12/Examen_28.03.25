from Examen.lanzador import Lanzador

if __name__ == "__main__":
    # Obtener los puntos
    p1, p2, p3, p4 = lanzador.obtener_puntos()
    
    # Mostrar información
    lanzador.mostrar_coordenadas(p1, p2, p3, p4)
    lanzador.mostrar_ubicaciones(p1, p3, p4)
    lanzador.calcular_distancias(p1, p2, p3, p4)

    # Crear rectángulo y mostrar dimensiones
    lanzador.crear_rectangulo(p1, p2)
