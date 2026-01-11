import datetime
users = [
    {
        'user_id': 1,
        'name': 'Alice',
        'age': 30,
    },
    {
        'user_id': 2,
        'name': 'Bob',
        'age': 25,
    }
]

print(len(users))  # Output: 2
print(users[1]['user_id'])  # Output: Alice

# речь про списки и как можно вставить несколько списков в один
my_fruit = 'apple'
other_fruit = 'banana'
new_fruit = 'lime'

all_fruits = [my_fruit, other_fruit, new_fruit]
print(all_fruits)  # Output: ['apple', 'banana', 'lime']

del all_fruits[1]
print(all_fruits)  #


happy_smiles = []  # создание пустого списка

happy_smiles.append(':)')   # добавление элемента в список
# добавление нового элемента в список. С каждым добавлением элемент добавляется в конец списка
happy_smiles.append(':D')
happy_smiles.append(':(')
happy_smiles.append(':|')
print(happy_smiles)  # Output: [':)', ':D', ':(', ':|']
print(len(happy_smiles))  # Output: 4


inputs = [True, 'Hello', 1, 3.14]
print(inputs)  # Output: [True, 'Hello', 1, 3.14]

inputs.pop()  # удаление последнего элемента из списка
print(inputs)  # Output: [True, 'Hello', 1]

inputs.pop(0)  # удаление первого элемента из списка
print(inputs)  # Output: ['Hello', 1]

# удаление первого элемента и сохранение его в переменную
removed_element = inputs.pop(0)
print(removed_element)  # Output: Hello
print(inputs)  # Output: [1]

# сортировка списка
posts_ids = [233, 444, 123, 456, 2]
posts_ids.sort()  # сортировка списка по возрастанию
print(posts_ids)  # Output: [2, 123, 233, 444, 456]
posts_ids.sort(reverse=True)  # сортировка списка по убыванию
print(posts_ids)  # Output: [456, 444, 233, 123, 2]


my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': True, 'e': 'Hello'}
my_dict_keys = list(my_dict.keys())  # получение списка ключей словаря
print(my_dict_keys)  # Output: ['a', 'b', 'c', 'd', 'e']


ratings = [2.5, 4.0, 3.5, 5.0, 4.5]

print(min(ratings))  # Output: 2.5
print(max(ratings))  # Output: 5.0
print(sum(ratings))  # Output: 19.5
ratings.sort(reverse=True)
print(ratings)  # Output: [5.0, 4.5, 4.0, 3.5, 2.5]
print(sum(ratings) / len(ratings))  # Output: 3.9 average rating


all_numbers = posts_ids + ratings
all_numbers.sort(reverse=True)
print(all_numbers)  # Output: [456, 444, 233, 123, 2, 5.0, 4.5, 4.0, 3.5, 2.5]


# нарезка списков
ratings = all_numbers
print(ratings)  # Output: [456, 444, 233, 123, 2, 5.0, 4.5, 4.0, 3.5, 2.5]
top_5 = ratings[:5]  # первые 5 элементов списка
# сортировка по возрастанию или убыванию в зависимости от True/False
top_5.sort(reverse=False)
print(top_5)  # Output: [456, 444, 233, 123, 2]
last_5 = ratings[-5:]  # последние 5 элементов списка
print(last_5)  # Output: [5.0, 4.5, 4.0, 3.5, 2.5]
middle_numbers = ratings[3:7]  # элементы с 4 по 7 (не включая 8)
print(middle_numbers)  # Output: [123, 2, 5.0, 4.5]


# копирование списков
original_list = ['a', 'b', 'c', 'd']
copied_list = original_list  # создание копии списка
copied_list.append('e')
print(copied_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# Output: ['a', 'b', 'c', 'd', 'e'] - обе переменные указывают на один и тот же список
print(original_list)
print(id(original_list)) == id(copied_list)  # Output: True
print(id(copied_list))  # разные id - разные списки


# КОПИРОВАНИЕ В НОВЫЙ СПИСОК
# вариант 1 - срез
original_list = ['a', 'b', 'c', 'd']
copied_list = original_list[:]  # создание копии списка с помощью среза
copied_list.append('e')
print(copied_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# Output: ['a', 'b', 'c', 'd'] - оригинальный список не изменился
print(original_list)
print(id(original_list) == id(copied_list))  # Output: False - разные списки


# вариант 2 - функция list()
original_list = ['a', 'b', 'c', 'd']
# создание копии списка с помощью функции list()
copied_list = list(original_list)
copied_list.append('e')
print(copied_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# Output: ['a', 'b', 'c', 'd'] - оригинальный список не изменился
print(original_list)
print(id(original_list) == id(copied_list))  # Output: False - разные списки

# вариант 3 - функция copy() из модуля copy
original_list = ['a', 'b', 'c', 'd']
# создание копии списка с помощью метода copy()
copied_list = original_list.copy()
copied_list.append('e')
original_list.clear()  # очистка оригинального списка
print(copied_list)  # Output: ['a', 'b', 'c', 'd', 'e']
# Output: ['a', 'b', 'c', 'd'] - оригинальный список не изменился
print(original_list)
print(id(original_list) == id(copied_list))  # Output: False - разные списки


five_elements = [1, 'abc', 3, True, 5]
print(five_elements)  # Output: [1, 'abc', 3, True, 5]
five_elements.pop(2)  # удаление элемента по индексу 2
print(five_elements)  # Output: [1, 'abc', True, 5]
print(len(five_elements))  # Output: 4
five_elements.reverse()  # реверс списка
print(five_elements)  # Output: [5, True, 'abc', 1

two_elements = [2, 4]
# объединение списков без создания нового списка!!
five_elements.extend(two_elements)
print(five_elements)  # Output: [5, True, 'abc', 1, 2, 4]
print(two_elements)  # Output: [2, 4] - второй список не изменился

new_list = ['x', 'y', 'z']
new_new_list = ['a', 'b', 'c']
combined_list = new_list.__add__(new_new_list)  # объединение списков
combined_list.sort()  # сортировка объединенного списка
print(combined_list)  # Output: ['x', 'y', 'z', 'a', 'b', 'c']
print(dir(combined_list))  # Output: список доступных методов для списка

# словари
my_pc = {
    'cpu': 'Ryzen 5 5600X',
    'ram': '32GB',
    'storage': '2Tb SSD',
}
# Output: {'cpu': 'Ryzen 5 5600X', 'ram': '32GB', 'storage': '2Tb SSD'}
print(my_pc)
my_pc['gpu'] = 'RTX 4060ti'  # добавление нового ключа-значения в словарь
print(my_pc)
del my_pc['ram']  # удаление ключа-значения из словаря
# Output: {'cpu': 'Ryzen 5 5600X', 'storage': '2Tb SSD', 'gpu': 'RTX 4060ti'}
print(my_pc)

time = datetime.datetime.now()
print("Current date and time: ")
print(time.strftime("%Y %H:%M"))

name = "John Pork"
emoji = True

this_slovar = {
    'time': time.strftime("%Y %H:%M"),
    'name': name,
    'emoji': emoji,
    'users': {1: 'Alice', 2: 'Bob', 3: 'John Pork'},
    'pc': my_pc,
}
# Output: {'cpu': 'Ryzen 5 5600X', 'storage': '2Tb SSD', 'gpu': 'RTX 4060ti'}
print(this_slovar['pc'])
# Функция get вернет None, если ключ не найден, а если есть, то вернет значение по ключу
# Output: 0 если ключ не найден (или можно указать другое значение по умолчанию)
print(this_slovar.get('name1', 0))


double_slovar = this_slovar.copy()
double_slovar['power'] = 147.3
print(double_slovar)  # Output: копия словаря с новым ключом 'power'
print(this_slovar)  # Output: оригинальный словарь без ключа 'power'


list1 = [[name, 'aboba'], [time.strftime("%Y %H:%M"), emoji]]
print(list1)  # Output: [[['John Pork', 'aboba'], ['2023-04-05 14:30', True]]]
list1_dict = dict(list1)
print(list1_dict)  # Output: {'John Pork': 'aboba', '2023-04-05 14:30': True}
for key, value in list1_dict.items():      # итерация по ключам и значениям словаря
    print(f"Key: {key} | Value: {value}")


# working = {}


# def keys_and_values():
#     for i in range(3):
#         key = input("Enter key: ")
#         value = input("Enter value: ")
#         working[key] = value
#     return working


# result = keys_and_values()
# working['based'] = 143.55
# print("Resulting dictionary: " + str(result))
# print("this working - " + str(working))
# del working['based']
# print("working after deletion - " + str(working))


typle = (my_pc, this_slovar)
print(typle)  # Output: кортеж из двух словарей
# изменение словаря внутри кортежа и также в оригинальной переменной
my_pc['cpu'] = 'Intel Ryzen 5600X --- modified'
print(typle)  # Output: кортеж с измененным словарем my_pc
print(my_pc)


# метода кортежа
sample_tuple = (5, 2, 9, 1, 5, 6)
# Output: 2 - количество вхождений числа 5 в кортеж
print(sample_tuple.count(5))
# Output: 2 - индекс первого вхождения числа 9 в кортеж
print(sample_tuple.index(9))


# конвертиация кортежа в список для добавления изменения и обратно
sample_typle = (1, 2, 3)
print(sample_typle)  # Output: (1, 2, 3)
temp_list = list(sample_typle)  # конвертация кортежа в список
temp_list.append(4)  # добавление элемента в список
temp_list.append(4)
temp_list.append(3)
sample_typle = tuple(temp_list)  # конвертация списка обратно в кортеж
print(sample_typle)  # Output: (1, 2, 3, 4, 4, 3)
sample_typle.index(4)  # получение индекса первого вхождения числа 4
print(sample_typle.index(4))  # Output: 3
# получение индекса второго вхождения числа 4
index_two = sample_typle.index(4, sample_typle.index(4) + 1)
print(index_two)  # Output: 4 - индекс второго вхождения числа 4


for_test_typle = ('A', True, 3.14, 42, 'B')
big_for_test_typle = for_test_typle + sample_typle
# Output: ('A', True, 3.14, 42, 'B', 1, 2, 3, 4, 4, 3)
print(big_for_test_typle)
print(big_for_test_typle.count(4))  # Output: 2 - количество вхождений числа 4


list_example = [1, 2, 2, 4, 4, 5, 5, 5, 6]
print(list_example)  # Output: [1, 2, 2, 4, 4, 5, 5, 5, 6]
# создание множества из списка для удаления дубликатов
set_example = set(list_example)
print(set_example)  # Output: {1, 2, 4, 5, 6} - дубликаты удалены

# МНОЖЕСТВА (SET)
# в наборках set можно добавлять только неизменяемые типы данных (числа, строки, кортежи)
my_set = {1, 2, ('John', 'Pork')}
print(my_set)  # Output: {1, 2, ('John', 'Pork')}
# list — можно менять
# tuple — нельзя менять
# set — без порядка и без повторов
# dict — ключи и значения
my_set2 = set()
print(my_set2)  # Output: set() - пустое множество
my_set2.add(3)  # добавление элемента в множество
my_set2.add(4)
my_set2.add(3)  # добавление дубликата не изменит множество
print(my_set2)  # Output: {3, 4} - дубликат
my_set2.remove(3)  # удаление элемента из множества
print(my_set2)  # Output: {4}

photo_size = {'1024:720', '2048:1366', '4096:2160'}
extra_size = {'800:600', '1024:720', '1024:720'}
# объединение множеств
all_sizes = photo_size.union(extra_size)
print(all_sizes)  # Output: {'2048:1366', '800:600', '4096:2160', '1024:720'}
# пересечение множеств (можно использовать & вместо метода intersection)
common_sizes = photo_size.intersection(extra_size)
print(common_sizes)  # Output: {'1024:720'}
# один набор включен в другой (можно использовать <= вместо метода issubset)


nums = {10, 22, 31}
other_nums = {10, 22, 31, 45, 50}
is_subset = nums.issubset(other_nums)
print(is_subset)  # Output: True
# можно использовать - вместо метода difference. этот метод показывает разницу между множествами
print(other_nums.difference(nums))  # print(other_nums - nums)
# Output: {45, 50} - разница между множествами
# Output: {10, 31, 50, 22, 45} - объединение множеств
print(nums | other_nums)  # .union - то же самое
big_nums = nums | other_nums
print(big_nums)  # Output: {10, 31, 50, 22, 45} - объединение множеств
# удаление элемента из множества (.discard не вызывает ошибку, если элемента нет)
# .remove можно использовать, но если элемента нет, то будет ошибка
big_nums.discard(22)
print(big_nums)  # Output: {10, 31, 50, 45}

copied_bignums = big_nums.copy()  # копирование множества
copied_bignums.add('s')  # добавление новых элементов в множество
copied_bignums.add(100)
copied_bignums.add(True)
big_nums.add(100)
big_nums.add(99)
big_nums.add(False)
big_nums.add(True)
print(copied_bignums)  # Output: {True, 100, 10, 31, 50, 's'}
print(big_nums)  # Output: {False, True, 99, 100, 10, 31, 45, 50}
# Output: {False, True, 99, 100, 10, 31, 45, 50, 's'}
print(big_nums - copied_bignums)
print(big_nums & copied_bignums)  # пересечение множеств
# элементы, которые есть в одном из множеств, но нет в обоих (.symmetric_difference)
print(big_nums.symmetric_difference(copied_bignums))
# то же самое что и выше  (.symmetric_difference)
print((big_nums | copied_bignums) - (big_nums & copied_bignums))
