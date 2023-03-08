import logging

logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


class BowlingGame:

    NUMBER_OF_FRAMES = 10
    list_of_frames = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    frames = ['first frame', 'second frame', 'third frame', 'fourth frame', 'fifth frame',
              'sixth frame', 'seventh frame', 'eighth frame', 'ninth frame', 'tenth frame']
    list_of_numbers = ['first player', 'second player',
                       'third player', 'fourth player', 'fifth player', 'sixth player']
    list_of_throws = ['first throw', 'second throw', 'third throw']
    players_list: list = []
    total_score: dict = {}
    frame_score: dict = {}
    frame_total_score: dict = {}

    def __init__(self, number_of_frames=NUMBER_OF_FRAMES,) -> None:
        self.number_of_frames = number_of_frames
       

    def get_number_of_players(self) -> int:
        number_of_players = int(input('Please enter the number of players (from one to six): '))
        # try:
        #     self.get_number_of_players()
        # except 
        return number_of_players
          

class Player(BowlingGame):

    def __init__(self) -> None:
        
        
        super().__init__()
        self.number_of_players = self.get_number_of_players()

    def input_player_names(self) -> list:
        for number in range(self.number_of_players):
            player = input(f"PLease input {self.list_of_numbers[number]}'s name (first three letters): ").upper()
            self.players_list.append(player)
        return (self.players_list)


class Frame(Player, BowlingGame):

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

    def print_empty_table(self) -> None:
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
        self.print_empty_table()
        for frame in range(1, 11):
            for player in self.players_list:
                count = 0
                for throw in self.list_of_throws:

                    self.frame_score[frame][player][throw] = int(
                        input(f'Enter {self.frames[frame-1]} {player} {throw} score: '))
                    self.frame_total_score[frame][player] = self.frame_score[frame][player][throw]

                    if frame == 1:
                        if self.frame_score[frame][player]['first throw'] == 10:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.print_empty_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10 and int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw']) == 10:

                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.frame_score[frame][player]['second throw'] = '/'
                            self.print_empty_table()
                            count += 1
                            if count == 2:
                                break
                        
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
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
                            self.print_empty_table()

                        if self.frame_score[frame][player]['first throw'] == 10:
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(
                                self.frame_score[frame][player]['first throw'])
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10:

                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            if self.frame_score[frame][player]['first throw'] + int(self.frame_score[frame][player]['second throw']) == 10:
                                self.frame_score[frame][player]['second throw'] = '/'
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
                            count += 1
                            if count == 2:
                                break
                        
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
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
                            self.print_empty_table()

                        if self.frame_score[frame-1][player]['second throw'] == '/':
                            if throw == 'first throw':
                                self.frame_total_score[frame-1][player] += int(
                                    self.frame_score[frame][player]['first throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()

                        if self.frame_score[frame][player]['first throw'] == 10:
                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player][throw])
                                self.total_score[player] = self.frame_total_score[frame][player]
                                self.print_empty_table()
                            
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw'])
                            self.frame_score[frame][player]['first throw'] = 'X'
                            self.frame_score[frame][player]['second throw'] = ' '
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
                            break

                        elif int(self.frame_score[frame][player]['first throw']) != 10:

                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            if self.frame_score[frame][player]['first throw'] + int(self.frame_score[frame][player]['second throw']) == 10:
                                self.frame_score[frame][player]['second throw'] = '/'
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
                            count += 1
                            if count == 2:
                                break
                        else:
                            self.frame_total_score[frame][player] = int(
                                self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]
                            self.print_empty_table()
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
                                    self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + self.frame_score[frame][player]['second throw'] + int(self.frame_score[frame][player]['third throw'])
                                    if self.frame_score[frame][player]['first throw'] + self.frame_score[frame][player]['second throw'] == 10:
                                        self.frame_score[frame][player]['second throw'] = '/'
                                    if self.frame_score[frame][player]['third throw'] == '0':
                                        self.frame_score[frame][player]['third throw'] = ' '
                                    self.total_score[player] = self.frame_total_score[frame][player]
                                    self.print_empty_table()
                                    break

                            if self.frame_score[frame-1][player]['first throw'] == 'X':
                                self.frame_total_score[frame-1][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                                
                            self.frame_total_score[frame][player] = self.frame_total_score[frame-1][player] + int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw'])
                            self.total_score[player] = self.frame_total_score[frame][player]

                            if throw == 'second throw':
                                if int(self.frame_score[frame][player]['first throw']) + int(self.frame_score[frame][player]['second throw']) != 10:
                                    self.frame_score[frame][player]['third throw'] = ' '
                                    self.print_empty_table()
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
                        self.print_empty_table()

        return self.frame_score




player = Frame()


player.count_frame_score()

