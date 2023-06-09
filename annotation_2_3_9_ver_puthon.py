'''Аннотации в новых версиях python (python >=3.9)
Начиная с версии python3.9 был реализован стандарт, который позволил не пользоваться модулем typing для аннотирования. 
Теперь вы можете сразу указывать вложенные типы и не нужно импортировать типы из модуля typing

 Замена Union
Вместо слова Union и оформления кода следующим образом 

param: Union[int, float, str] = 3
начиная с версии python3.9, мы теперь можем написать вот так

param: int | float | str = 3
 

При помощи оператора | мы можем объединять несколько типов в аннотации

Замена Optional
Вместо слова Optional и оформления кода следующим образом 

from typing import Optional

num: Optional[int] = None
word: Optional[str] = None
начиная с версии python3.9, мы теперь можем написать вот так


num: int | None = None
word: str | None = None
Аннотация элементов списков и множеств
Вместо записи 

from typing import List

words: List[str] = ["hello", "world"]
начиная с версии python3.9, мы теперь можем написать вот так


words: list[str] = ["hello", "world"]
Аннотация словарей
Вместо записи

from typing import Dict
person: Dict[str, str] = { "first_name": "John", "last_name": "Doe"}
начиная с версии python3.9, мы теперь можем написать вот так

person: dict[str, str] = { "first_name": "John", "last_name": "Doe"}
Вместо

from typing import Dict, Optional, Union

def foo(bar: Dict[Union[str, int], Optional[str]]) -> bool:
   return True
Мы можем написать


def foo(bar: dict[str | int, str | None]) -> bool:
   return True
   '''
