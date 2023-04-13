"""Мишка — маленький белый медвежонок. А как известно, маленькие медвежата в свободное время любят играть в кости на шоколадки. 
Одним замечательным солнечным утром, гуляя по льдинам, Мишка встретил своего друга Криса, которому и предложил сыграть в эту занимательную игру.
Правила её очень просты: сначала определяется значение n — количество раундов игры. 
В очередном раунде каждый из игроков один раз бросает стандартный игральный кубик, на грани которого нанесены различные числа от 1 до 6. 
Игрок, выбросивший большее значение, становится победителем в раунде. В случае, если выпавшие значения равны, победа не засчитывается никому.

В самой же игре побеждает участник, выигравший в большем количестве раундов. Если же количества побед, заслуженных игроками, равны, то объявляется ничья.
Мишка ещё совсем маленький и плохо умеет вести счёт, а потому попросил Вас понаблюдать за ходом игры и сообщить ему результат.
Входные данные
В первой строке входных данных содержится число n (1 ≤ n ≤ 100) — количество раундов игры.
Следующие n строк содержат описание раундов. В i-й из них содержится пара целых чисел mi и ci (1 ≤ mi,  ci ≤ 6) — результаты бросков Мишки и Криса в i-ом раунде соответственно.
Выходные данные
В случае победы Мишки в единственной строке выведите "Mishka" (без кавычек), а в случае победы Криса выведите "Chris" (без кавычек). Если же игра сведётся к ничьей, то выведите "Friendship is magic!^^" (без кавычек).
PS: генерировать случайные числа(пользоваться модулем random) вам не нужно, данные для игры уже готовы. Вам нужно только их считать,  и узнать кто же победил
Sample Input 1:

3
3 5
2 1
4 2
Sample Output 1:

Mishka
"""
cnt_m = 0
cnt_c = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    if a > b:
        cnt_m += 1
    elif a == b:
        cnt_m += 1
        cnt_c += 1
    else:
        cnt_c += 1

if cnt_m > cnt_c:
    print('Mishka')
elif cnt_m == cnt_c:
    print('Friendship is magic!^^')
else:
    print('Chris')
    
    
    
    
#вариант второй
n = int(input())

x = y = 0
for _ in range(n): 
    a, b = input().split()
    x += int(a > b)
    y += int(a < b)

print('Mishka' if x > y else 'Chris' if x < y else 'Friendship is magic!^^')

#вариант три
score = 0
for _ in range(int(input())):
    m, k = map(int, input().split())
    score += (m > k) - (m < k)
print(('Friendship is magic!^^', 'Mishka', 'Chris')[(score > 0) - (score < 0)])
