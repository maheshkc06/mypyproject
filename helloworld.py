import sys

class Helloworld():

    def __init__(self, name):
        self.name = name

    def greet(self):
        return "hello " + self.name


c = Helloworld("mahesh")
print(c.greet())



