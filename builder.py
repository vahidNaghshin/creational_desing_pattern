class director():
    def __init__(self, name):
        self.name = name

    def get_car_without_horn(self):
        #one config
        self.name.get_car()
        self.name.add_model()
        self.name.add_engine()
        self.name.add_tire()

    def get_car_with_horn(self):
        #another config
        self.name.get_car()
        self.name.add_model()
        self.name.add_engine()
        self.name.add_tire()
        self.name.add_horn()

    def get_car(self):
        return self.name.car

class builder():
    # generate the class car and hand it over to engine_builder
    def __init__(self, car=None):
        self.car = car

    def get_car(self):
        self.car = car()


class engin_builder(builder):
    # this initialise the attributes of the class
    def add_model(self):
        self.car.model = 'Toyota'

    def add_engine(self):
        self.car.engine = "V8"

    def add_tire(self):
        self.car.tire = 'Bridgestone'
    
    def add_horn(self):
        self.car.horn = 'Air Horn'


class car():
    # this is the core class to be initialised
    def __init__(self):
        self.model = None
        self.engine = None
        self.tire = None
        self.horn = None

    def __str__(self):
        if self.horn:
            return f"this is model:{self.model}, enine:{self.engine}, tire:{self.tire} with horn {self.horn}"
        else:
            return f"this is model:{self.model}, enine:{self.engine}, tire:{self.tire} with no horn"

car_obj = car()
carBuilder = engin_builder(car_obj)
build_car = director(carBuilder)
build_car.get_car_without_horn()
car_built = build_car.get_car()
print(car_built)

car_obj_horn = car()
carBuilder = engin_builder(car_obj_horn)
build_car = director(carBuilder)
build_car.get_car_with_horn()
car_built = build_car.get_car()
print(car_built)