from Game import Game

def main():
    g = Game(1,1)
    g.train()
    g.change_player(True)
    g.run()

if __name__ == '__main__':
    main()