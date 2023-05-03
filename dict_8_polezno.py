'''Подсчет количества объектов'''


'''
Пример подсчёта количества элементов в строке: подсчитаем сколько раз встретилась каждая буква в строке.
'''

s = input('Введите строку! Подсчитваем ее буквы: ')
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)
for letter, count in d.items():
    print(letter, count)
    
'''
В данном алгоритме если в нашем словаре есть уже такой элемент, то мы увеличиваем счётчик на 1, а если этого элемента не было, 
то мы создавали его как ключ и ставим счётчик на 1 (поскольку это его первое появление)

Давайте оптимизируем:

при помощи метода isalpha() у строк оставим только буквы, тем самым исключим числа и знаки препинания
вспомним о методе get у словаря: с помощью метода get() можно получить значение, которое лежало по данному ключу, а в случае, 
если ключа не было, возвращается 0 и добавляем единицу
В итоге получим такой код
'''

s = input('Введите строку! Подсчитваем ее буквы: ')
d = {}
for i in s:
     if i.isalpha():
        d[i] = d.get(i, 0) + 1
print(d)
for letter, count in d.items():
    print(letter, count)
    
    

'''
Словари помогают установить соответствие между объектами
'''

words = {}
while True:
  s = input('Введите английское слово: ')
  if s in words:
      print("Слово", s, 'переводится как', words[s])
  else:
      print("Введите перевод слова", s)
      words[s] = input()
      
'''
В итоге мы вводим слово, если оно есть в словаре, то мы выводим значение по заданному ключу (перевод слова), если же такого ключа нет, 
то мы просим ввести перевод и добавляем в словарь пару ключ-значение
'''


