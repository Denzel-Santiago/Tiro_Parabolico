import math
from core.config import G

def calcular_componentes_velocidad(velocidad_inicial, angulo):
    """
    Calcula las componentes de la velocidad inicial en X y Y.
    """
    angulo_rad = math.radians(angulo)
    vx = velocidad_inicial * math.cos(angulo_rad)
    vy = velocidad_inicial * math.sin(angulo_rad)
    return vx, vy

def calcular_altura_maxima(vy):
    """
    Calcula la altura máxima alcanzada por el proyectil.
    """
    return (vy ** 2) / (2 * G)

def calcular_tiempo_altura_maxima(vy):
    """
    Calcula el tiempo para alcanzar la altura máxima.
    """
    return vy / G

def calcular_tiempo_total_vuelo(vy, y0):
    """
    Calcula el tiempo total de vuelo hasta que el proyectil toque el suelo.
    """
    t_subida = calcular_tiempo_altura_maxima(vy)
    t_caida = math.sqrt((2 * (y0 + calcular_altura_maxima(vy))) / G)
    return t_subida + t_caida

def calcular_distancia_x(vx, tiempo_total):
    """
    Calcula la distancia total recorrida en X.
    """
    return vx * tiempo_total

def calcular_trayectoria(x0, y0, v0, angulo, num_pasos=100):
    """
    Genera la trayectoria del proyectil en intervalos de tiempo.
    """
    vx, vy = calcular_componentes_velocidad(v0, angulo)
    t_total = calcular_tiempo_total_vuelo(vy, y0)
    
    tiempo = [t_total * i / num_pasos for i in range(num_pasos + 1)]
    x = [x0 + vx * t for t in tiempo]
    y = [y0 + vy * t - 0.5 * G * t**2 for t in tiempo]
    
    return tiempo, x, y
