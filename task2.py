class Archives:
    """Создайте класс Архив, который хранит пару свойств.
    Например, число и строку.
    При нового экземпляра класса, старые данные из ранее
    созданных экземпляров сохраняются в пару списковархивов
    list-архивы также являются свойствами экземпляра
    """

    repository = None

    def __init__(self, intt: int, strr: str):
        self.intt = intt
        self.strr = strr

    def __new__(cls, *args, **kwargs):
        if cls.repository:
            cls.repository.old_str.append(cls.repository.strr)
            cls.repository.old_int.append(cls.repository.intt)
        else:
            cls.repository = super().__new__(cls)
            cls.repository.old_int = []
            cls.repository.old_str = []
        return cls.repository


if __name__ == '__main__':
    a = Archives(123, 'jgg')
    a2 = Archives(54, 'ujfg')
    a3 = Archives(545, 'ujggcvgvgvgfg')

    print(a2.repository.old_str)
    print(a2.repository.old_int)
    print(a.repository.old_int)
    print(a.repository.old_int)
    print(a3.repository.old_str)

