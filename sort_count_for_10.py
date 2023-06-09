'''Рассмотрим ещё одну задачу, где дана строка и нужно подсчитать сколько раз каждая буква встречалась в строке. 
При этом не имеет разницы большая буква или нет.

s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
Создадим список из такого же числа нулей, как и букв в английском алфавите:

letters = [0] * 26
И здесь на нулевой позиции подсчитываем количество раз, когда встретилась буква a, на первой позиции – буква b и т.д. 
Для того, чтобы убрать разницу между большими и маленькими буквами воспользуемся методом lower(), а так же отсечём
условным оператором все символы, которые не являются буквами.
Код будет иметь вид:

Этот код позволит вывести все те символы из строки, которые нам нужны. Нам осталось только установить соответствие: a = 0, b = 1 и т.д.
Для этого нужно воспользоваться функцией ord, которая принимает символ и возвращает его порядковый номер в кодировке ASCII. 
Для проверки в каком диапазоне находятся наши символы мы можем ввести в эту функцию по очереди крайние наши символы:

Получается, что наши символы букв имеют коды от 97 до 122, а индексы списка лежат в пределах от 0 до 25

В итоге, чтобы получить нужные нам значения, нужно отнимать от получившихся значения число 97 (ord("a") = 97, чтобы получить 0 необходимо 97-97, ord("z") = 122, 
чтобы получить 25 необходимо 122-97).
В итоге наш код будет иметь следующий вид:

При выводе мы видим не буквы, а номера из-за того, что мы подстроили каждую букву под номер индекса. Теперь ввернём буквы, для этого 
существует схожая с ord() функция – chr(), которая из определенного номера выводит его символ в ASCII, стоит так же не забывать, что мы отнимали 97, 
так что мы теперь должны прибавить это число. 
В итоге наш код будет следующим:

Обратите внимание, что в этой задаче мы использовали смещение (сначала мы в ord() отнимали 97, а потом делали обратную операцию 
другим смещением - в chr() прибавляли 97).
'''

s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(i, letters[i])
        
        
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i+97), letters[i])

        
s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
letters = [0] * 26
for i in s.lower():
    if i >= "a" and i <= "z":
        nomer = ord(i) - 97
        letters[nomer] += 1
for i in range(26):
    if letters[i] > 0:
        print(chr(i+97) * letters[i], end="")
