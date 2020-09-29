""" As of 09/28/2020 17:19 MST
    Runtime: 584 ms (beats 5.11% of python3 submissions)
    Memory: 16.5 MB (beats 6.30%  of python3 submissions)
"""


class TicTacToe:
    def __init__(self, n: int):
        self.state = {1:
                      {
                          "ROWS": [0 for x in range(n)],
                          "COLUMNS": [0 for x in range(n)],
                          "MAINDIAGONAL": 0,
                          "CROSSDIAGONAL": 0
                      },
                      2: {
                          "ROWS": [0 for x in range(n)],
                          "COLUMNS": [0 for x in range(n)],
                          "MAINDIAGONAL": 0,
                          "CROSSDIAGONAL": 0
                      }}

        self.n = n
        self.round = 0

    def winner(self):
        if self.round < self.n:
            return 0
        else:
            for player in [1, 2]:
                if self.state[player]["MAINDIAGONAL"] == self.n:
                    return player
                elif self.state[player]["CROSSDIAGONAL"] == self.n:
                    return player
                else:
                    for i in range(self.n):
                        if self.state[player]["ROWS"][i] == self.n or self.state[player]["COLUMNS"][i] == self.n:
                            return player

            return 0

    def move(self, row: int, col: int, player: int) -> int:
        self.state[player]["ROWS"][row] += 1
        self.state[player]["COLUMNS"][col] += 1

        if row == col:
            self.state[player]["MAINDIAGONAL"] += 1

        if row + col == self.n - 1:
            self.state[player]["CROSSDIAGONAL"] += 1

        self.round += 1
        return self.winner()


t = TicTacToe(3)

print(t.move(0, 0, 1))
print(t.move(0, 1, 1))
print(t.move(0, 2, 1))
