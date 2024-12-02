from enum import IntEnum

class Point(IntEnum):
    MINUS_ONE = -1
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4

class TennisGame:
    def __init__(self, blue_player_name, red_player_name):
        self.blue_player_name = blue_player_name
        self.red_player_name = red_player_name
        self.blue_player_score = 0
        self.red_player_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.blue_player_score = self.blue_player_score + 1
        else:
            self.red_player_score = self.red_player_score + 1

    def get_score(self):
        game_score = ""

        if self.blue_player_score == self.red_player_score:
            game_score = self.string_in_each_type_of_tie()

        elif self.blue_player_score >= Point.FOUR or self.red_player_score >= Point.FOUR:
            game_score = self.string_in_advantage_or_win_situation()

        else:
            game_score = self.string_in_normal_game_situation(game_score)

        return game_score

    def string_in_each_type_of_tie(self):
        if self.blue_player_score == Point.ZERO:
            score = "Love-All"
        elif self.blue_player_score == Point.ONE:
            score = "Fifteen-All"
        elif self.blue_player_score == Point.TWO:
            score = "Thirty-All"
        else:
            score = "Deuce"
        return score

    def string_in_advantage_or_win_situation(self):
        point_difference = self.blue_player_score - self.red_player_score

        if point_difference == Point.ONE:
            score = "Advantage player1"
        elif point_difference == Point.MINUS_ONE:
            score = "Advantage player2"
        elif point_difference >= Point.TWO:
            score = "Win for player1"
        else:
            score = "Win for player2"
        return score

    def string_in_normal_game_situation(self, score):
        for i in range(1, 3):
            if i == Point.ONE:
                current_score = self.blue_player_score
            else:
                score = score + "-"
                current_score = self.red_player_score
            if current_score == Point.ZERO:
                score = score + "Love"
            elif current_score == Point.ONE:
                score = score + "Fifteen"
            elif current_score == Point.TWO:
                score = score + "Thirty"
            elif current_score == Point.THREE:
                score = score + "Forty"
        return score
