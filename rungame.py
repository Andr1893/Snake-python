from snake import *

_game = snake()

def run():
    while True:
        while not _game.game_over:
            _game.startGame()

        
        while _game.game_over:
            _game.gameOver()



run()