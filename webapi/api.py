import os
from apistar import App, Route

LISTEN_ADDR = os.environ.get('LISTEN_ADDR', '127.0.0.1')
LISTEN_PORT = int(os.environ.get('LISTEN_PORT', '5000'))
USE_DEBUGGER = True if os.environ.get('DEBUG') == "True" else False


def welcome() -> str:
    return 'Welcome to Mancala'


def gameNew(player1:str='human', player2:str='random') -> dict:
    return {
        'status': 'created'
    }


def gameList() -> dict:
    return {
            'games': [
                'sdfasefg',
                'fasgseg',
                'ifheahb',
                ] }


def gameGetState(gameid: str) -> dict:
    return {'status': 'in-progress'}


def gameMakeMove(gameid: str) -> dict:
    return {'status': 'legal'}


def gameWaitForAI(gameid: str) -> dict:
    return {'status': 'waiting'}


routes = [
    Route('/', method='GET', handler=welcome),
    Route('/new', method='POST', handler=gameNew),
    Route('/list', method='GET', handler=gameList),
    Route('/game/{gameid}', method='GET', handler=gameGetState),
    Route('/game/{gameid}/move', method='POST', handler=gameMakeMove),
    Route('/game/{gameid}/wait', method='GET', handler=gameWaitForAI)
]

app = App(routes=routes)

def main():
    app.serve(LISTEN_ADDR, LISTEN_PORT,
              use_debugger=USE_DEBUGGER, use_reloader=USE_DEBUGGER)

if __name__ == '__main__':
    main()
