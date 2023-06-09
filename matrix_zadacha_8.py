'''Манао работает на спортивном телевидении. Он долгое время наблюдал за футбольными матчами чемпионата одной страны и начал замечать разные закономерности. 
Например, у каждой команды есть две формы: домашняя и выездная. Когда команда проводит матч на своем стадионе, футболисты надевают домашнюю форму, 
а когда на чужом — выездную. Единственное исключение из этого правила — когда цвет домашней формы принимающей команды совпадает с цветом формы гостей. В таком случае домашняя команда облачается в свою выездную форму. Цвета домашней и выездной формы для каждой команды различны.

В чемпионате страны участвует n команд и он состоит из n·(n - 1) матчей: каждая из команд принимает каждую другую команду на своем стадионе. 
Манао задумался, а сколько раз в течение одного чемпионата случится, что команда, играющая на своем стадионе, оденет выездную форму? Обратите внимание, 
что для подсчета этого количества порядок матчей не играет никакого значения.

Вам даны цвета домашней и выездной формы каждой команды. Для удобства эти цвета пронумерованы целыми числами таким образом, что никакие два разных цвета 
не имеют одинаковый номер. Помогите Манао найти ответ на его вопрос.

Входные данные
В первой строке содержится целое число n (2 ≤ n ≤ 30). В каждой из следующих n строк записана пара разделенных одним пробелом различных 
целых чисел hi, ai (1 ≤ hi, ai ≤ 100) — номер цвета домашней и выездной форм i-ой команды соответственно.

Выходные данные
В единственной строке выведите количество матчей, в которых домашняя команда выступит в выездной форме.

Разбор задачи Youtube Patreon Boosty

Sample Input 1:

3
1 2
2 4
3 4
Sample Output 1:

1
Sample Input 2:

4
100 42
42 100
5 42
100 5
Sample Output 2:

5
'''

n=int(input())
a = [list(map(int, input().split())) for i in range(n)]
count=0
for i in range(n):
    for j in range(n):
        if a[i][0]==a[j][1]:
            count+=1
print(count)

#вариант два

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

lst_1 = []
lst_2 = []

for i in range(n):
    lst_1.append(matrix[i][0])
    lst_2.append(matrix[i][1])

k = 0

for i in lst_1:
    k += lst_2.count(i)
     
print(k)


#вариант три

x=' '.join([input() for _ in ' '*int(input())]).split()
print(sum(x[::2].count(i) for i in x[1::2]))
