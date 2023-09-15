'''Доработаем задания 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''
class Animal:

    def __init__(self,
                 name: str,
                 age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name, self.age


class Dog(Animal):

    def __init__(self,
                 name: str, age: int,
                 color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def __str__(self):
        return f"{self.name}, {self.age}, {self.color}, {self.voice}"


class Bird(Animal):

    def __init__(self,
                 name: str, age: int,
                 color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def __str__(self):
        return f"{self.name}, {self.age}, {self.color}, {self.voice}"


class Fish(Animal):
    def __init__(self,
                 name: str,age: int,
                 predatory: bool):
        super().__init__(name, age)
        self.predatory = predatory
        if self.predatory:
            self.predatory = "predatory"
        else:
            self.predatory = "peaceful"

    def __str__(self):
        return f"{self.name}, {self.age}, {self.predatory}"


class FabricAnimal:
    _tmp_parameters = {}

    @classmethod
    def build(cls,
              animal_type: str,
              name: str, age: int,
              color: str, voice: str,
              predatory: object = bool) -> Animal:
        cls._tmp_parameters = dict(name=name, age=age,
                                   color=color, voice=voice,
                                   predatory=predatory)
        return cls._choice(animal_type)

    @classmethod
    def _choice(cls, animal_type):
        match animal_type:
            case "Dog":
                return cls._create_dog(**cls._tmp_parameters)
            case "Bird":
                return cls._create_bird(**cls._tmp_parameters)
            case "Fish":
                return cls._create_fish(**cls._tmp_parameters)

    @classmethod
    def _create_dog(cls, name, age, color, voice, **_):
        return Dog(name=name, age=age, color=color, voice=voice)

    @classmethod
    def _create_bird(cls, name, age, color, voice, **_):
        return Dog(name=name, age=age, color=color, voice=voice)

    @classmethod
    def _create_fish(cls, name, age, predatory, **_):
        return Fish(name=name, age=age, predatory=predatory)


dog = FabricAnimal.build(animal_type="Dog", name="Джек", age=5, color="чёрно-белый", voice="лает")
print(dog)

bird = FabricAnimal.build(animal_type="Bird", name="Попугай Рома", age=2, color="голубой", voice="Рома хоррроший")
print(bird)

fish = FabricAnimal.build(animal_type="Fish", name="Без имени", age=1, color="неоновый", voice="молчат", predatory=True)
print(fish)