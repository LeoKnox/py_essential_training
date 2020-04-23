def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
    t_game = ( 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
    print(game[1:4:2])
    i = game.index('Paper')
    print(game[i])
    game.append('Dynamite')
    game.insert(1, 'Cockroach')
    game.remove('Dynamite')
    y = game.pop(1)
    print(y)
    del game[1:3]
    print(', '.join(game))
    print(len(game))
    print_list(game)
    print(t_game[1 : 6 : 2])

def print_list(o):
    for i in o:
        print(i, end=' ', flush = True)
    print()

if __name__ == '__main__': main()