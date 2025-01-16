class Trem:
    def __init__(self, num_vagoes):
        self.num_vagoes = num_vagoes

    def __iter__(self):
        for vagao in range(1, self.num_vagoes + 1):
            yield 'vagao #%s' % vagao


if __name__ == '__main__':
    for vagao in Trem(4):
        print(vagao)
