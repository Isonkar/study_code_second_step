'''
Премия Оскар
Представьте, что мы с вами сами можем решать кому и сколько статуэток Оскара уйдет (Лео бы тогда давно купался в этих статуэтках)
Ваша задача написать программу, которая находит информацию, кто из актеров получил наибольшее и наименьшее количество статуэток

Входные данные
Программа принимает на вход в первой строке натуральное число n - количество вручаемых сегодня наград. И затем в n следующих строках вводятся имена актеров - победителей.

Выходные данные
Нужно вывести в  отдельных строках имена актеров набравших наибольшее и наименьшее количество статуэток и через запятую их количество. 
Гарантируется, что всегда будет только один человек, набравший наибольшее и наименьшее количество статуэток.

Sample Input:

6
Леонардо Ди Каприо
Джонни Депп
Леонардо Ди Каприо
Леонардо Ди Каприо
Джонни Депп
Мэтт Деймон
Sample Output:

Леонардо Ди Каприо, 3
Мэтт Деймон, 1
'''

def sort_coll(persons: list):
    dict_person = dict()
    for person in persons: 
        if person not in dict_person:
            dict_person[person] = 1
        else:
            dict_person[person] += 1
    minimum = min(dict_person.items(), key=lambda x: x[1])
    maximum = max(dict_person.items(), key=lambda x: x[1])

    if len(dict_person) >= 1:
        print(*maximum, sep=', ')
        print(*minimum, sep=', ')
    else:
        for k,v in dict_person.items():
            print(f'{k}, {v}') 

persons = [input() for i in range(int(input()))]
sort_coll(persons)

#var 2

sp = [input() for _ in range(int(input()))]
d = {c + ',': sp.count(c) for c in sp}
result = sorted(d.items(), key=lambda x: x[1])
print(*result[-1])
print(*result[0])
