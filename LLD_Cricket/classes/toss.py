import random


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