#mnostwo powtarzalnych warunkow
class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.P1Score()
        else:
            self.P2Score()
    def score(self):
        if self.player1_score == self.player2_score:
            return self._draw_score()
        elif self.player1_score >= 4 or self.player2_score >=4:
            return self._endgame_score()
        else:
            return f"{self._point_name(self.player1_score)}-{self._point_name(self.player2_score)}"

    def setP1Score(self,number):
        self.player1_score = number
    def setP2Score9(self, number):
        self.player2_score = number

    def P1Score(self):
        self.player1_score += 1
    def P2Score(self):
        self.player2_score += 1

    def _point_name(self, point):
        return ["Love", "Fifteen","Thirty","Forty"][point]

    def _draw_score(self):
        if self.player1_score <3:
            return f"{self._point_name(self.player1_score)}-All"
        return "Deuce"

    def _endgame_score(self):
        diff = self.player1_score - self.player2_score
        if diff == 1:
            return f"Advantage {self.player1_name}"
        elif diff == -1:
            return f"Advantage {self.player2_name}"
        elif diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"