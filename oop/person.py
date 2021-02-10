

class Person:

    def __init__(self, name, age):
        self.age = age
        self.name = name


    def __str__(self):
        return 'Name is {} and age is {}'.format(self.name, self.age)

    @property
    def age(self):
        print('getting Age...')
        return self._age

    @age.setter
    def age(self, value):
        print('setting Age...')
        if value < 0:
            raise ValueError("Age can not be negative!")
        else:
            self._age = value


    @property
    def name(self):
        print('Getting Name...')
        return self._name


    @name.setter
    def name(self, value):
        print('Setting Name...')
        self._name = value


p = Person('mansour', 10)
print(p.age)
print(p)
