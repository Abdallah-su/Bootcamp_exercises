from game import Game
my_game =Game()
def get_user_menu_choice():
    print('Welcome to RockPaperScissors Game!')
    user_choice = input("Type in a letter, 'P' to play a new game or 'N' to show scores or 'Q' to quit: ")
    return user_choice


def print_results(results): 
    results  = { }
    user_choice = my_game.get_user_item()
    computer_choice = my_game.get_computer_item()
    game_outcome = my_game.get_game_result(user_choice, computer_choice)
    results[game_outcome] += 1
    return results 


def main():
    get_user_menu_choice()
    game_outcome= { }
    
    while True:
        if get_user_menu_choice() == "P":
           my_game.play()
           print(print_results(game_outcome))
        elif get_user_menu_choice() == "N":
            print(print_results(game_outcome))
        elif get_user_menu_choice() == "Q":
            print("goodbye")
            break
        else:
            ValueError("choose from the options")

main()

