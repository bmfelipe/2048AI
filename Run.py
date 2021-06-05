
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
    stdin = input("Move:")
    movement = char_to_move(stdin)
    if movement is None:
        continue

    game.try_move(movement)
    print("Step 7: Move done!")
    game.refresh_screen()

