'''
Ваша задача написать функцию find_duplicate, которая принимает один аргумент - список чисел. 
Функция должна возвращать список из дублей, каждый дубль нужно брать только один раз в том порядке, в котором они встречаются в исходном списке. 
Под дублем будем подразумевать число, которое присутствовало в списке несколько раз. 

find_duplicate([1, 1, 1, 1, 1, 2, 2, 2, 2]) => [1, 2]
find_duplicate([2, 1, 1, 1, 1, 1, 2, 2, 2, 2]) => [2, 1]
find_duplicate([1, 2, 3, 4]) => []
find_duplicate([1, 2, 3, 4, 3]) => [3]
Ваша задача написать только определение функции find_duplicate

Про инструкцию assert можно прочитать здесь

Разбор Youtube Boosty Patreon

Sample Input:

Sample Output:

Все успешно
'''

def find_dublicate(lst):
    res_list = []
    for i in lst:
        if lst.count(i) > 1 and i not in res_list:
            res_list.append(i)
    
    return res_list

print(find_dublicate([8, 7, 6, 5, 4, 3, 4, 5, 6, 7, 8]))

# var 2

def find_duplicate(n):
    b = []
    [b.append(i) for i in n if i not in b and n.count(i) > 1]
    return(b)
