


from classes.match import Match
from classes.players_list import PlayersList


class Main:
    def __init__(self) -> None:
        self.player_list = PlayersList()
        self.introduction()

    def introduction(self):
        while True:
            try:
                inp = int(input(f'Hi User.Press 1 to add a new player,\nPress 2 to view all the players\nPress 3 to start a match.\n Press 4 to exit.'))
            except:
                print('Invalid Input')
                continue
            if inp == 1:
                self.player_list.add_new_player()
            elif inp == 2:
                self.player_list.view_players()
            elif inp == 3:
                start_match = Match(self.player_list)
            elif inp == 4:
                break
            else:
                print('Invalid Input')

start = Main()

        