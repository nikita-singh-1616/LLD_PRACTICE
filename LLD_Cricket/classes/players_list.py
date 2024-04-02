

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

    def add_overs(self):
        add_team_player_over = super().add_overs()
        self.player.add_overs()
        
class Player(PlayerInterface):
    def __init__(self,name):
        super().__init__(name)
        self.name = name

class PlayersList:
    def __init__(self):
        self.player_list = []
        self.booked_list = []

    def add_new_player(self):
        player_name = input('enter player name ')
        player = Player(player_name)
        player_id = input('enter player Id ')
        if not self.search_players(player_id):
            player.set_player_id(player_id)
        else:
            print('player already exists.')
            return False
            
        self.player_list.append(player)
        return player

    def view_players(self):
        print('PLAYER LIST')
        print('Displaying bowling stats of all the available players')
        print(f'Id\tName\tOvers\tRuns\tWickets\tMaiden\tEconomy')
        for i in self.player_list:
            i.display_bowling_stats()
        print('Displaying the batting stats of all the players')
        print(f'Id\tName\tRuns\tBalls\tsixes\tfours\n')
        for i in self.player_list:
            i.display_batting_player_score()

    def search_players(self,id):
        for i in self.player_list:
            if i.id == id:
                return i
        return False
    def search_booked_players(self,id):
        for i in self.booked_list:
            if i.id == id:
                return i
        return False
    def book_player(self,player):
        self.booked_list.append(player)

    def release_player(self,player):
        self.player_list.remove(player)
    