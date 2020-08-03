# import abc # Abstract Base Classes


# class Dog(metaclass=abc.ABCMeta):
#     @abc.abstractmethod
#     def eat_shit(self):
#         return NotImplemented


# class Shiba(Dog):
#     pass


# Shiba()
# Error > TypeError: Can't instantiate abstract class Shiba with abstract methods eat_shit

import abc


class Dog(metaclass=abc.ABCMeta): # the Dog class is an interface
    @abc.abstractmethod
    def eat_shit(self):
        return NotImplemented

    @abc.abstractmethod
    def pee(self):
        return NotImplemented


class Shiba(Dog): # Shiba inherit from Dog
    # override the methods of the base class
    def eat_shit(self): 
        print("I'm eating shit".format())

    def pee(self):
        print("I'm peeing........")


Shiba().eat_shit()
# Result > I'm eating shit

Shiba().pee()
# Result > I'm peeing........