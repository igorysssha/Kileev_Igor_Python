import sys

# Аргумент: путь к файлу с nums
if len(sys.argv) != 2:
    print("Нужен файл с nums")
    sys.exit(1)

file_path = sys.argv[1]

# Читаем nums
with open(file_path, 'r') as f:
    lines = f.readlines()
nums = [int(line.strip()) for line in lines if line.strip()]

n = len(nums)
if n == 0:
    print(0)
    sys.exit(0)

if n == 1:
    print(0)
    sys.exit(0)

# Находим min и max для перебора
min_val = min(nums)
max_val = max(nums)

# Больший минимум
min_moves = float('inf')

# Ищем минимальное количество ходов
for k in range(min_val, max_val + 1):
    moves = 0
    for num in nums:
        moves += abs(num - k)
    if moves < min_moves:
        min_moves = moves

print(min_moves)
