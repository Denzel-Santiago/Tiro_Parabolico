from models.projectile import Projectile
from ui.plotter import graficar_trayectoria

def main():
    """
    Punto de entrada del programa. Solicita datos y grafica la trayectoria.
    """
    print("\n--- Simulación de Tiro Parabólico ---")
    x0 = float(input("Ingrese la posición inicial en X (m): "))
    y0 = float(input("Ingrese la posición inicial en Y (m): "))
    velocidad = float(input("Ingrese la velocidad inicial (m/s): "))
    angulo = float(input("Ingrese el ángulo de lanzamiento (grados): "))
    
    proyectil = Projectile(x0, y0, velocidad, angulo)
    graficar_trayectoria(proyectil)

if __name__ == "__main__":
    main()
