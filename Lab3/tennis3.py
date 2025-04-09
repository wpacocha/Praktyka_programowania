#cala logika upchana w score()
#spaghetti if elif
#trudne do zrozumienia porownania
class TennisGame3:
    def __init__(self, player1_name, player2_name):
        self.p1_n = player1_name
        self.p2_n = player2_name
        self.p1 = 0
        self.p2 = 0

    def won_point(self, n):
        if n == self.p1_n:
            self.p1 += 1
        else:
            self.p2 += 1

    def score(self):
        if self.p1 == self.p2:
            return self._draw_score()
        elif self.p1 >= 4 or self.p2 >= 4:
            return self._endgame_score()
        else:
            return self._standard_score()

    def _point_name(self, point):
        return ["Love", "Fifteen","Thirty","Forty"][point]

    def _draw_score(self):
        if self.p1 <3:
            return f"{self._point_name(self.p1)}-All"
        return "Deuce"

    def _endgame_score(self):
        score_diff = self.p1 - self.p2
        if score_diff == 1:
            return f"Advantage {self.p1_n}"
        elif score_diff == -1:
            return f"Advantage {self.p2_n}"
        elif score_diff >= 2:
            return f"Win for {self.p1_n}"
        else:
            return f"Win for {self.p2_n}"

    def _standard_score(self):
        return f"{self._point_name(self.p1)}-{self._point_name(self.p2)}"