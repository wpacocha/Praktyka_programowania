# zagniedzone warunki score
# duzo duplikacji
# dodano 3 metody
# dodano score_names
class TennisGame1:
    SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        elif player_name == self.player2_name:
            self.player2_score += 1

    def score(self):
        if self.player1_score == self.player2_score:
            return self._draw_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self._endgame_score()
        else:
            return self._standard_score()

    def _draw_score(self):
        if self.player1_score < 3:
            return f"{self.SCORE_NAMES[self.player1_score]}-All"
        return "Deuce"

    def _endgame_score(self):
        score_diff = self.player1_score - self.player2_score
        if score_diff == 1:
            return f"Advantage {self.player1_name}"
        elif score_diff == -1:
            return f"Advantage {self.player2_name}"
        elif score_diff >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def _standard_score(self):
        return f"{self.SCORE_NAMES[self.player1_score]}-{self.SCORE_NAMES[self.player2_score]}"
