'''Программа получает на вход число n - количество элементов в списке, и затем в следующей строке сам список.
Ваша задача отсортировать список по возрастанию при помощи сортировки вставками, в случае если элементы соседние совпадают менять их ненужно.
В качестве ответа нужно вывести отсортированный список.
Sample Input 1:
6
5 4 2 15 6 6
Sample Output 1:
2 4 5 6 6 15
'''

n = int(input())
lst_in = list(map(int, input().split()))


for i in range(n):
    for j in range(i + 1, n):
      if  lst_in[j] < lst_in[i]:
          lst_in[i], lst_in[j] = lst_in[j], lst_in[i]

print(*lst_in)


