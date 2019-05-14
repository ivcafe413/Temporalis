from transitions import Machine

class GameStateMachine:
    GameStates = ['overworld', 'menu', 'battle']

    def __init__(self):
        self.machine = Machine(model=self, states=GameStateMachine.GameStates, initial='overworld')
