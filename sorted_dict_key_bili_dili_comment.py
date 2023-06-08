'''
Дили Вили Били
Дили Вили Били завели себе аккаунты в одной известной соцсети. Их страницы стали пользоваться популярностью и, конечно же, появились поклонники, оставляющие комментарии.  
Ребята решили узнать у кого из них самое большое количество уникальных комментаторов. Ваша задача помочь им в этом и собрать нужную информацию.

Входные данные
В каждой строке будет вводиться одно из имен наших героев, а затем через двоеточие и пробел имя комментатора. Комментаторы могут повторяться и комментировать разных персонажей

Строка "конец" означает окончание ввода и встречается последней

Разбор решения Youtube Patreon Boosty

Входные данные
Ваша задача вывести в порядке уменьшения популярности 3 строки вида:
"Количество уникальных комментаторов у <имя героя> - <количество комментаторов>"
На склонение давайте не будем обращать внимание в этой задаче.

Гарантируется, что количество уникальных комментаторов у всех наших героев разное. 
Могут быть ситуации, когда у героя нету ни единого комментатора, в таком случае все равно нужно выводить информацию о нем.

Sample Input 1:

Дили: navalny
Дили: realdonaldtrump
Били: navalny
Вили: realdonaldtrump
Вили: realdonaldtrump
Били: joebiden
Дили: joebiden
конец
Sample Output 1:

Количество уникальных комментаторов у Дили - 3
Количество уникальных комментаторов у Били - 2
Количество уникальных комментаторов у Вили - 1
'''

dc = {'Дили': [], 'Били': [], 'Вили': []}

def dcomment(dcomm):
    while True:
        comm = input().split(':')
        if comm[0] == 'конец': break
        if comm[1] not in dcomm[comm[0]]:
            dcomm[comm[0]].append(comm[1])
    for k,v in dcomm.items():
        dcomm[k] = len(v)
    return dcomm


def sort_dcomment(dcomm: dict):
    for k,v in sorted(dcomm.items(), key=lambda x: -x[1]):
        print(f'Количество уникальных комментаторов у {k} - {v}')


sort_dcomment(dcomment(dc))


# var 2

blogers = {'Дили': set(), 'Били': set(), 'Вили': set()}

for s in iter(input, 'конец'):
    name, user = s.split(': ')
    blogers[name].add(user)
  
for k, v in sorted(blogers.items(), key=lambda x: -len(x[1])):
    print(f'Количество уникальных комментаторов у {k} - {len(v)}')