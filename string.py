class RevStr(str):
    def __str__(self):
        return self[::-1]

def main():
    hello = RevStr('Hello everybody!')
    print(hello)

if __name__ == '__main__': main()