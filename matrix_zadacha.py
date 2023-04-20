'''Состязания - 2
В метании молота состязается n спортcменов. Каждый из них сделал m бросков. Победителем соревнований объявляется тот спортсмен, у которого максимален
наилучший результат по всем броскам. Таким образом, программа должна найти значение максимального элемента в данном массиве, а также его индексы (то есть номер спортсмена и номер попытки).

Входные данные

Программа получает на вход два числа n и m, являющиеся числом строк и столбцов в массиве. Далее во входном потоке идет n строк по m чисел, 
являющихся элементами массива.

Выходные данные
Программа выводит значение максимального элемента, затем номер строки и номер столбца, в котором он встречается. Если в массиве несколько максимальных элементов, 
то нужно вывести минимальный номер строки, в которой встречается такой элемент, а если в этой строке таких элементов несколько, 
то нужно вывести минимальный номер столбца. Не забудьте, что все строки и столбцы нумеруются с 0.

Sample Input 1:
3 3
3 1 2
1 3 4
3 3 3
Sample Output 1:
4
1 2
'''

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
x = 0
coords = []
for i in range(n):
    
    for j in range(m):
        if matrix[i][j] > x:
            x = matrix[i][j]
            coords.clear()
            coords.append(i)
            coords.append(j)
print(x)
print(*coords)


