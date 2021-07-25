class dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"
    
    def food(self):
        return "Dog Food"

    def __str__(self):
        return "dog"


class cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Miow!"
    
    def food(self):
        return "Cat Food"

    def __str__(self):
        return "cat"


def get_pet(pet="dog"):
    """the factory method"""

    pets = dict(dog=dog("petty"), cat=cat("kitty"))
    return pets[pet]

class petfactory:
    def __init__(self, name):
        self.name = name

    def get_pet_obj(self):
        return get_pet(self.name)

    def get_food(self):
        return get_pet(self.name).food()


class petStore:
    def __init__(self, pet_factory=None):
        self._pet_factory = pet_factory

    def show_pet(self):
        pet = self._pet_factory.get_pet_obj()
        food = self._pet_factory.get_food()

        print(f"the pet is {pet} and the food is {food}, and it speaks {pet.speak()}")

dogClass = petfactory('dog')
petStore(dogClass).show_pet()

catClass = petfactory('cat')
petStore(catClass).show_pet()






