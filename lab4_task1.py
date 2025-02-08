# TODO: описать базовый класс
class Cars:

    """Создаем базовый класс Cars и задаем атрибуты класса(name)
       Атрибут name делаем непубличным для того, чтобы пользователь не менял марку автомобиля"""

    def __init__(self, name) -> str:
        self._name = name

    def __str__(self):
        return f"Автомобили {self._name}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name {self._name!r})"
# TODO: описать дочерний класс
class Passenger(Cars):

    """Создаем дочерний класс Passenger и наследуем атрибут _name"""

    def __init__(self, _name: str, maxmass: int, maxspeed: int):
        super().__init__(_name)

        """ Создаем доп. атрибуты  массы и скорости автомобиля 
            (просто обычная масса и скорость уже двигающегося автомобиля)"""
        self.maxmass = maxmass
        self.maxspeed = maxspeed

    """ Создаем метод измененния массы лег.автомобиля без всяких ограничений,
        который в последствии сможем наследовать в грузовой автомобиль.
        Если пользователь захочет изменить атрибут массы, то метод __str__ перегружается"""

    def mass(self, cargo):
        mass = self.maxmass + cargo
        return f"Автомобили {self._name}. Максимальная масса с грузом {mass}. Максимальная скорость {self.maxspeed}"

    """Создаем метод изменения скорости лег.автомобиля,
        который в последствии сможем наследовать в грузовой автомобиль.
        Если пользователь захочкет изменить атрибут скорости, то метод __str__ перегружается"""

    def speed(self, speeds):
        speed = self.maxspeed + speeds
        return f"Автомобили {self._name}. Максимальная масса {self.maxmass}. Максимальная скорость(добавление\сбавление) {speed}"

    """Перегружаем методы __str__ и __repr__, т.к. добавились новые атрибуты"""

    def __str__(self):
        return f"Автомобили {self._name}. Максимальная масса {self.maxmass}. Максимальная скорость {self.maxspeed}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name {self._name!r}, mass={self.maxmass}, maxspeed={self.maxspeed})"


class Freight(Passenger):

    """Создаем дочерний класс Freight и наследуем от класса Passenger атрибуты _name, maxmass, maxspeed,
        а также методы __str__, __repr__, mass"""

    def __init__(self, _name: str, maxmass: int, maxspeed: int):
        super().__init__(_name, maxmass, maxspeed)

    """ Перегружаем метод speed т.к. здесь по определенным причинам 
        захотелось создать ограничение скорости """

    def speed(self, speeds):
        speed = self.maxspeed + speeds
        if speed > 150:
            raise ValueError('разогнать автомобиль больше 150 км/ч нельзя')
        return f"Автомобили {self._name}. Максимальная масса {self.maxmass}. Максимальная скорость(добавление\сбавление) {speed}"

    """Поверяем возможность создания экземпляров
        атрибут name нельзя изменить пользователю"""

if __name__ == "__main__":
    # Write your solution here
    cr = Cars('Fiat')
    la = Passenger('Audi', 9, 57)
    la1 = la.mass(5)
    la2 = la.speed(-34)
    ga = Freight('BMW',20,100)
    ga1 = ga.mass(8)
    ga2 = ga.speed(50)
    print(repr(cr), cr, repr(la), la, la1, la2, repr(ga), ga, ga1, ga2, sep = "\n")