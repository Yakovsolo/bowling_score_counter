from os import  system
import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class BowlingGame:

    def get_number_of_players(self) -> int:
        number_of_players = input('Please enter the number of players (from one to six): ')

        try:
            players = int(number_of_players)
            if players >= 1 and players <= 6:
                logging.info(f'{number_of_players} players entered to play')
                return players 
        
        except ValueError:
            print(f'You must enter an integer from one to six!')
            logging.error(f'You must enter an integer from one to six! {number_of_players} is not an integer!')
            return self.get_number_of_players()
        else:
            print(f'You must enter an integer from one to six!')
            logging.error(f'You must enter an integer from one to six! {number_of_players} is out of range from one to six!')
            return self.get_number_of_players()


class Player(BowlingGame):
    players_list: list = []
    list_of_numbers = ['first player', 'second player',
                       'third player', 'fourth player', 'fifth player', 'sixth player']

    def __init__(self) -> None:
        super().__init__()
        self.number_of_players = self.get_number_of_players()

    def input_player_names(self) -> list:
        for number in range(self.number_of_players):
            player_name = input(f"PLease input {self.list_of_numbers[number]}'s name: ").upper()
            if len(player_name) > 3:
                player_name = player_name[0:3]
            self.players_list.append(player_name)
        return (self.players_list)


class Frame(Player, BowlingGame):
    
    NUMBER_OF_FRAMES = 10
    list_of_frames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    frames = ['first frame', 'second frame', 'third frame', 'fourth frame', 'fifth frame',
              'sixth frame', 'seventh frame', 'eighth frame', 'ninth frame', 'tenth frame']
    list_of_throws = ['first throw', 'second throw', 'third throw']
    total_score: dict = {}
    frame_score: dict = {}
    frame_total_score: dict = {}

    def __init__(self) -> None:
        super().__init__()
        self.players_list = self.input_player_names()
        self.frame_score = self.get_frame_score()
        self.frame_total_score = self.get_frame_total_score()
        self.total_score = self.get_total_score()

    def get_frame_score(self) -> dict:
        frame_score = {frame: {player: {throws: '0' for throws in self.list_of_throws}
                               for player in self.players_list} for frame in self.list_of_frames}

        return frame_score

    def get_frame_total_score(self) -> dict:
        frame_total_score = {frame: {
            player: ' ' for player in self.players_list} for frame in self.list_of_frames}
        return frame_total_score

    def get_total_score(self) -> dict:
        total_score = {player: ' ' for player in self.players_list}
        return total_score
    
    def clear_console(self):
        system('cls')

    def print_score_table(self) -> None:
        self.clear_console()
        print("\n")
        print("\t+-------------+-----------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+-------------+")
        print("\t| Player name |   Frame   |   1   |   2   |   3   |   4   |   5   |   6   |   7   |   8   |   9   |     10    | Total score |")
        print('\t+-------------+-----------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+-------------+')
        for player_name in self.players_list:
            print('\t+-------------+-----------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+-------------+')
            print("\t|             |   Score   | "
                  + str(self.frame_score[1][player_name]['first throw']) + " | " + str(
                      self.frame_score[1][player_name]['second throw']) + " | "
                  + str(self.frame_score[2][player_name]['first throw']) + " | " + str(
                      self.frame_score[2][player_name]['second throw']) + " | "
                  + str(self.frame_score[3][player_name]['first throw']) + " | " + str(
                      self.frame_score[3][player_name]['second throw']) + " | "
                  + str(self.frame_score[4][player_name]['first throw']) + " | " + str(
                      self.frame_score[4][player_name]['second throw']) + " | "
                  + str(self.frame_score[5][player_name]['first throw']) + " | " + str(
                      self.frame_score[5][player_name]['second throw']) + " | "
                  + str(self.frame_score[6][player_name]['first throw']) + " | " + str(
                      self.frame_score[6][player_name]['second throw']) + " | "
                  + str(self.frame_score[7][player_name]['first throw']) + " | " + str(
                      self.frame_score[7][player_name]['second throw']) + " | "
                  + str(self.frame_score[8][player_name]['first throw']) + " | " + str(
                      self.frame_score[8][player_name]['second throw']) + " | "
                  + str(self.frame_score[9][player_name]['first throw']) + " | " + str(
                      self.frame_score[9][player_name]['second throw']) + " | "
                  + str(self.frame_score[10][player_name]['first throw']) + " | " + str(
                      self.frame_score[10][player_name]['second throw']) + " | " + str(
                      self.frame_score[10][player_name]['third throw'])
                  + " |             |")
            print('\t+' + ' '*int(round((12.9-len(player_name))/2, 0)) + player_name + ' '*(int(round((13-len(player_name))/2, 0))) +
                  '+-----------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+'
                  + " " * int(round(((12.9-len(str(self.total_score[player_name])))/2), 0)) + str(
                      self.total_score[player_name])
                  + " " * int(round(((13-len(str(self.total_score[player_name])))/2), 0)) + '+')

            print("\t|             |Frame Score|" + " " * int(round(((7-len(str(self.frame_total_score[1][player_name])))/2) + 0.1, 0)) + str(self.frame_total_score[1][player_name])
                  + " " *
                  int(round(
                      ((7-len(str(self.frame_total_score[1][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[2][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[2][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[2][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[3][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[3][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[3][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[4][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[4][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[4][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[5][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[5][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[5][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[6][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[6][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[6][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[7][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[7][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[7][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[8][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[8][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[8][player_name])))/2), 0)) + "|"
                  + " " * int(round(((7-len(str(self.frame_total_score[9][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[9][player_name]) + " " * int(round(((7-len(str(self.frame_total_score[9][player_name])))/2), 0)) + "|"
                  + " " * int(round(((11-len(str(self.frame_total_score[10][player_name])))/2) + 0.1, 0)) + str(
                      self.frame_total_score[10][player_name])
                  + " " * int(round(((11-len(str(self.frame_total_score[10][player_name])))/2), 0)) + "|             |")
            print("\t+-------------+-----------+-------+-------+-------+-------+-------+-------+-------+-------+-------+-----------+-------------+")


    def count_frame_score(self) -> dict:
        
        frame = 1
        self.print_score_table()
        for frame in range(1, 11):
            for player in self.players_list:
                count = 0
                for throw in self.list_of_throws:

                    self.frame_score[frame][player][throw] = int(input(f'Enter {self.frames[frame-1]} {player} {throw} score: '))
                    # try 

                    self.frame_total_score[frame][player] = self.frame_score[frame][player][throw]

                    if frame == 1:
                        if self.frame_score[frame][player]['first throw'] == 10:
                            self.frame_total_score[frame][player] = int(self.frame_score[frame][player]['first throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.print_score_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10 and int(self.frame_score[frame][player]['first throw']) + int(
                            self.frame_score[frame][player]['second throw']) == 10:

                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.frame_score[frame][player]['second throw'] = '/'
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break
                        
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break

                    elif frame == 2:
                        if self.frame_score[frame-1][player]['first throw'] == 'X':
                            self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(
                                self.frame_score[frame][player][throw])

                        if self.frame_score[frame-1][player]['second throw'] == '/':
                            if throw == 'first throw':
                                self.frame_total_score[frame-1][player] += int(
                                    self.frame_score[frame][player]['first throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()

                        if self.frame_score[frame][player]['first throw'] == 10:
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(
                                self.frame_score[frame][player]['first throw'])
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10:

                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            if self.frame_score[frame][player]['first throw'] + int(self.frame_score[frame][player]['second throw']) == 10:
                                self.frame_score[frame][player]['second throw'] = '/'
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break
                        
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break
                            count += 1

                    elif 2 < frame < 10:
                        print(f'frame {frame}')

                        if self.frame_score[frame-2][player]['first throw'] == 'X':
                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-2][player] = self.frame_total_score[frame-2][player] + int(self.frame_score[frame][player]['first throw'])
                            
                        self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player]
                        if self.frame_score[frame-1][player]['first throw'] == 'X':

                            self.frame_total_score[frame-1][player] += self.frame_score[frame][player][throw]
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()

                        if self.frame_score[frame-1][player]['second throw'] == '/':
                            if throw == 'first throw':
                                self.frame_total_score[frame-1][player] += int(
                                    self.frame_score[frame][player]['first throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()

                        if self.frame_score[frame][player]['first throw'] == 10:
                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player][throw])
                                self.total_score[player] = self.frame_total_score[frame][player]
                                self.print_score_table()
                            
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw'])
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10:

                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(
                                self.frame_score[frame][player]['second throw'])
                            if self.frame_score[frame][player]['first throw'] + int(self.frame_score[frame][player]['second throw']) == 10:
                                self.frame_score[frame][player]['second throw'] = '/'
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_score_table()
                            count += 1
                            if count == 2:
                                break
                            
                    elif frame == 10:
                        self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player]
                        if self.frame_score[frame][player]['first throw'] == 'X':
                            self.frame_score[frame][player]['first throw'] = 10
                        if self.frame_score[frame][player]['second throw'] == 'X':
                            self.frame_score[frame][player]['second throw'] = 10
                        if self.frame_score[frame][player]['third throw'] == 'X':
                            self.frame_score[frame][player]['third throw'] = 10
                        if self.frame_score[frame][player]['second throw'] == '/':
                            self.frame_score[frame][player]['second throw'] = 10 - \
                                self.frame_score[frame][player]['first throw']

                        if self.frame_score[frame-2][player]['first throw'] == 'X':
                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                if throw == 'first throw':
                                    self.frame_total_score[frame-2][player] = self.frame_total_score[frame-2][player] + self.frame_score[frame][player]['first throw']

                        if self.frame_score[frame][player]['first throw'] == 10:
                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-1][player] += int(
                                    self.frame_score[frame][player]['first throw'])
                                self.frame_total_score[frame][player] += int(
                                    self.frame_score[frame][player]['second throw'])
                                self.frame_total_score[frame][player] += int(
                                    self.frame_score[frame][player]['third throw'])

                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw'])
                            self.frame_total_score[frame][player] += int(
                                self.frame_score[frame][player]['second throw'])
                            self.frame_total_score[frame][player] += int(
                                self.frame_score[frame][player]['third throw'])

                            self.total_score[player] = self.frame_total_score[frame][player]

                        if self.frame_score[frame][player]['first throw'] != 10:

                            if throw == 'third throw':
                                if int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw']) == 10:
                                    self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['second throw'])
                                    self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(
                                        self.frame_score[frame][player]['first throw']) + self.frame_score[frame][player]['second throw'] + int(
                                        self.frame_score[frame][player]['third throw'])
                                    if self.frame_score[frame][player]['first throw'] + self.frame_score[frame][player]['second throw'] == 10:
                                        self.frame_score[frame][player]['second throw'] = '/'
                                    if self.frame_score[frame][player]['third throw'] == '0':
                                        self.frame_score[frame][player]['third throw'] = ' '
                                    self.total_score[player] = self.frame_total_score[frame][player]
                                    self.print_score_table()
                                    break

                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(
                                    self.frame_score[frame][player]['second throw'])
                                
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(
                                self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]

                            if throw == 'second throw':
                                if int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw']) != 10:
                                    self.frame_score[frame][player]['third throw'] = ' '
                                    self.print_score_table()
                                    break

                        self.total_score[player] = self.frame_total_score[frame][player]
                        if int(self.frame_score[frame][player]['first throw']) == 10:
                            self.frame_score[frame][player]['first throw'] = 'X'
                        if int(self.frame_score[frame][player]['second throw']) == 10:
                            self.frame_score[frame][player]['second throw'] = 'X'
                        if int(self.frame_score[frame][player]['third throw']) == 10:
                            self.frame_score[frame][player]['third throw'] = 'X'
                        if int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw']) == 10:
                            self.frame_score[frame][player]['second throw'] = '/'
                        self.print_score_table()

        return self.frame_score

if __name__=='__main__':

    player = Frame()

    player.count_frame_score()

