class Duck:
    sound = 'Duck duck'
    movement = 'Swim like a duck'

    def quack(self):
        print(self.sound)
    
    def move(self):
        print(self.movement)

def main():
    daffy = Duck()
    daffy.quack()
    daffy.move()

if __name__ == '__main__': main()