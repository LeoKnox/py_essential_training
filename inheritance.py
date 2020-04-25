class Animal:
    def __init__(self, **kwargs):
        if 'type' in kwargs: self.__type = kwargs['type']
        if 'name' in kwargs: self.__name = kwargs['name']
        if 'sound' in kwargs: self.__sound = kwargs['sound']
    
    def type(self, t = None):
        if t: self.__type = t
        try: return self.__type
        except AttributeError: return None
    
    def name(self, n = None):
        if n: self.__name = n
        try: return self.__name
        except AttributeError: return None
    
    def sound(self, s = None):
        if s: self.__sound = s
        try: return self.__sound
        except AttributeError: return None
    
    def __str__(self):
        return f'The {self.type()} is named "{self.name()}" and says "{self.sound()}".'

class Duck(Animal):
    def __init__(self, **kwargs):
        self.__type = 'duck'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

class Kitten(Animal):
    def __init__(self, **kwargs):
        self._type = 'kitten'
        if 'type' in kwargs: del kwargs['type']
        super().__init__(**kwargs)

    def kill(self, s):
        print(f'{self.name()} will now kill all {s}!')

def main():
    a0 = Kitten(name = 'fluffy', sound = 'hiss')
    a1 = Duck(name = 'quack', sound = 'quack quack')
    print(a0)
    print(a1)
    a0.kill('humans')
if __name__ == '__main__': main()