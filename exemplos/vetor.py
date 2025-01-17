import math


class Vetor:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def __repr__(self) -> str:
        return 'Vetor({}, {})'.format(self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __add__(self, vetor):
        return Vetor(self.x + vetor.x, self.y + vetor.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, n):
        return Vetor(self.x * n, self.y * n)

    def __rmul__(self, other):
        return self * other


if __name__ == '__main__':
    vetor_1 = Vetor(3, 4)
    print(vetor_1)
    print(abs(vetor_1))
    vetor_2 = Vetor(1, 1)
    print(vetor_1 + vetor_2)
    print(vetor_1)
    print(vetor_2)
    print(id(vetor_1))
    vetor_1 += vetor_2
    print(id(vetor_1))
    print(vetor_1)

    print(vetor_1 * 2)
    print(2 * vetor_1)
