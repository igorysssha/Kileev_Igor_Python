import sys

# Вводим аргументы
if len(sys.argv) == 3:
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Аргументы n и m должны быть целыми числами")
        sys.exit(1)
else:
    while True:
        try:
            n = int(input("Введите n: ").strip())
            m = int(input("Введите m: ").strip())
            break
        except ValueError:
            print("Пожалуйста введите целые числа для n и m.")
# Круговой массив
circle = list(range(1, n+1))

path = [] 
current_pos = 0 

while True:
    start = circle[current_pos]
    path.append(start)
    
    if start == 1 and len(path) > 1:
        break
    
    current_pos = (current_pos + m - 1) % n

# Выводим путь без пробелов
print(''.join(map(str, path)))
