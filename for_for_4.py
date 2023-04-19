'''Фурик очень любит уроки математики, поэтому, в отличие от Рубика, он их не посещает. Но теперь Фурик хочет получить хорошую оценку по математике. Для этого Лариса Ивановна, учительница математики, дала ему новое задание. Фурик сразу же решил эту задачу, а вы сможете?

Задана система уравнений:
 a**2 + b = n
 a + b**2 = m


Нужно посчитать количество пар целых чисел (a, b) (0 ≤ a, b), которые удовлетворяют системе.
Входные данные
В единственной строке заданы два целых числа n, m (1 ≤ n, m ≤ 1000) — параметры системы. Числа в строке разделены пробелом.
Выходные данные
В единственную строку выведите ответ на задачу.
Решение youtube patreon boosty
Sample Input 1:
9 3
Sample Output 1:
1

Sample Input 2:
14 28
Sample Output 2:
1
'''

n, m = map(int, input().split())
cnt = 0
for a in range(n):
    for b in range(m):
         if (a * a + b == n) and (a + b * b == m):
             cnt += 1
print(cnt)
