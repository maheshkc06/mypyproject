#import copy

class Myclass():
    def __init__(self, name):
        self.name = name

    def __cmp__(self, other):
        return self.name, other.name

    
