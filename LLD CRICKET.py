#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random


class Player:
    def __init__(self,name):
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
        print(f'{self.name}\t{self.score}\t{self.balls_faced}\t{self.sixes}\t{self.fours}\n')
        print(div)
        
    def display_bowling_stats(self):
        div = '-'*40
        print(f'{self.name}\t{self.overs}\t{self.runs}\t{self.wickets}\t{self.maiden}\t{self.economy}\n')
        print(div)

    def add_runs_to_bowler(self,runs):
        self.runs_given+=runs

    def add_wicket(self):
        self.wickets+=1
        
class Team:
    def __init__(self,size):
        self.team_name = None
        self.size = size
        self.team = []
        self.score = 0
        self.make_team()
        self.i = 0
    
    def make_team(self):
        self.team_name = input('enter the name of the team')
        print('enter the team member details in order of the batting order.')
        for i in range(self.size):
            inp = input(f'enter player {i} name ')
            player = Player(inp)
            self.team.append(player)
            
    def show_batting_team(self):
        print(f'TEAM {self.team_name}')
        div = '-'*40
        print(f'Name\tRuns Scored\tBalls\tsixes\tfours\n')
        for i in self.team:
            i.display_batting_player_score()
            
    def show_team(self):
        print(f'TEAM {self.team_name}')
        div = '-'*40
        print(f'Id\tName\n')
        for i in self.team:
            print(f'{self.team.index(i)}\t{i.name}')
            
    def add_score(self,runs):
        self.score+=runs
    
    def send_player(self):
        if self.i>=self.size:
            return False
        player = self.team[self.i]
        self.i+=1
        return player
    
    def send_specified_player(self,index):
        if index>=self.size:
            return False
        return self.team[index]

    
    
class Over:
    def __init__(self,batting,bowling,striker,non_striker):
        self.balls = []
        self.batting_team = batting
        self.bowling_team = bowling
        self.bowler = None
        self.striker = striker
        self.non_striker = non_striker
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

                
    
class Match:
    def __init__(self):
        self.team1 = None
        self.team2 = None
        self.overs = 0
        self.over_rec = []
        self.striker = None
        self.non_striker = None
        self.score = 0
        self.batting_team = None
        self.bowling_team = None
        self.welcome()
        
        
    def welcome(self):
        print('Hello Chief!! Lets play some cricket!!')
        team_size = int(input('enter the team size'))
        self.overs = int(input('enter the number of overs'))
        self.team1 = Team(team_size)
        self.team1.show_team()
        self.team2 = Team(team_size)
        self.team2.show_team()
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
            current_over = Over(self.batting_team,self.bowling_team,self.striker,self.non_striker)
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
    
    def chose(self):
        inp = input('Team1 choose heads or tails(H/T)')
        if inp not in ['H','T']:
            print('invalid choice please try again')
            return self.chose()
        toss_val = self.toss()
        print(toss_val)
        if toss_val == inp:
            return [self.team1,self.team2]
        return [self.team2,self.team1]

        
    def toss(self):
        return random.choice(['H', 'T'])
    
        
start_match = Match()        
        
            

