'''Линейный поиск, также известный как последовательный поиск, этот метод используется для поиска элемента в списке.
Линейный поиск является одним из базовых алгоритмов, с которым вы должны познакомиться, изучая программирования. 
Суть алгоритма в следующем: вы должны проверять каждый элемент списка последовательно один за другим, пока не найдете интересующий вас элемент или пока не закончится весь список.
Входные данные
Программа получает на вход в одной строке элементы списка - целые числа, разделенные пробелом. Количество элементов произвольное
И на следующей строке вводится одно число r - значение поиска
Выходные данные
Ваша задача реализовать линейный алгоритм поиска введенного значения r. В случае успеха - выведите порядковый номер(индекс) первого найденного элемента в списке при условии, что индексация начинается с единицы. 
Если данный элемент отсутствует - необходимо вывести строку ErrorValue 

Sample Input 1:
8 11 45 32 543 65
32
Sample Output 1:
4'''

lst = list(map(int, input().split()))
x = int(input())
cnt = 0
for i in range(len(lst)):
    if lst[i] == x:
        print(i + 1)
        cnt += 1
        break
if cnt == 0:
    print('ErrorValue')

#вариант второй(break and else)
lst, x = input().split(), int(input())
for i in range(len(lst)):
    if int(lst[i]) == x:
        print(i + 1)
        break
else:print('ErrorValue')