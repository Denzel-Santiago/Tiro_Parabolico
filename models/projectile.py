class Projectile:
    """
    Representa un proyectil con sus propiedades iniciales.
    """
    def __init__(self, x0: float, y0: float, velocidad_inicial: float, angulo: float):
        self.x0 = x0  # Posición inicial en X
        self.y0 = y0  # Posición inicial en Y
        self.velocidad_inicial = velocidad_inicial  # Velocidad inicial
        self.angulo = angulo  # Ángulo de lanzamiento en grados
    
    def __repr__(self):
        return (f"Projectile(x0={self.x0}, y0={self.y0}, "
                f"velocidad_inicial={self.velocidad_inicial}, angulo={self.angulo})")
