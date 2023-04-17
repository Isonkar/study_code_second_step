'''На вход программе поступает строка, состоящая из нескольких слов, знаком разделителем между словами будем считать символ пробела. 
Ваша задача исключить из строки дублирующие слова: первое появление слова остается в строке, второе и все последующие появления исключаются. 
При сравнении на дубли строк регистр букв не учитывать, это значит слова python и PyThOn считаются одинаковыми.
В качестве ответа необходимо вывести итоговую строку без дублей.

Sample Input 1:
Python is best I love python
Sample Output 1:
Python is best I love'''

lst1 = input().split()
lst2 = []
lst3 = []

for i in lst1:
    if i.lower() not in lst2:
        lst2.append(i.lower())
        lst3.append(i)
print(*lst3)


#вариант 2 (сразу печать)
lst1 = input().split()
lst2 = []

for i in lst1:
    if i.lower() not in lst2:
        lst2.append(i.lower())
        print(i, end=' ')
