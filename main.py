from models.projectile import Projectile
from ui.plotter import graficar_trayectoria
from ui.animation import ProjectileAnimation

def main():
    """
    Punto de entrada del programa. Solicita datos y permite elegir entre graficar o animar.
    """
    print("\n--- Simulación de Tiro Parabólico ---")
    x0 = float(input("Ingrese la posición inicial en X (m): "))
    y0 = float(input("Ingrese la posición inicial en Y (m): "))
    velocidad = float(input("Ingrese la velocidad inicial (m/s): "))
    angulo = float(input("Ingrese el ángulo de lanzamiento (grados): "))

    proyectil = Projectile(x0, y0, velocidad, angulo)

    print("\n¿Qué deseas hacer?")
    print("1. Graficar la trayectoria")
    print("2. Ver animación")
    opcion = input("Selecciona una opción (1 o 2): ")

    if opcion == "1":
        graficar_trayectoria(proyectil)
    elif opcion == "2":
        animator = ProjectileAnimation(proyectil)
        animator.run_animation()
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()