'''
Напишите функцию file_read, которая принимает имя файла, и печатает его содержимое.

Учитывайте, что содержимое файла может быть как на русском языке, так и на английском
'''

def file_read(file_name: str) -> None:
    my_file = open(file_name, encoding='utf-8')
    print(my_file.read())
