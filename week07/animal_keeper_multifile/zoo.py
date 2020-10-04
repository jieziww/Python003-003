from animal import Animal


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        if animal not in self.animals:
            self.animals.append(animal)
            setattr(self, animal.__class__.__name__, 'yes')
        else:
            print(f'已经有{animal.name}了，同一只动物不能重复添加！')
