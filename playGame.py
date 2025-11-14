"""
Juego interactivo de 2048 donde el jugador humano compite contra la computadora.
El jugador utiliza las teclas de flecha o WASD para mover las fichas,
mientras que la computadora coloca nuevas fichas en el tablero de acuerdo a un modo seleccionado
(aleatorio o utilizando un agente Alpha-Beta).
"""

import tkinter as tk
import random
import time
from gameState import GameState
from multiAgent import AlphaBetaAgent, evaluationFunction2048
from gameUI import start_ui

class InteractiveGame:
    def __init__(self, master, app, computer_mode='random', agent_depth=2):
        self.master = master
        self.app = app
        self.gameState = GameState()
        
        # --- Configuración del modo de juego ---
        self.computer_mode = computer_mode
        if self.computer_mode == 'alphabeta':
            self.computer_agent = AlphaBetaAgent(evalFn=evaluationFunction2048, depth=agent_depth)
            self.computer_agent.index = 1 
        
        self.score = 0
        self.bind_keys()
        self.start_game()

    def start_game(self):
        """ Inicia el juego añadiendo dos fichas aleatorias. """
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def bind_keys(self):
        """ Asocia las teclas a las acciones del juego. """
        self.master.bind("<Key>", self.key_press)

    def key_press(self, event):
        """ Maneja el evento de presionar una tecla. """
        key = event.keysym
        action = None
        
        # Mapeo de teclas a acciones
        if key in ['Up', 'w', 'W']:
            action = 'Up'
        elif key in ['Down', 's', 'S']:
            action = 'Down'
        elif key in ['Left', 'a', 'A']:
            action = 'Left'
        elif key in ['Right', 'd', 'D']:
            action = 'Right'
        
        if action and action in self.gameState.getLegalActions(0):
            # 1. El jugador realiza su movimiento
            self.gameState = self.gameState.generateSuccessor(0, action)
            self.update_ui()
            
            if self.check_game_over():
                return

            # 2. El agente responde después de un breve retraso
            self.master.after(200, self.computer_turn)

    def computer_turn(self):
        """ El agente coloca una nueva ficha. """
        if self.computer_mode == 'random':
            self.add_random_tile()
        elif self.computer_mode == 'alphabeta':
            self.add_alphabeta_tile()
        
        self.update_ui()
        self.check_game_over()

    def add_random_tile(self):
        """ Añade una ficha (2 o 4) en una celda vacía al azar. """
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.gameState.board[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            value = 2 if random.random() < 0.9 else 4
            self.gameState.board[i][j] = value

    def add_alphabeta_tile(self):
        """ El agente Alpha-Beta elige dónde colocar la siguiente ficha. """
        action = self.computer_agent.getAction(self.gameState, agentIndex=1)
        if action:
            self.gameState = self.gameState.generateSuccessor(1, action)

    def update_ui(self):
        """ Actualiza el tablero y la puntuación en la interfaz gráfica. """
        self.score = sum(sum(row) for row in self.gameState.board)
        self.app.update_board(self.gameState.board, self.score)
        self.master.update()

    def check_game_over(self):
        """ Verifica si el juego ha terminado (victoria o derrota). """
        if self.gameState.isWin():
            print("¡Has ganado!")
            self.master.unbind("<Key>")
            return True
        if self.gameState.isLose():
            print("¡Juego terminado!")
            self.master.unbind("<Key>")
            return True
        return False

if __name__ == '__main__':
    # --- Configuración ---
    COMPUTER_MODE = 'random'  # Cambia a 'alphabeta' para un desafío mayor
    AGENT_DEPTH = 2  # Profundidad para el agente Alpha-Beta

    # --- Iniciar UI y Juego ---
    root, app = start_ui()
    game = InteractiveGame(root, app, computer_mode=COMPUTER_MODE, agent_depth=AGENT_DEPTH)
    root.mainloop()