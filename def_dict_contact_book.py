'''
Телефонная книга
Петя очень популярный парень, у него много друзей и он хочет сохранить их контакты в телефонной книге. Известно, что у каждого друга может быть один или больше номеров телефонов. 
Напишите программу, которая поможет Пете находить все номера определённого друга.

Формат ввода
В первой строке задано одно целое число N (1 ≤ N ≤ 1000) — количество номеров телефонов, информацию о которых Петя  решил сохранить в телефонной книге. 
В следующих N строках заданы телефоны и имена их владельцев через пробел. Телефон — это несколько цифр, записанных подряд, имя же состоит только из русских букв. Записи не повторяются.

В следующей строке записано целое число M (1 ≤ M ≤ 100) — количество запросов от Пети. В следующих M строках записаны сами запросы, по одному на строке. 
Каждый запрос — это имя какого-то друга, чьи телефоны Петя хочет сейчас найти, записанное в точности так, как в телефонной книге.

Формат вывода
Для каждого запроса от Пети выведите в отдельной строке все телефоны, принадлежащие человеку с этим именем. 
Телефоны одного человека выводите в одну строку через пробел в том порядке, в котором они были заданы во входных данных.

Если в телефонной книге нет телефонов человека с таким именем, выведите в соответствующей строке «Неизвестный номер» (без кавычек).

Sample Input:

3
444444 Женя
79129874521 Женя
79604845827 Оля
3
Оля
Олег
Женя
Sample Output:

79604845827
Неизвестный номер
444444 79129874521
'''

contact_book = dict()

def add_contact():
    n = int(input())
    for i in range(n):
        contact = list(input().split())
        if contact[1] not in contact_book:
            contact_book[contact[1]] = [int(contact[0])]
        else: contact_book[contact[1]].append(int(contact[0]))
    return contact_book
          


def request_contact(contact_book: dict):
    n = int(input())
    for i in range(n):
        request = input()
        if request not in contact_book.keys():
            print("Неизвестный номер")
        else:
            for name, number in contact_book.items():
                if name == request:
                    print(*number)
                
            
              

request_contact(add_contact())


# var 2

phone_book = {}

for _ in range(int(input())):
    phone, name = input().split()
    phone_book.setdefault(name, []).append(phone)

for _ in range(int(input())):
    name = input()
    print(*phone_book.get(name, ['Неизвестный номер']))