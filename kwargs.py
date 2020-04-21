def main():
    x = Bugs = "mrrow", Daffy = "hiss", Goofy="ehh"
    kitten(**x)

def kitten(**kwargs):
    if len(kwargs):
        for k in kwargs:
            print('Kitten {} say {}'.format(k, kwargs[k]))
    else:
        print ('feh')

if __name__ == '__main__': main()