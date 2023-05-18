'''
Шифр цезаря
На основании предыдущей задачи мы с вами можем реализовать знаменитый шифр Цезаря. 
Этот шифр брал каждую букву исходной фразы и смещал ее на значение ключа, это так раз был на сдвиг. 
В пределах кодирования одной фразы значение сдвига всегда постоянно.
И так, ваша задача создать функцию caesar_cipher , которая принимает на вход текст и значение сдвига.

Внутри функции caesar_cipher  необходимо последовательно пройтись по каждому символу и преобразовать его по следующим правилам:
если символ является знаком пунктуации, оставляем его как есть
если это буква, то сместить ее при помощи ранее написанной функции shift_letter 
Закодированный текст необходимо вернуть в качестве ответа. Вот пример работы

caesar_cipher('leave out all the rest', -1) => 'kdzud nts zkk sgd qdrs'
caesar_cipher('one more light', 3) => 'rqh pruh oljkw'
Аннотации, мой друг, не забываем прописывать. И еще нужно сделать док-строку для функции caesar_cipher со значением «Шифр цезаря»

Нужно написать только определение функций shift_letter и caesar_cipher 
Sample Input 1:
lost in the echo
27
Sample Output 1:
mptu jo uif fdip
'''

def shift_letter(letter: str, shift: int) -> str:
    'Функция сдвигает символ letter на shift позиций'  
    return chr((ord(letter) - ord('a') + shift) % 26 + 97)

def caesar_cipher(letter: str, shift: int) -> str:
    'Шифр цезаря'
    res = ''
    for word in letter.split():
        for letter in word:
            if letter.isalpha():
                res += shift_letter(letter, shift)
            else:
                res += letter
        res += ' '
    return res
