from game import Game

def get_user_menu_choice():
    valid_choices = ['1', '2', '3', 'x', 'q']
    choice = ''
    while choice not in valid_choices:
        print('Menu:')
        print('1. Play a new game')
        print('2. Show scores')
        print('3. Quit')
        choice = input('Enter your choice: ')
    return choice

def print_results(results):
    print('Results:')
    print(f"Win: {results['win']}")
    print(f"Loss: {results['loss']}")
    print(f"Draw: {results['draw']}")
    print('Thank you for playing!')

def main():
    results = {'win': 0, 'loss': 0, 'draw': 0}
    choice = ''
    while choice not in ['x', 'q']:
        choice = get_user_menu_choice()
        if choice == '1':
            game = Game()
            result = game.play()
            if result == 'win;':
                results['win'] += 1
            elif result == 'loss;':
                results['loss'] += 1
            else:
                results['draw'] += 1
        elif choice == '2':
            print_results(results)
    print_results(results)

if __name__ == '__main__':
    main()
