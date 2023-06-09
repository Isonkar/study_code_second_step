'''
Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке.
Входные данные
Программа принимает на вход натуральное число N (N ≤ 103). Во второй строке через пробел идут N целых чисел, по модулю не превосходящих 103 - элементы последовательности.
Выходные данные
Ваша задача вывести заданную последовательность в обратном порядке.
Sample Input 1:
3
1 2 3
Sample Output 1:
3 2 1
'''

def print_to(n: int, lst):
    print(*reversed(lst))

print_to(n := input(), lst := list(map(int, input().split())))
