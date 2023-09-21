import time

class MyStr(str):
    """Создайте класс Моя Строка, где:
    будут доступны все возможности str
    дополнительно хранятся имя автора строки и время создания
    (time.time)
    """
    def __new__(cls, value, name:str):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time_cr = time.time()
        return instance

if __name__ == '__main__':

    mystr = MyStr('blablabla', 'ivan')
    print(mystr)
    print(mystr.name)
    print(mystr.time_cr)
    print('hhh')
