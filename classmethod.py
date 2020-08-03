# when we pass the class as a parameter of the function, then it is called class method (which is different from the other oop language)
# use decorator'@classmethod' to declare it
class Shiba:
    pee_length = 10 # static member(variable)

    # instance method
    def __init__(self, height, weight):
        self.height = height
        self.weight = weight

    @classmethod
    def pee(cls):  # we need to pass the class itself as a parameter (cls means class)
        print("pee" + "." * cls.pee_length)

Shiba.pee()


black_shiba = Shiba(30, 40)
black_shiba.pee()

# both of them have the same output
