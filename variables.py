class Animal:
    x = [1, 2, 3]
    def __init__(self, **kwargs):
        self.__type = kwargs['type'] if 'type' in kwargs else 'puma'
        self.__name = kwargs['name'] if 'name' in kwargs else 'kitty'
        self.__sound = kwargs['sound'] if 'sound' in kwargs else 'purrrrrr'
    
    def type(self, t = None):
        if t: self.__type = t
        return self.__type
    
    def name(self, n = None):
        if n: self.__name = n
        return self.__name
    
    def sound(self, s = None):
        if s: self.__sound = set
        return self.__sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says {self.sound()}".'

def main():
    a0 = Animal(type = 'hellhound', name='x fido', sound='arrrrrf')
    a1 = Animal(type = 'parrot', name='jimmy', sound='squawk')
    print(a0)
    print(a1)
    print(a0.x)
    a1.x[0] = 8
    print(a0.x)

if __name__ == '__main__': main()