from animal import Animal


class Dog(Animal):
    cry_sound = "汪汪~"

    def __init__(self, name, kind, size, characteristic):
        super().__init__(name, kind, size, characteristic)
