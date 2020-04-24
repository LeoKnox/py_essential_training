def main():
    animals = { 'kitten': 'meow', 'puppy': 'bark', 'lion': 'roar', 'fox':'what do I say?', 'dragon':'fire!'}
    animals2 = dict( kitten= 'meow', puppy= 'bark', lion= 'roar', fox='what do I say?', dragon='fire!')
    animals['monkey'] = 'eepeep'
    print(animals.get('godzilla')) #this does not return error if not found
    for k, v in animals2.items():
    #for k in animals2.keys():
    #for v in animals2.values():
        print(f'{k}: {v}')
    print_dict(animals)

def print_dict(o):
    for x in o:
        print(f'{x}: {o[x]}')

if __name__ == '__main__': main()