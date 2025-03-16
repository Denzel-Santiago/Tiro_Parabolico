import matplotlib.pyplot as plt
import matplotlib.animation as animation
from core.calculations import calcular_trayectoria

class ProjectileAnimation:
    def __init__(self, proyectil):
        """
        Inicializa la animación con los datos del proyectil.
        """
        self.proyectil = proyectil
        self.tiempo, self.x_vals, self.y_vals = calcular_trayectoria(
            proyectil.x0, proyectil.y0, proyectil.velocidad_inicial, proyectil.angulo
        )
        self.fig, self.ax = plt.subplots(figsize=(10, 5))
        self.line, = self.ax.plot([], [], 'b-', label="Trayectoria", lw=2)
        self.point, = self.ax.plot([], [], 'ro', label="Punto de lanzamiento")
        self.init_axes()

    def init_axes(self):
        """
        Configura los ejes, etiquetas y título del gráfico.
        """
        self.ax.set_xlim(0, max(self.x_vals) + 10)
        self.ax.set_ylim(0, max(self.y_vals) + 10)
        self.ax.set_xlabel("Distancia en X (m)")
        self.ax.set_ylabel("Altura en Y (m)")
        self.ax.set_title("Animación de Tiro Parabólico")
        self.ax.axhline(0, color='black', linewidth=0.5)
        self.ax.axvline(0, color='black', linewidth=0.5)
        self.ax.grid()
        self.ax.legend()

    def init_animation(self):
        """
        Inicializa los elementos de la animación.
        """
        self.line.set_data([], [])
        self.point.set_data([], [])
        return self.line, self.point

    def animate(self, i):
        """
        Actualiza la posición de la línea y el punto en cada fotograma.
        """
        self.line.set_data(self.x_vals[:i], self.y_vals[:i])
        self.point.set_data([self.x_vals[i]], [self.y_vals[i]])  # Pasar listas en lugar de valores individuales
        return self.line, self.point

    def run_animation(self):
        """
        Ejecuta la animación.
        """
        ani = animation.FuncAnimation(
            self.fig, self.animate, frames=len(self.x_vals),
            init_func=self.init_animation, blit=True, interval=50
        )
        plt.show()

