'''
Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и возвращает его в качестве строки

get_domain_name("http://google.com") => "google"
get_domain_name("http://google.co.jp") => "google"
get_domain_name("www.xakep.ru") => "xakep"
get_domain_name("https://youtube.com") => "youtube"
get_domain_name("https://www.asos.com") => "asos"
get_domain_name("http://www.lenovo.com") => "lenovo"
Строка url может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://, могут также содержать www.

Ваша задача написать только определение функции get_domain_name

Про инструкцию assert можно прочитать здесь

Sample Input:

Sample Output:

Проверки пройдены
'''
def get_domain_name(url):
    protocols = ['http://', 'https://', 'www.', 'https://www.', 'http://www.']
    for protocol in protocols:
        if protocol in url:
            url = url.replace(protocol, '', 1)
    return url[:url.find('.')]

# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')


# var 2
def get_domain_name(url):
    for protocol in ['http://', 'https://', 'www.', 'https://www.', 'http://www.']:
        url = url.replace(protocol, '', 1)
    print(url[:url.find('.')])

url = "https://www.mywww.com"
get_domain_name(url)
