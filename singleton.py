class borg:
    _attr_dict = {}

    def __init__(self):
        self.__dict__ = self._attr_dict


class Singleton(borg):
    def __init__(self, **kwargs):
        borg.__init__(self)
        self._attr_dict.update(kwargs)

    def __str__(self):
        return str(self._attr_dict)

x = Singleton(John="Paid")
print(f"the current version is {x}")

y = Singleton(Lucy="NOT Paid")
print(f"the current version NOW changed to {x}")


