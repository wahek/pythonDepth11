class Figure:
    """Дорабатываем класс прямоугольник из прошлого семинара.
    Добавьте возможность сложения и вычитания.
    При этом должен создаваться новый экземпляр
    прямоугольника.
    Складываем и вычитаем периметры, а не длинну и ширину.
    При вычитании не допускайте отрицательных значений.
    Дорабатываем класс прямоугольник из прошлого семинара.
    Добавьте возможность сложения и вычитания.
    При этом должен создаваться новый экземпляр
    прямоугольника.
    Складываем и вычитаем периметры, а не длинну и ширину.
    При вычитании не допускайте отрицательных значений.
    """

    def __init__(self, length_1, length_2=0):
        self.length_1 = length_1
        self.length_2 = length_1 if length_2 == 0 else length_2

    def calc_len(self):
        return (self.length_1 + self.length_2) * 2

    def calc_area(self):
        return self.length_1 * self.length_2

    def __add__(self, other):
        return Figure((self.calc_area() + other.calc_area()) / self.length_2, self.length_2)

    def __sub__(self, other):
        return Figure(abs(self.calc_area() - other.calc_area()) / self.length_2, self.length_2)

    def __eq__(self, other):
        return self.calc_area() == other.calc_area()

    def __gt__(self, other):
        return self.calc_area() > other.calc_area()

    def __ge__(self, other):
        return self.calc_area() >= other.calc_area()


if __name__ == '__main__':
    b = Figure(12, 14)
    a = Figure(10, 6)
    c = a + b
    d = b - a
    print(b.calc_area())
    print(a.calc_area())
    print(c.length_1)
    print(c.calc_area())
    print(d.calc_area())
    print(d.length_1, d.length_2)
    print(a > c)
    print(b < a)
    print(b > a)
