from LLD_Cricket.classes.team import Team
from classes.overs import Over
from classes.toss import Toss                
    
class Match:
    def __init__(self,players_list):
        self.team1 = None
        self.team2 = None
        self.overs = 0
        self.over_rec = []
        self.striker = None
        self.non_striker = None
        self.inning1_score = 0
        self.inning2_score = 0
        self.batting_team = None
        self.bowling_team = None
        self.players_list = players_list
        self.welcome()
        
        
    def welcome(self):
        print('Hello Chief!! Lets play some cricket!!')
        team_size = int(input('enter the team size: '))
        self.overs = int(input('enter the number of overs: '))
        self.team1 = Team(team_size,self.players_list)
        self.team1.show_team()
        self.team2 = Team(team_size,self.players_list)
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
            current_over = Over(self.batting_team,self.bowling_team,self.striker,self.non_striker,None)
            self.over_rec.append(current_over)
            self.striker = current_over.non_striker
            self.non_striker = current_over.striker
            if not self.striker or not self.non_striker:
                self.inning1_score = self.batting_team.score
                break
            self.inning1_score = self.batting_team.score
        # self.batting_team.show_batting_team()
        self.start_second_innings()

    def start_second_innings(self):
        print('STARTING SECOND INNINGS')
        self.bowling_team,self.batting_team = self.batting_team,self.bowling_team
        self.striker = self.assign_batsmen()
        self.non_striker = self.assign_batsmen()
        for i in range(self.overs):
            print(f'STARTING OVER {i+1}')
            current_over = Over(self.batting_team,self.bowling_team,self.striker,self.non_striker,self.inning1_score-self.inning2_score)
            self.over_rec.append(current_over)
            self.striker = current_over.non_striker
            self.non_striker = current_over.striker
            if not self.striker or not self.non_striker:
                if self.inning1_score > self.batting_team.score:
                    print(f'{self.batting_team.team_name} lost the chase.')
                    print(f'{self.bowling_team.team_name} Won the match.')
                    break
                else:
                    print(f'{self.bowling_team.team_name} lost the chase.')
                    print(f'{self.batting_team.team_name} Won the match.')
                    break
            self.inning2_score = self.batting_team.score
        self.batting_team.show_batting_team()

    def release_players(self):
        for i in self.batting_team:
            self.players_list.release_player(i)
        for i in self.bowling_team:
            self.players_list.release_player(i)
          
    def assign_batsmen(self):
        player = self.batting_team.send_player()
        if not player:
            print('No batsmen available.')
            return False
        return player

