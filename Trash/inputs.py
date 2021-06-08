# ---------------------------TRASH---------------------------
# from game_v2 import *
# from interface import *
# from helper import *
# import sys

# def print_matrix(arr):
#     for i in arr:
#         print(i)

# game = Game()
# print("Step 1: Game created!")

# game.refresh_game()
# print("Step 2: Game refreshed!")

# interf = GameInterface(game)
# print("Step 3: Interface created!")

# interf.show_game()
# print("Step 4: Interface shown!")

# interf.show_score()
# print("Step 5: Score2 shown!")
# # time.sleep(5)
# # sys.exit("Error message")

# while True:
#     print_matrix(game.getMatrix())
#     print(game.getScreen())
#     interf.refresh_screen()
#     print("Step 6: Screen refreshed!")
#     stdin = input("Move:")
#     movement = char_to_move(stdin)
#     if movement is None:
#         continue

#     game.try_move(movement)
#     print("Step 7: Move done!")
#     interf.refresh_screen()

