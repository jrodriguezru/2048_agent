import time
import random
from gameState import GameState
from multiAgent import MinimaxAgent, AlphaBetaAgent, ExpectimaxAgent, evaluationFunction2048
from gameUI import start_ui

class Game:
    def __init__(self, agent, ui_root, ui_app, delay=0.5):
        self.gameState = GameState()
        self.agent = agent
        self.ui_root = ui_root
        self.ui_app = ui_app
        self.delay = delay
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
        self.update_ui()

    def add_tile(self):
        if type(self.agent) == MinimaxAgent or type(self.agent) == AlphaBetaAgent:
            nextMove = self.agent.getAction(self.gameState, agentIndex=1)
        else:
            self.add_random_tile()
            return
        i, j, value = nextMove.split(', ')
        i, j, value = int(i), int(j), int(value)
        self.gameState.board[i][j] = value

    def add_random_tile(self):
        empty_cells = []
        for i in range(4):
            for j in range(4):
                if self.gameState.board[i][j] == 0:
                    empty_cells.append((i, j))
        
        if empty_cells:
            i, j = random.choice(empty_cells)
            # 90% chance of 2, 10% chance of 4
            value = 2 if random.random() < 0.9 else 4
            self.gameState.board[i][j] = value

    def update_ui(self):
        self.score = sum(sum(row) for row in self.gameState.board)
        self.ui_app.update_board(self.gameState.board, self.score)
        self.ui_root.update()

    def run(self):
        while not self.gameState.isWin() and not self.gameState.isLose():
            # Player's turn (Agent 0)
            action = self.agent.getAction(self.gameState)
            if not action: # No legal moves
                break
            
            self.gameState = self.gameState.generateSuccessor(0, action)
            self.update_ui()
            time.sleep(self.delay)

            if self.gameState.isWin() or self.gameState.isLose():
                break

            # Computer's turn (Agent 1) - Add a random tile
            self.add_tile()
            self.update_ui()
            time.sleep(self.delay)

        # Game over
        if self.gameState.isWin():
            print("You Win!")
        else:
            print("Game Over!")
        self.ui_root.mainloop() # Keep window open

if __name__ == '__main__':
    # --- Configuration ---
    AGENT_DEPTH = 2  # How many moves ahead the agent thinks
    GAME_SPEED_DELAY = 0.01  # Seconds between moves

    # --- Setup ---
    # You can switch to MinimaxAgent or ExpectimaxAgent if you want
    agent = MinimaxAgent(evalFn=evaluationFunction2048, depth=AGENT_DEPTH)
    
    ui_root, ui_app = start_ui()

    # --- Start Game ---
    game = Game(agent, ui_root, ui_app, delay=GAME_SPEED_DELAY)
    game.run()
