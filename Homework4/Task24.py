# 4.2[24]: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, 
# причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# Всего на грядке растет N кустов. Собирающий модуль за один заход, находясь непосредственно перед 
# некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом. На входе задано количество ягод на каждом кусте.
# Не обязательно вводить их с клавиатуры, можно задать непосредственно в коде программы

# Примеры/Тесты:
# Input1: 1, 2, 3, 4, 5, 6, 7, 8
# Output1: Макс. кол-во ягод 21, собрано для куста 7

# Input1: 11, 92, 1, 42, 15, 12, 11, 81
# Output1: Макс. кол-во ягод 184, собрано для куста 1

n = int(input('Введите количество кустов: '))
lot_berry = [
    int(input(f'Введите количество ягод на {i} кусте ')) for i in range(1, n + 1)]
max_count_berry = 0
count_berry = 0
for i in range(n):
    if i == 0:
        count_berry = lot_berry[0] + lot_berry[1] + \
            lot_berry[len(lot_berry) - 1]
    elif i == len(lot_berry) - 1:
        count_berry = lot_berry[0] + \
            lot_berry[len(lot_berry) - 2] + lot_berry[len(lot_berry) - 1]
    else:
        count_berry = lot_berry[i - 1] + lot_berry[i] + lot_berry[i + 1]
    if max_count_berry < count_berry:
        max_count_berry = count_berry
        ind = i + 1
print(
    f'Максимальное количество ягод {max_count_berry}.')
print(f'Собрано для куста {ind}.')