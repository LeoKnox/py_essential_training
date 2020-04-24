class Animal:
    def __init__(self, **kwargs):
        self.__type = kwargs['type'] if 'type' in kwargs else 'kitten'
        self.__name = kwargs['name'] if 'name' in kwargs else 'kitty'
        self.__sound = kwargs['sound'] if 'sound' in kwargs else 'sound'
    
    def type(self, t = None):
        if t: self.__type = t
        return self.__type

    def name(self, n = None):
        if n: self.__name = n
        return self.__name
    
    def sound(self, s =  None):
        if s: self.__sound = s
        return self.__sound

    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'
    
def main():
    a0 = Animal(type= 'badger', name = 'honey', sound = 'I dont care')
    a1 = Animal(type='wolf', name='dark', sound='howl')
    a0.sound('owww')
    print(a0)
    print(a1)
    
if __name__ == '__main__': main()