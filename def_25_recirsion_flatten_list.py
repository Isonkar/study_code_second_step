'''
Представьте, что у нас есть список целых чисел неограниченной вложенности. 
То есть наш список может состоять из списков, внутри которых также могут быть списки. 
Ваша задача превратить все это в линейный список при помощи функции flatten

flatten([1, [2, 3, [4]], 5]) => [1, 2, 3, 4, 5]
flatten([1, [2, 3], [[2], 5], 6]) => [1, 2, 3, 2, 5, 6]
flatten([[[[9]]], [1, 2], [[8]]]) => [9, 1, 2, 8]
Ваша задача только написать определение функции flatten

Разбор Youtube Patreon Boosty
'''

def flatten(n, result=None):
    if result is None:
        result = []
    for i in n:
        if type(i) == list:
            flatten(i, result)
        else:
            result.append(i)

    return result
