class Node:
    def __init__(self, name):
        self.grid = name
        self.h = 10000
        self.g = 1000
        self.f = self.g + self.h
        self.parent = ""
    
    def update(self, g, h):
        self.h = h
        self.g = g
        self.f = self.g + self.h

    def __str__(self):
        return self.grid