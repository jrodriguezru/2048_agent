class GameState:    
    """
    A class to represent the state of a 2048 game.
    """
    def __init__(self):
        self.board = [[0 for _ in range(4)] for _ in range(4)]

    def isLose(self) -> bool:
        """
        Check if there are no legal moves left
        """
        for row in self.board:
            for cell in row:
                if cell == 0:
                    return False
        for i in range(4):
            for j in range(3):
                if self.board[i][j] == self.board[i][j + 1]:
                    return False
        for j in range(4):
            for i in range(3):
                if self.board[i][j] == self.board[i + 1][j]:
                    return False
        return True
    
    def isWin(self) -> bool:
        """
        Check if there is a tile with value 2048
        """
        for row in self.board:
            for cell in row:
                if cell == 2048:
                    return True
        return False
    
    def getLegalActions(self, agentIndex: int = 0) -> list:
        """
        Returns a list of legal actions for the given agent.
        Agent 0 is the player, Agent 1 is the random tile generator.
        """
        actions = []
        if agentIndex == 0:
            # Check possible moves for the player
            # Check left
            for i in range(4):
                for j in range(1, 4):
                    if self.board[i][j] != 0:
                        if self.board[i][j - 1] == 0 or self.board[i][j - 1] == self.board[i][j]:
                            actions.append('Left')
                            break
            # Check right
            for i in range(4):
                for j in range(2, -1, -1):
                    if self.board[i][j] != 0:
                        if self.board[i][j + 1] == 0 or self.board[i][j + 1] == self.board[i][j]:
                            actions.append('Right')
                            break
            # Check up
            for j in range(4):
                for i in range(1, 4):
                    if self.board[i][j] != 0:
                        if self.board[i - 1][j] == 0 or self.board[i - 1][j] == self.board[i][j]:
                            actions.append('Up')
                            break
            # Check down
            for j in range(4):
                for i in range(2, -1, -1):
                    if self.board[i][j] != 0:
                        if self.board[i + 1][j] == 0 or self.board[i + 1][j] == self.board[i][j]:
                            actions.append('Down')
                            break
        elif agentIndex == 1:
            # Possible placements for new tiles (2 or 4) in empty cells
            actions = []
            for i in range(4):
                for j in range(4):
                    if self.board[i][j] == 0:
                        actions.append(f"{i}, {j}, 2")
                        actions.append(f"{i}, {j}, 4")
        return actions

    def generateSuccessor(self, agentIndex: int, action: str) -> 'GameState':
        """
        Returns the successor game state after the given agent takes the given action.
        """
        newState = GameState()
        if agentIndex == 0:
            newState.board = [row[:] for row in self.board]
            if action == 'Left':
                for i in range(4):
                    filtered = [num for num in newState.board[i] if num != 0]
                    merged = []
                    skip = False
                    for j in range(len(filtered)):
                        if skip:
                            skip = False
                            continue
                        if j + 1 < len(filtered) and filtered[j] == filtered[j + 1]:
                            merged.append(filtered[j] * 2)
                            skip = True
                        else:
                            merged.append(filtered[j])
                    merged += [0] * (4 - len(merged))
                    newState.board[i] = merged
            elif action == 'Right':
                for i in range(4):
                    filtered = [num for num in newState.board[i] if num != 0]
                    merged = []
                    skip = False
                    for j in range(len(filtered) - 1, -1, -1):
                        if skip:
                            skip = False
                            continue
                        if j - 1 >= 0 and filtered[j] == filtered[j - 1]:
                            merged.insert(0, filtered[j] * 2)
                            skip = True
                        else:
                            merged.insert(0, filtered[j])
                    merged = [0] * (4 - len(merged)) + merged
                    newState.board[i] = merged
            elif action == 'Up':
                for j in range(4):
                    filtered = [newState.board[i][j] for i in range(4) if newState.board[i][j] != 0]
                    merged = []
                    skip = False
                    for i in range(len(filtered)):
                        if skip:
                            skip = False
                            continue
                        if i + 1 < len(filtered) and filtered[i] == filtered[i + 1]:
                            merged.append(filtered[i] * 2)
                            skip = True
                        else:
                            merged.append(filtered[i])
                    merged += [0] * (4 - len(merged))
                    for i in range(4):
                        newState.board[i][j] = merged[i]
            elif action == 'Down':
                for j in range(4):
                    filtered = [newState.board[i][j] for i in range(4) if newState.board[i][j] != 0]
                    merged = []
                    skip = False
                    for i in range(len(filtered) - 1, -1, -1):
                        if skip:
                            skip = False
                            continue
                        if i - 1 >= 0 and filtered[i] == filtered[i - 1]:
                            merged.insert(0, filtered[i] * 2)
                            skip = True
                        else:
                            merged.insert(0, filtered[i])
                    merged = [0] * (4 - len(merged)) + merged
                    for i in range(4):
                        newState.board[i][j] = merged[i]
        elif agentIndex == 1:
            newState.board = [row[:] for row in self.board]
            i, j, value = action.split(', ')
            i, j, value = int(i), int(j), int(value)
            newState.board[i][j] = value
        return newState

    def getNumAgents(self) -> int:
        """
        Returns the number of agents in the game. 2048 has two agents.
        """
        return 2  # Player and random tile generator
