import random
from classes.players_list import Player, PlayersList

from interfaces.player_interface import PlayerInterface

class MatchPlayer(PlayerInterface):
    def __init__(self, name,player) -> None:
        super().__init__(name)
        self.player = player
        self.name = name

    def update_batting_scores(self,runs):
        team_player_update = super().update_batting_score(runs)
        self.player.update_batting_score(runs)

    def add_runs_to_bowler(self,runs):
        add_runs_to_team_player = super().add_runs_to_bowler(runs)
        self.player.add_runs_to_bowler(runs)

    def add_wicket(self):
        add_team_player_wicket = super().add_wicket()
        self.player.add_wicket()
        
class Team:
    def __init__(self,size,players_list):
        self.team_name = None
        self.size = size
        self.team = []
        self.score = 0
        self.player_list = players_list
        self.make_team()
        self.i = 0
    
    def make_team(self):
        self.team_name = input('enter the name of the team')
        print('enter the team member details in order of the batting order.')
        for i in range(self.size):
            self.player_list.view_players()
            while True:
                inp = input(f'enter player id or enter new to add a new player')
                if inp == 'new':
                    player = self.player_list.add_new_player()
                else:
                    player = self.player_list.search_players(inp)
                if player:
                    break
            match_player = MatchPlayer(player.name,player)
            self.team.append(match_player)
            print(f'{player.name} added successfully')
            
    def show_batting_team(self):
        print(f'TEAM {self.team_name}')
        div = '-'*40
        print(f'Name\tRuns\tBalls\tsixes\tfours\n')
        for i in self.team:
            i.display_batting_player_score()
            
    def show_team(self):
        print(f'TEAM {self.team_name}')
        div = '-'*40
        print(f'Id\tName\n')
        for i in self.team:
            print(f'{i.player.id}\t{i.name}')
            
    def add_score(self,runs):
        self.score+=runs
    
    def send_player(self):
        if self.i>=self.size:
            return False
        player = self.team[self.i]
        self.i+=1
        return player
    
    def send_specified_player(self,index):
        for i in self.team:
            if i.player.id == index:
                return i
        return False

    
    
class Over:
    def __init__(self,batting,bowling,striker,non_striker,score):
        self.balls = []
        self.batting_team = batting
        self.bowling_team = bowling
        self.bowler = None
        self.striker = striker
        self.non_striker = non_striker
        self.score_to_meet = score
        self.assign_bowler()
        self.validate()
    
    def validate(self):
        print('VALIDATING')
        if not self.striker or not self.non_striker:
            return False
        else:
            self.start()
        
    def assign_batsmen(self):
        player = self.batting_team.send_player()
        if not player:
            print('No batsmen available.')
            return False
        return player
    
    def assign_bowler(self):
        print('ASSIGNING BOWLER')
        self.bowling_team.show_team()
        while not self.bowler:
            player = self.bowling_team.send_specified_player(int(input('enter the player id that you want bowl this over. ')))
            if not player:
                print('invalid id, select again!')
            else:
                self.bowler = player
                
    def start(self):
        i = 0
        while i<6:
            if self.score_to_meet<=0:
                self.striker = None
                self.non_striker = None
                print(f'{self.batting_team.team_name} has won!!')
                break
            print(f'STRIKER-{self.striker.name}\nNON-STRIKER-{self.non_striker.name}')
            inp = input('enter the ball reading')
            runs = ['0','1','2','3','4','5','6']
            if inp in runs:
                score = int(inp)
                self.balls.append(inp)
                self.batting_team.add_score(score)
                self.striker.update_batting_score(score)
                self.bowler.add_runs_to_bowler(score)
                if score%2!=0:
                    self.striker,self.non_striker=self.non_striker,self.striker
                i+=1
            elif inp == 'wd':
                self.balls.append(inp)
                self.bowler.add_runs_to_bowler(1)
                self.batting_team.add_score(1)
            elif inp == 'w':
                self.balls.append(inp)
                self.striker = self.batting_team.send_player()
                self.bowler.add_wicket()
                i+=1
                if not self.striker:
                    break
            else:
                print('unknown input...enter a valid input.')
        self.batting_team.show_batting_team()
        print(self.balls)
        print('------------------------------------------------------')
        print('SCORE-'+str(self.batting_team.score))
    def meet_score(self,inp):
        self.score_to_meet-=inp

                
    
class Match:
    def __init__(self,players_list):
        self.team1 = None
        self.team2 = None
        self.overs = 0
        self.over_rec = []
        self.striker = None
        self.non_striker = None
        self.score = 0
        self.batting_team = None
        self.bowling_team = None
        self.players_list = players_list
        self.welcome()
        
        
    def welcome(self):
        print('Hello Chief!! Lets play some cricket!!')
        team_size = int(input('enter the team size:'))
        self.overs = int(input('enter the number of overs:'))
        self.team1 = Team(team_size,self.players_list)
        self.team1.show_team()
        self.team2 = Team(team_size,self.players_list)
        self.team2.show_team(self.players_list)
        self.toss()

    def toss(self):
        print('ITS TIME FOR TOSS!!')
        toss_obj =Toss(self.team1,self.team2)
        self.batting_team,self.bowling_team=toss_obj.chose()
        print(f'Batting Team-{self.batting_team.team_name}')
        print(f'Bowling Team-{self.bowling_team.team_name}')
        self.striker = self.assign_batsmen()
        self.non_striker = self.assign_batsmen()
        self.start_innings()

    def start_innings(self):
        for i in range(self.overs):
            print(f'STARTING OVER {i+1}')
            current_over = Over(self.batting_team,self.bowling_team,self.striker,self.non_striker,None)
            self.over_rec.append(current_over)
            self.striker = current_over.non_striker
            self.non_striker = current_over.striker
            if not self.striker or not self.non_striker:
                self.score = self.team1.score
                break
        self.score = self.batting_team.score
        self.batting_team.show_batting_team()
        self.start_second_innings()

    def start_second_innings(self):
        print('STARTING SECOND INNINGS')
        for i in range(self.overs):
            print(f'STARTING OVER {i+1}')
            current_over = Over(self.batting_team,self.bowling_team,self.striker,self.non_striker,self.score)
            self.over_rec.append(current_over)
            self.striker = current_over.non_striker
            self.non_striker = current_over.striker
            if not self.striker or not self.non_striker:
                self.score = self.team1.score
                break
        self.score = self.batting_team.score
        self.batting_team.show_batting_team()
          
    def assign_batsmen(self):
        player = self.batting_team.send_player()
        if not player:
            print('No batsmen available.')
            return False
        return player

class Toss:
    def __init__(self,team1,team2):
        self.team1 = team1
        self.team2 = team2
        self.calling_team = None
        self.not_calling_team = None

    
    def chose(self):
        choice = self.validate_choice([self.team1.team_name,self.team2.team_name])
        if choice == self.team1.team_name:
            self.calling_team = self.team1
            self.not_calling_team = self.team2
        else:
            self.calling_team = self.team2
            self.not_calling_team = self.team1
            
        print(f'{self.calling_team.team_name} you will be calling the toss')
        heads_or_tails = self.validate_choice(['Heads','Tails'])
        toss_val = self.toss()
        print(toss_val)
        if toss_val == heads_or_tails:
            print(f'{self.calling_team.team_name} has won the toss')
            choice = self.validate_choice(['Bat','Bowl'])
            if choice == 'Bat':
                return [self.calling_team,self.not_calling_team]
            else:
                return [self.not_calling_team,self.calling_team]
        else:
            print(f'{self.not_calling_team.team_name} has won the toss')
            choice = self.validate_choice(['Bat','Bowl'])
            if choice == 'Bat':
                return [self.not_calling_team,self.calling_team]
            else:
                return [self.calling_team,self.not_calling_team]
    
    def validate_choice(self,choices):
        while True:
            choice = input(f'Do you want to {choices[0]} or {choices[1]} first?')
            if choice not in choices:
                print(f'Invalid choice, your choices are {choices[0]} and {choices[1]}')
            else:
                return choice

        
    def toss(self):
        return random.choice(['Heads', 'Tails'])
    
        
# start_match = Match()        
        
            

