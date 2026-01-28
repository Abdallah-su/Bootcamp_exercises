from game import Game
my_game =Game()
def get_user_menu_choice():
    print('Welcome to RockPaperScissors Game!')
    user_choice = input("Type in a letter, 'P' to play a new game or 'N' to show scores or 'Q' to quit: ")
    return user_choice


def print_results(results):
    for outcome, count in results.items():
        print(f"{outcome} : {count}")



def main():
    get_user_menu_choice()
    game_outcome= {"win" : 0, "draw" : 0, "loss" : 0}
    while True:
        choice = get_user_menu_choice().upper()
        if choice == "P":
           result = my_game.play()
           game_outcome[result] +=1
        elif choice == "N":
            print_results(game_outcome)
        elif choice== "Q":
            print_results(game_outcome)
            print("goodbye")
            break
        else:
            ValueError("choose from the options")

main()

