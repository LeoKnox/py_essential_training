class Duck():
    def quack(self):
        print('says Quaaaack!')

    def walk(self):
        print('Walks like a duck.')

def main():
    donald = Duck()
    donald.quack()
    donald.walk()

if __name__ == '__main__': main()