from abc import ABC

class PlayerInterface(ABC):
    def __init__(self,name) -> None:
        self.id = None
        self.name = name
        self.score = 0
        self.balls_faced = 0
        self.sixes = 0
        self.fours = 0
        self.runs_given = 0
        self.maiden = 0
        self.overs = 0
        self.economy = 0
        self.wickets = 0
        
    def update_batting_score(self,runs):
        self.score+=runs
        self.balls_faced+=1
        if runs == 6:
            self.sixes+=1
        elif runs == 4:
            self.fours+=1
    
    def display_batting_player_score(self):
        div = '-'*40
        print(f'{self.id}\t{self.name}\t{self.score}\t{self.balls_faced}\t{self.sixes}\t{self.fours}\n')
        print(div)
        
    def display_bowling_stats(self):
        div = '-'*40
        print(f'{self.id}\t{self.name}\t{self.overs}\t{self.runs_given}\t{self.wickets}\t{self.maiden}\t{self.economy}\n')
        print(div)


    def add_runs_to_bowler(self,runs):
        self.runs_given+=runs

    def add_wicket(self):
        self.wickets+=1

    def set_player_id(self,id):
        self.id = id


