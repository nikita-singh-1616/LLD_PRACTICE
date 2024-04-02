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
            player = self.bowling_team.send_specified_player(input('enter the player id that you want bowl this over. '))
            if not player:
                print('invalid id, select again!')
            else:
                self.bowler = player
                self.bowler.add_overs()
                
    def start(self):
        i = 0
        while i<6:
            if self.score_to_meet or self.score_to_meet==0:
                if self.score_to_meet<=0:
                    self.striker = None
                    self.non_striker = None
                    print(f'{self.batting_team.team_name} has won!!')
                    break
            print(f'STRIKER-{self.striker.name}\nNON-STRIKER-{self.non_striker.name}')
            inp = input('enter the ball reading ')
            runs = ['0','1','2','3','4','5','6']
            if inp in runs:
                score = int(inp)
                self.balls.append(inp)
                self.batting_team.add_score(score)
                self.striker.update_batting_scores(score)
                self.bowler.add_runs_to_bowler(score)
                self.meet_score(score)
                if score%2!=0:
                    self.striker,self.non_striker=self.non_striker,self.striker
                i+=1
            elif inp == 'wd':
                self.balls.append(inp)
                self.bowler.add_runs_to_bowler(1)
                self.batting_team.add_score(1)
                self.meet_score(1)
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
        if self.score_to_meet:
            self.score_to_meet-=inp
