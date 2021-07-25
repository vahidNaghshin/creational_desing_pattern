class dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Woof!"

    def __str__(self):
        return "dog"


class cat:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Miow!"

    def __str__(self):
        return "cat"


def get_pet(pet="dog"):
    """the factory method"""

    pets = dict(dog=dog("petty"), cat=cat("asghar"))
    return pets[pet]


dog_pet = get_pet("dog")
print(f'This is {dog_pet}, and sounds like {dog_pet.speak()}')
cat_peg = get_pet("cat")
print(f'This is {cat_peg}, and sounds like {cat_peg.speak()}')