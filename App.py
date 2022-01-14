from Game import Game

HUMAN = 0
AI = 1
WHITE = True
BLACK = False

def main():

    g = Game(AI,AI)
    g.train()
    g.change_player(WHITE)
    g.run()

if __name__ == '__main__':
    main()