'''Все просто, вам поступает число n - количество элементов в списке, и затем сам список.
Ваша задача отсортировать список по возрастанию при помощи пузырьковой сортировки, в случае если элементы соседние совпадают менять их ненужно.
В качестве ответа нужно вывести отсортированный список и какое количество раз пришлось переставлять элементы в процессе сортировки
Разбор
Sample Input 1:
7
8 5 3 1 4 7 9
'''

a=int(input())
b=list(map(int,input().split()))
c=0
for j in range (a-1):
    for i in range(a-1):
        if b[i]>b[i+1]:
            b[i],b[i+1]=b[i+1],b[i]
            c+=1
for d in range(a):
    print(b[d], end=' ')
print()
print(c)

#вариант два(тоже, только вывод другой)

n = int(input())
s = list(map(int, input().split()))
count = 0
for _ in range(n - 1):
    for j in range(n - 1):
        if s[j] > s[j + 1]:
            s[j], s[j + 1] = s[j + 1], s[j]
            count += 1
print(*s)
print(count)
