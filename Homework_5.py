import webbrowser
import requests

def access(func):
    """Проверяет существование url адреса и его status code

    аргументы:
    url--электронный адрес сайта
    func--функция"""
    def wrapper(url):
        try:
            print(requests.get(f'https://{url}').status_code)
            func(url)
        except:
            print(f'URl is not available')
    return wrapper


@access
def open(url):
    """Открывает сайт и указывает время запроса

     аргументы:
     url--электронный адрес сайта"""
    webbrowser.open(url)
    print(requests.get(f'https://{url}').headers['Date'])


def lib():
    """Проверяет последовательность из numb чисел на четность

    аргументы:
    numb--колличество чисел в последовательности"""
    numb=int((input('Какое колличество цифр проверить? ')))
    print(list(filter(lambda x:x%2==0,range(numb))))


if __name__=='__main__':

    open(input('Add URL: '))
    lib()