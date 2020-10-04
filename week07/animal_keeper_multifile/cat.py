from animal import Animal


class Cat(Animal):
    cry_sound = "喵喵~"

    def __init__(self, name, kind, size, characteristic):
        super().__init__(name, kind, size, characteristic)
