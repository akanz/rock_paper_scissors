class Participant:
    def __init__(self, name: str) -> None:
        self.__point__ = 0
        self.symbol = ''
        self.name = name

    def choose(self):
        self.symbol = input(
            '{name}, choose an option. Rock, paper or Scissors: '.format(name=self.name))
        print('{name} selected {choice}'.format(
            name=self.name, choice=self.symbol))

    def toNumericalChoice(self):
        switcher = {
            "rock": 0,
            "paper": 1,
            "scissor": 2
        }
        return switcher[self.symbol]

    def increment_point(self):
        self.__point__ += 1

    def get_points(self):
        return self.__point__


class Game:
    def __init__(self) -> None:
        self.endGame = False
        self.player1, self.player2 = Participant('Samuel'), Participant('Juwon')

    def start(self):
        while not self.endGame:
            Round(self.player1, self.player2)
            self.end_game()

    def check_winner(self):
        resultString = "It's a Draw"
        if self.player1.get_points() > self.player2.get_points():
            resultString = "Winner is {name}".format(name=self.player1.name)
        elif self.player1.get_points() < self.player2.get_points():
            resultString = "Winner is {name}".format(name=self.player2.name)
        print(resultString)

    def end_game(self):
        answer = input("Continue game y/n: ")
        if answer == 'y':
            Round(self.player1, self.player2)
            self.end_game()
        else:
            print("Game ended, {p1name} has {p1points}, and {p2name} has {p2points}"
            .format(p1name = self.player1.name, p1points= self.player1.get_points(), p2name=self.player2.name, p2points=self.player2.get_points()))
            self.check_winner()
            self.endGame = True


class Round:
    def __init__(self, p1: Participant, p2: Participant) -> None:
        self.rules = [
            [0, -1, 1],
            [1, 0, -1],
            [-1, 1, 0]
        ]  
        p1.choose()
        p2.choose()
        result = self.compare_choice(p1, p2)
        print("Round resulted in a {result}".format(result = self.getResultAsString(result) ))
        if result > 0:
           p1.increment_point()
        elif result < 0:
           p2.increment_point()

    def compare_choice(self, p1, p2):
        return self.rules[p1.toNumericalChoice()][p2.toNumericalChoice()]

    def getResultAsString(self, result):
        res = {
            0: "draw",
            1: "win",
            -1: "loss"
        }
        return res[result]

game = Game()
game.start()
