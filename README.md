# Agente de IA para 2048

Este repositorio contiene la implementación de agentes de búsqueda capaces de jugar al juego 2048. En particular, se han desarrollado varios algoritmos de búsqueda adversaria para controlar al jugador y el generador de casillas, y se proporciona tanto un modo de juego automático (IA vs. Juego) como un modo interactivo (Humano vs. Juego).

## Características Principales

- **Lógica completa del juego 2048**: Implementación de las reglas, movimientos y condiciones de victoria/derrota.
- **Interfaz Gráfica**: Visualización del tablero en tiempo real construida con `Tkinter`.
- **Agentes de Inteligencia Artificial**:
    - **Minimax**: Agente basado en el algoritmo clásico de Minimax para juegos de suma cero.
    - **Poda Alpha-Beta**: Una versión optimizada de Minimax que reduce el número de nodos a evaluar.
    - **Expectimax**: Un agente diseñado para manejar la naturaleza estocástica (aleatoria) del juego 2048, donde la computadora coloca fichas al azar.
- **Dos Modos de Juego**:
    - **Automático**: Observa a un agente de IA jugar por sí mismo.
    - **Interactivo**: Juega tú mismo contra la computadora, que puede colocar fichas de forma aleatoria o usando un agente inteligente en tu contra.

## Estructura del Repositorio

El proyecto está organizado en los siguientes archivos principales:

-   `gameState.py`: Contiene la clase `GameState`, que modela el estado del juego, incluyendo el tablero, las reglas de movimiento, y la lógica para determinar si se ha ganado o perdido.
-   `multiAgent.py`: Aquí se implementan los agentes de IA. Contiene las clases `MinimaxAgent`, `AlphaBetaAgent` y `ExpectimaxAgent`, junto con una función de evaluación de ejemplo.
-   `gameUI.py`: Define la clase `GameUI`, responsable de crear y actualizar la interfaz gráfica del juego usando `Tkinter`.
-   `game.py`: Script para ejecutar el **modo de juego automático**. Un agente de IA toma todas las decisiones.
-   `playGame.py`: Script para ejecutar el **modo de juego interactivo**, donde el usuario controla los movimientos.

## Cómo Ejecutar el Proyecto

No se requieren dependencias externas, ya que el proyecto utiliza bibliotecas estándar de Python.

### 1. Modo Automático (IA jugando sola)

En este modo, puedes ver a uno de los agentes de IA jugar al 2048. Es ideal para probar y comparar el rendimiento de los diferentes algoritmos.

**Para ejecutar:**

```bash
python game.py
```

**Personalización:**

Puedes modificar el comportamiento del agente directamente en el archivo `game.py`:

-   **Cambiar el agente**: En la sección `if __name__ == '__main__':`, puedes cambiar la clase del agente.
    ```python
    # Elige entre AlphaBetaAgent, MinimaxAgent o ExpectimaxAgent
    agent = AlphaBetaAgent(evalFn=evaluationFunction2048, depth=AGENT_DEPTH)
    ```
-   **Ajustar la profundidad de búsqueda (`AGENT_DEPTH`)**: Un valor más alto hará que el agente "piense" más movimientos a futuro, resultando en mejores decisiones pero un tiempo de respuesta más lento.
    ```python
    AGENT_DEPTH = 3 # Aumenta para una IA más fuerte
    ```
-   **Cambiar la velocidad del juego (`GAME_SPEED_DELAY`)**: Modifica el tiempo (en segundos) entre cada movimiento para observar el juego más rápido o más lento.
    ```python
    GAME_SPEED_DELAY = 0.1 # Menor valor = juego más rápido
    ```

### 2. Modo Interactivo (Tú juegas)

En este modo, tú controlas las fichas usando el teclado, y la computadora añade una nueva ficha después de cada movimiento.

**Para ejecutar:**

```bash
python playGame.py
```

**Controles:**

-   **Flechas del teclado**: Arriba, Abajo, Izquierda, Derecha.
-   **Teclas WASD**: `W` (Arriba), `S` (Abajo), `A` (Izquierda), `D` (Derecha).

**Personalización:**

Puedes cambiar cómo la computadora coloca las nuevas fichas editando el archivo `playGame.py`:

-   **Modo del adversario (`COMPUTER_MODE`)**:
    -   `'random'`: La computadora colocará una ficha (2 o 4) en una casilla vacía al azar. Es el modo estándar y más fácil.
    -   `'alphabeta'`: La computadora usará un agente Alpha-Beta para colocar la ficha en la **peor posición posible para ti**. Este modo ofrece un desafío mucho mayor.
    ```python
    # Cambia a 'alphabeta' para un desafío
    COMPUTER_MODE = 'random'
    ```
