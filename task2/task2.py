import sys
import math

# Аргументы: файл1(circle) и файл2(points)
if len(sys.argv) != 3:
    print("Надо ввести путь к двум файлам как аргументы")
    sys.exit(1)

file1 = sys.argv[1]
file2 = sys.argv[2]

# Центр с радусом
with open(file1, 'r') as f:
    lines = f.readlines()
    center_x = float(lines[0].strip())  # тут x
    center_y = float(lines[1].strip())  # тут y
    radius = float(lines[2].strip())    # тут r

# Читаем точки
with open(file2, 'r') as f:
    points = f.readlines()

for point in points:
    coords = point.strip().split()
    if len(coords) != 2:
        continue
    
    px = float(coords[0])
    py = float(coords[1])
    
    dist = math.sqrt( (px - center_x)**2 + (py - center_y)**2 )
    
    if abs(dist - radius) < 1e-6:
        print(0)  # На окружности
    elif dist < radius:
        print(1)  # Внутри круга
    else:
        print(2)  # Снаружи круга
