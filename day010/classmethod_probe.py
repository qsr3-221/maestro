class Demo:
    def __init__(self, x):
        self.x = x
    @classmethod
    def make(cls, x):
        return cls(x)
d = Demo.make(5)
print(d.x)
print(type(d))