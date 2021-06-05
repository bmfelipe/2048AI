
from game_v2 import *
from interface import *
from helper import *

def print_matrix(arr):
    for i in arr:
        print(i)

game = Game()
game.refresh_game()
interf = GameInterface(game)
interf.show_game()
interf.show_score()


while True:
    print_matrix(game.getMatrix())
    print(game.getScreen())
    print("Refresh 1...")
    interf.refresh_screen()
    stdin = input("Move:")
    movement = char_to_move(stdin)
    if movement is None:
        continue

    game.try_move(movement)
    interf.refresh_screen()
    print("Refresh 2...")

