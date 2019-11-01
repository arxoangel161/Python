
# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

def permutation(a, value):
    max_value = max(a)
    if value > max_value:
        a.insert(0, value)
    elif value in a:
        a.insert(-a[::-1].index(value), value)
    else:
        a.append(value)

my_list = [7, 5, 3, 3, 2]
print(my_list)
permutation(my_list, 3)
print(my_list)
permutation(my_list, 8)
print(my_list)
permutation(my_list, 1)
print(my_list)