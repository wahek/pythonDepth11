import numpy


class Matrix:
    """Задача 3. Создайте класс Матрица.
    Добавьте методы для: - вывода на печать,
    сравнения,
    сложения,
    *умножения матриц"""

    def __init__(self, *args):
        current_len = len(args[0])
        for arg in args:
            if not isinstance(arg, (list, tuple)):
                raise TypeError('невозможно создать такую матрицу')
            if len(arg) != current_len:
                raise TypeError('невозможно создать такую матрицу, разная длинна')
        self.params = args
        self.len = current_len
        self.capacity = len(args)

    def __add__(self, other):
        if self.len == other.len and self.capacity == other.capacity:
            tuple_of_lists = tuple([list(range(self.len)) for _ in range(self.capacity)])
            for param in range(len(self.params)):
                for item in range(len(self.params[0])):
                    tuple_of_lists[param][item] = self.params[param][item] + other.params[param][item]
            return Matrix(*tuple_of_lists)

    def sum_(self):
        total = 0
        for param in self.params:
            for item in param:
                total += item
        return total

    def __eq__(self, other):
        return self.sum_() == other.sum_()

    def __ge__(self, other):
        return self.sum_() >= other.sum_()

    def __gt__(self, other):
        return self.sum_() > other.sum_()

    def __mul__(self, other):
        return Matrix(tuple(numpy.dot(self.params, other.params)))


if __name__ == '__main__':
    a = Matrix([1, 5], [1, 3])
    b = Matrix([2, 6], [3, 1])
    c = Matrix([1, 5, 4], [1, 3, 7])
    d = a + b
    print(d.params)
    print(a > b, a == b, a <= b)
    h = a * b
    print(h)
    print(h.params)
