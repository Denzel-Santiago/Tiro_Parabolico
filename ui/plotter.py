import matplotlib.pyplot as plt 
from core.calculations import calcular_trayectoria

def graficar_trayectoria(proyectil):
    """
    Grafica la trayectoria del proyectil.
    """
    tiempo, x, y = calcular_trayectoria(proyectil.x0, proyectil.y0, proyectil.velocidad_inicial, proyectil.angulo)
    
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, label="Trayectoria", color='b')
    plt.scatter([proyectil.x0], [proyectil.y0], color='r', label="Punto de lanzamiento")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlabel("Distancia en X (m)")
    plt.ylabel("Altura en Y (m)")
    plt.title("Trayectoria del proyectil")
    plt.legend()
    plt.grid()
    plt.show()
