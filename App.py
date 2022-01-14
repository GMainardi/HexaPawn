from Game import Game

HUMAN = 0
AI = 1
MONTECARLO = 2
RANDOM = -1
WHITE = True
BLACK = False

def main():

    g = Game(MONTECARLO, AI)
    g.train()
    g.change_player(WHITE)
    g.run()

if __name__ == '__main__':
    main()