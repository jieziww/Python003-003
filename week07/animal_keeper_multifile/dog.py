from animal import Animal


class Dog(Animal):
    crysound = "汪汪~"

    def __init__(self, name, kind, size, characteristic):
        super().__init__(name, kind, size, characteristic)
