'''Сумма строк и столбцов двумерного массива 
Задан целочисленный двумерный массив, состоящий из N строк и M столбцов. Требуется вычислить сумму элементов в каждой строке и в каждом столбце.
Программа получает на вход два натуральных числа N и M – количество строк и столбцов двумерного массива. 
В каждой из последующих N строк записаны M целых чисел – элементы массива. Все числа во входных данных не превышают 1000 по абсолютной величине.
В первой строке вам необходимо вывести N чисел – суммы элементов массива для каждой строки в отдельности.
Во второй строке в аналогичном формате выведите M чисел – суммы элементов для каждого столбца.

Sample Input 1:

3 4
5 9 2 6
6 2 4 3
1 2 8 7
Sample Output 1:

22 15 18
12 13 14 16
'''

n, m = map(int, input().split())
matrix = [(list(map(int, input().split()))) for _ in range(n)]

sum_row = 0
sum_col = 0

for i in range(n):
    for j in range(m):
        sum_row += matrix[i][j]
    print(sum_row, end=' ')
    sum_row = 0

print()

for j in range(m):
    for i in range(n):
        sum_col += matrix[i][j]
    print(sum_col, end=' ')
    sum_col = 0

    
    
#вариант два
n,m=map(int,input().split())
s=[list(map(int,input().split())) for i in range(n)]

print(*[sum(s[i][j] for j in range(m)) for i in range(n)])
print(*[sum(s[i][j] for i in range(n)) for j in range(m)])
