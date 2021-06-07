
from game_v2 import *
from helper import *

def print_matrix(arr):
    for i in arr:
        print(i)

game = Game()
game.interface()
game.refresh_game()

while True:
    print_matrix(game.getMatrix())
    print(game.getScreen())
    game.refresh_screen()
    
    while(True):
        available_moves_list = game.available_moves()
        stdin = input("Move:")
        if str(stdin) in available_moves_list:
            if mapped_keyz.get(str(stdin)) != None:
                movement = char_to_move(stdin)
                break
            else:
                print("Invalid key, please use: ",available_moves_list)
                continue
                # if movement is None:
        else:
            print("Invalid key, please use: ",available_moves_list)
            continue


    game.try_move(movement)
    print("Step 7: Move done!")
    game.refresh_screen()
    game.is_over()

