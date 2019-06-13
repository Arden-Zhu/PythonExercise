class Cat(object):
    def __init__(self):
        self.__attr = 1

    @property
    def attr(self):
        return self.__attr

    @attr.setter
    def attr(self, value):
        self.__attr = value

def main():
    c = Cat()
    print(c.attr)
    c.attr = 3
    print(c.attr)

main()

