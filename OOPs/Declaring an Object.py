class Dog:
    # a simple class
    # attribute
    pass
    attr1 = "mammal"
    attr2 = "dog"

    # A sample method

    def fun(self):
        print("I'm a ", self.attr1)
        print("I'm a ", self.attr2)

# Object Instantiation
Rodger =  Dog()

# Accessing class and objects through objects
print(Rodger.attr1)
Rodger.fun()


"""
an object is created which is basically a dog named Rodger. This class only has two class attributes that tell us that Rodger is a dog and a mammal.

"""
