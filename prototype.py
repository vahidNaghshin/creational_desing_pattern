import copy

class prototype:
    
    def __init__(self):
        self.obj_dict = {}

    def register_class(self, name, obj):
        self.obj_dict[name] = obj

    def unregister_class(self, name):
        del self.obj_dict[name]

    def clone(self, name, **attr):
        obj_aux = copy.deepcopy(self.obj_dict.get(name))
        obj_aux.__dict__.update(attr)

        return obj_aux


class car:

    def __init__(self):
        self.name = 'skyrocket'
        self.color = 'red'
        self.option = 'tuned'

    def __str__(self):
        return 'The obj attributes {} | {} | {}'.format(self.name, self.color, self.option)

car = car()
proto_1 = prototype()
proto_1.register_class('skyrocket', car)
car_cloned = proto_1.clone('skyrocket', color='red', option='tuned')
print(car_cloned)
