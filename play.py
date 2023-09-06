import pygame
import gui
import tictactoe
from time import sleep
    
running = True
player = 1
result = 0

gui.drawBoard()
tictactoe = tictactoe.TicTacToe()
state = tictactoe.get_initial_state()

def tictactoeAlgorithm(coordinate,state,player):
    result_t = 0
    coordinate_x , coordinate_y  = coordinate[0] // 50 , coordinate[1] // 50         
    print(coordinate, coordinate_x , coordinate_y )
    action = (coordinate_y * 3) + coordinate_x
    valid_moves = tictactoe.get_valid_moves(state)
    print("valid_moves", [i for i in range(tictactoe.action_size) if valid_moves[i] == 1])
    
    if valid_moves[action] == 0:
        print("action not valid")
    else:
        state = tictactoe.get_next_state(state, action, player)
        value, is_terminal = tictactoe.get_value_and_terminated(state, action)
        gui.screnUpdate(coordinate_x , coordinate_y,player)
        if is_terminal:
            print(state)
            if value == 1:
                print(player, "won")
                result_t = 1
            else:
                print("draw")
                result_t = 0.5
        player = tictactoe.get_opponent(player)
    print(state)    
    return player,result_t



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressed = pygame.mouse.get_pressed()
            if pressed[0]: #pushing left button
                pos = pygame.mouse.get_pos()
                player,result = tictactoeAlgorithm(pos,state,player)
        if result == 1:
            gui.drawMessage(player)
            pygame.display.update()
            sleep(3)
            state = tictactoe.get_initial_state()
            gui.drawBoard()
            result = 0
        if result == 0.5:
            print("0.5")
            gui.drawMessage(result)
            pygame.display.update()
            sleep(3)
            state = tictactoe.get_initial_state()
            gui.drawBoard()
            result = 0

    pygame.display.update()

