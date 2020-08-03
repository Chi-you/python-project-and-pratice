# static
# when a variable is delared as static which means it has already been writen into the memory when class initialize
# when to use static:
# 1. we hope that some members is independent of instance
# 2. because of using only one part of memory, so no matter how much instances there are, the space of the static member would not increase
# example:
class Shiba:
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @staticmethod # we use decorator '@staticmethod' to declare the method is static
    def pee(length): # parameter has no 'self' and 'cls' so it cannot access the static member
        print("pee" + "." * length)

Shiba.pee(3) # static method not only can be called by instance but also class 

Shiba.pee(20)

black_shiba = Shiba(90, 40)
black_shiba.pee(10)


class Sh:
    pee_length = 10

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @staticmethod
    def pee(): 
        print("pee" + "." * pee_length) # parameter has no 'self' and 'cls' so it cannot access the static member (pee_length)
Sh.pee() 

Sh.pee()

black = Sh(90, 40)
black.pee()


# Error > NameError: name 'pee_length' is not defined
