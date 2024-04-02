

from classes.players_list import MatchPlayer


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
        self.team_name = input('enter the name of the team ')
        print('enter the team member details in order of the batting order.')
        for i in range(self.size):
            while True:
                inp = input(f'enter player id or enter new to add a new player ')
                if inp == 'new':
                    player = self.player_list.add_new_player()
                else:
                    player = self.player_list.search_players(inp)
                if player:
                    """check if player is booked"""
                    if self.player_list.search_booked_players(inp):
                        print('Player already booked')
                    else:
                        break
                else:
                    print('Player not found.')
            match_player = MatchPlayer(player.name,player)
            self.team.append(match_player)
            self.player_list.book_player(player)
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