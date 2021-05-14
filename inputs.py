import game_v2
from game_v2 import *
from interface import *
from helper import *

def print_matrix(arr):
    for i in arr:
        print(i)

game = Game()
game.refresh_game()
interf = GameInterface(game)

while True:
    print_matrix(game.Matrix())
    interf.refresh_screen()
    stdin = input("Move:")
    movement = char_to_move(stdin)
    if movement is None:
        continue

    game.try_move(movement)
    interf.refresh_screen()
