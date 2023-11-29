import math

def calculate_angle(x1, y1, x2, y2):
    angle = math.atan2(y2 - y1, x2 - x1)
    deg_angle = math.degrees(angle)
    if deg_angle < 0:
        deg_angle = 180 + abs(deg_angle)
    return deg_angle

# Пример использования функции
x1 = 0
y1 = 3
x2 = 2
y2 = 2
angle = calculate_angle(x1, y1, x2, y2)
print("Угол между точками:", angle)