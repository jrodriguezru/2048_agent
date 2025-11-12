from gameState import GameState
from math import inf
from typing import Callable

def evalFunctionPlaceholder(gameState: GameState) -> int:
    """
    Placeholder evaluation function
    """
    return 0

class MultiAgentSearchAgent():
    """
    Abstract class for multi-agent search agents
    """

    def __init__(self, evalFn: Callable[[GameState], int] = evalFunctionPlaceholder, depth: int = 2):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = evalFn
        self.depth = depth


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def max_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int) -> float:
        """
        Max value function for minimax algorithm
        """
        v = -inf
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                v = max(v, self.evaluationFunction(successor))
            else:
                v = max(v, self.min_value(successor, agent + 1, totalAgents, actualDepth))
        return v
    
    def min_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int) -> float:
        """
        Min value function for minimax algorithm
        """
        v = inf
        nextAgent = (agent+1) % totalAgents
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                v = min(v, self.evaluationFunction(successor))
            else:
                if nextAgent == 0:
                    if self.depth == actualDepth:
                        v = min(v, self.evaluationFunction(successor))
                    else:
                        v = min(v, self.max_value(successor, nextAgent, totalAgents, actualDepth + 1))
                else:
                    v = min(v, self.min_value(successor, nextAgent, totalAgents, actualDepth))
        return v

    def getAction(self, gameState: GameState) -> str:
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.
        """
        best_action = ''
        best_value = -inf
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            if successor.isWin() or successor.isLose():
                value = self.evaluationFunction(successor)
            else:
                value = self.min_value(successor, 1, gameState.getNumAgents(), 1)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
        

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Minimax agent with alpha-beta pruning.
    """

    def max_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int, alpha: float, beta: float) -> float:
        """
        Max value function for minimax algorithm with alpha-beta pruning
        """
        v = -inf
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                v = max(v, self.evaluationFunction(successor))
            else:
                v = max(v, self.min_value(successor, agent + 1, totalAgents, actualDepth, alpha, beta))
            alpha = max(alpha, v)
            if v > beta:
                break
        return v

    def min_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int, alpha: float, beta: float) -> float:
        """
        Min value function for minimax algorithm with alpha-beta pruning
        """
        v = inf
        nextAgent = (agent+1) % totalAgents
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                v = min(v, self.evaluationFunction(successor))
            else:
                if nextAgent == 0:
                    if self.depth == actualDepth:
                        v = min(v, self.evaluationFunction(successor))
                    else:
                        v = min(v, self.max_value(successor, nextAgent, totalAgents, actualDepth + 1, alpha, beta))
                else:
                    v = min(v, self.min_value(successor, nextAgent, totalAgents, actualDepth, alpha, beta))
            beta = min(beta, v)
            if v < alpha:
                break
        return v

    def getAction(self, gameState: GameState) -> str:
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        best_action = ''
        best_value = -inf
        alpha = -inf
        beta = inf
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            if successor.isWin() or successor.isLose():
                value = self.evaluationFunction(successor)
            else:
                value = self.min_value(successor, 1, gameState.getNumAgents(), 1, alpha, beta)
            alpha = max(alpha, value)

            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Expectimax agent
    """

    def max_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int) -> float:
        v = -inf
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                v = max(v, self.evaluationFunction(successor))
            else:
                v = max(v, self.exp_value(successor, agent + 1, totalAgents, actualDepth))
        return v
    
    def exp_value(self, gameState: GameState, agent: int, totalAgents: int, actualDepth: int) -> float:
        v = inf
        nextAgent = (agent+1) % totalAgents
        scores = []
        for action in gameState.getLegalActions(agent):
            successor = gameState.generateSuccessor(agent, action)
            if successor.isWin() or successor.isLose():
                scores.append(self.evaluationFunction(successor))
            else:
                if nextAgent == 0:
                    if self.depth == actualDepth:
                        scores.append(self.evaluationFunction(successor))
                    else:
                        scores.append(self.max_value(successor, nextAgent, totalAgents, actualDepth + 1))
                else:
                    scores.append(self.exp_value(successor, nextAgent, totalAgents, actualDepth))
        v = sum(scores) / len(scores) if scores else 0
        return v

    def getAction(self, gameState: GameState) -> str:
        """
        Returns the expectimax action using self.depth and self.evaluationFunction
        """
        best_action = ''
        best_value = -inf
        for action in gameState.getLegalActions(0):
            successor = gameState.generateSuccessor(0, action)
            if successor.isWin() or successor.isLose():
                value = self.evaluationFunction(successor)
            else:
                value = self.exp_value(successor, 1, gameState.getNumAgents(), 1)
            if value > best_value:
                best_value = value
                best_action = action
        return best_action
    

def evaluationFunction2048(currentGameState: GameState) -> int:
    return 0