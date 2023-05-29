
'''
Напишите функцию, которая принимает имя и возраст водителя. 
Функция должна распечатать на экран заключение, может ли данный водитель управлять транспортом и определять она должна это по возрасту водителя: он должен быть больше или равен MIN_DRIVING_AGE
Если водитель может управлять, выведите фразу "<name> может водить" , в противном случае "<name> еще рано садиться за руль" 

MIN_DRIVING_AGE = 18
allowed_driving('tim', 17) # выведет "tim еще рано садиться за руль"
allowed_driving('bob', 18) # выведет "bob может водить"
'''
MIN_DRIVING_AGE = 18

def allowed_driving(name: str, age: int) -> None:
    'Функция выводит на экран заключение, может ли данный водитель управлять транспортом или нет'
    a = 'может водить'
    b = 'еще рано садиться за руль'
    print(f'{name} {a}' if age >= MIN_DRIVING_AGE else f'{name} {b}')
    
    
# var 2
'''
если внутри функции принта встречается [ вариант1, вариант2, вариант3, вариант4][тут указываем какой вариант необходимо печатать]
поскольку у нас возраст больше или равен, то выполняется ТРУ, а это один. Если фолс, то это ноль. 
'''
MIN_DRIVING_AGE = 18

def allowed_driving(name, age):
    print(name,["еще рано садиться за руль", "может водить"][age>=MIN_DRIVING_AGE])