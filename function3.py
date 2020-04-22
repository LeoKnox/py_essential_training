def main():
        x = kitten()
        print(type(x), x)

def kitten():
    print('cat')
    return dict(x=42, y=43)

if __name__ == '__main__': main()