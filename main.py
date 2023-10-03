import random


class Player:
    """A class to represent a player"""
    def __init__(self, player_position):
        self._player_position = player_position
        self._start_pos = None
        self._end_pos = None
        self._current_pos = ["H", "H"]
        self._status = False
        self._token_p_step_count = -1
        self._token_q_step_count = -1
        self._token_stacked = False
        self._home_square = []

    def get_player_position(self):
        """returns the player position by returning A, B, C, or D"""
        return self._player_position

    def get_completed(self):
        """returns boolean that determines if the player finished the game"""
        for pos in self._current_pos:
            if pos != "E":
                self._status = False
                return self._status
        self._status = True
        return self._status

    def get_token_p_step_count(self):
        """returns the total steps token p has taken"""
        return self._token_p_step_count

    def get_token_q_step_count(self):
        """returns the total steps token q has taken"""
        return self._token_q_step_count

    def get_home_square(self):
        """returns a list of the player's home squares and the end position"""
        for num in range(1, 7):
            self._home_square.append(self._player_position + str(num))
        self._home_square.append("E")
        return self._home_square

    def get_space_name(self, total_steps):
        """returns the name of the space the token has landed given total steps of a token and """
        board = ["R", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
                 51, 52, 53, 54, 55, 56, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, "H"]

        if total_steps > 57:
            bounce_back_steps = total_steps - 57
            return self.get_home_square()[-bounce_back_steps-1]

        elif total_steps > 50:
            home_steps = total_steps - 50
            return self.get_home_square()[home_steps-1]

        elif total_steps == -1 or total_steps == 0:
            return str(board[total_steps])

        elif self._start_pos == 0:
            return str(board[total_steps])

        else:
            return str(board[board.index(self._start_pos) + total_steps])

    def set_start_pos(self, player_position):
        """determines the starting position based on the player's position"""
        if player_position == "A":
            self._start_pos = 0

        elif player_position == "B":
            self._start_pos = 14

        elif player_position == "C":
            self._start_pos = 28

        elif player_position == "D":
            self._start_pos = 42

    def set_end_pos(self, player_position):
        """determines the ending position based on the player's position"""
        if player_position == "A":
            self._end_pos = 50

        elif player_position == "B":
            self._end_pos = 8

        elif player_position == "C":
            self._end_pos = 22

        elif player_position == "D":
            self._end_pos = 36

    def get_current_pos(self):
        """returns a list of the current position of both tokens"""
        token_p = self._current_pos[0]
        self._current_pos[0] = str(token_p)

        token_q = self._current_pos[1]
        self._current_pos[1] = str(token_q)

        return self._current_pos

    def update_token_p_step_count(self, steps):
        """updates the token p step count"""
        self._token_p_step_count += steps

        if self._token_p_step_count > 57:
            bounce_back_step_num = self._token_p_step_count - 57
            self._token_p_step_count = 57 - bounce_back_step_num

    def update_token_q_step_count(self, steps):
        """updates the token q step count"""
        self._token_q_step_count += steps

        if self._token_q_step_count > 57:
            bounce_back_step_num = self._token_q_step_count - 57
            self._token_q_step_count = 57 - bounce_back_step_num

    def set_token_stacked(self):
        """changes status of tokens whether they are stacked or not"""
        if self._token_stacked:
            self._token_stacked = False
        else:
            self._token_stacked = True

    def get_token_stacked(self):
        """returns boolean that determines if tokens are stacked"""
        return self._token_stacked


class LudoGame:
    """A class to represent LudoGame"""
    def __init__(self):
        # self._num_of_players = None
        # self._players = ['A', 'B', 'C', 'D']
        self._player_list = []
        self._turns_list = []

    def update_player_list(self, player_object):
        """add players to player list and initialize their start and end position"""
        self._player_list.append(player_object)

        player_object.set_start_pos(player_object.get_player_position())
        player_object.set_end_pos(player_object.get_player_position())

    def get_player_list(self):
        """returns player list"""
        return self._player_list

    def get_player_by_position(self, player_position):
        """returns player object given player's position: A, B, C, or D"""
        for player in self._player_list:

            if player.get_player_position() == player_position:
                return player

        return "Player not found!"

    def move_token(self, player_object, token_name, steps):
        """updates player's token step count and player's current position given player, token name,
         and number of steps"""

        # considering player's token p
        if token_name == "p":

            # update player's p step count
            player_object.update_token_p_step_count(steps)
            potential_p_space = player_object.get_space_name(player_object.get_token_p_step_count())

            # create list of opponents
            opponent_list = self.get_player_list().copy()
            opponent_list.remove(player_object)

            # check if we can kick opponent token
            for current_opponent in opponent_list:

                for index in range(0, 2):

                    opponent_token = current_opponent.get_current_pos()[index]

                    # check if we can kick opponent's p token
                    if index == 0 and potential_p_space == opponent_token:

                        # check if opponent's p token on the general board
                        if opponent_token != "H" and opponent_token != "R" and opponent_token != "E":

                            opponent_p_steps = current_opponent.get_token_p_step_count()

                            # check if opponent's tokens are stacked to kick both tokens if needed
                            if current_opponent.get_token_stacked():
                                current_opponent.update_token_q_step_count(-opponent_p_steps - 1)
                                current_opponent.get_current_pos()[1] = "H"
                                current_opponent.set_token_stacked()

                            # kick opponent's p token back to home yard
                            current_opponent.update_token_p_step_count(-opponent_p_steps-1)
                            current_opponent.get_current_pos()[index] = "H"

                    # check if we can kick opponent's q token
                    elif index == 1 and potential_p_space == opponent_token:

                        # check if opponent's q token on the general board
                        if opponent_token != "H" and opponent_token != "R" and opponent_token != "E":

                            opponent_q_steps = current_opponent.get_token_q_step_count()

                            # check if opponent's tokens are stacked to kick both tokens if needed
                            if current_opponent.get_token_stacked() and index == 1:
                                current_opponent.update_token_p_step_count(-opponent_q_steps - 1)
                                current_opponent.get_current_pos()[0] = "H"
                                current_opponent.set_token_stacked()

                            # kick opponent's p token back to home yard
                            opponent_q_steps = current_opponent.get_token_q_step_count()
                            current_opponent.update_token_q_step_count(-opponent_q_steps-1)
                            current_opponent.get_current_pos()[index] = "H"

            # update player's p token position
            player_object.get_current_pos()[0] = potential_p_space

            # when player's tokens are stacked, token q's total step count and position are updated
            if player_object.get_token_stacked():
                player_object.update_token_q_step_count(steps)
                potential_q_space = player_object.get_space_name(player_object.get_token_q_step_count())
                player_object.get_current_pos()[1] = potential_q_space

            # we stack player's tokens when player's p token lands on player's q token
            elif potential_p_space == player_object.get_space_name(player_object.get_token_q_step_count()):
                if potential_p_space != "H" and potential_p_space != "R":
                    player_object.set_token_stacked()

        # considering player's token q
        elif token_name == "q":

            # update player's q step count
            player_object.update_token_q_step_count(steps)
            potential_q_space = player_object.get_space_name(player_object.get_token_q_step_count())

            # create list of opponents
            opponent_list = self.get_player_list().copy()
            opponent_list.remove(player_object)

            # check if we can kick opponent token
            for current_opponent in opponent_list:

                for index in range(0, 2):

                    opponent_token = current_opponent.get_current_pos()[index]

                    # check if we can kick opponent's p token
                    if index == 0 and potential_q_space == opponent_token:

                        # check if opponent's p token on the general board
                        if opponent_token != "H" and opponent_token != "R" and not current_opponent.get_completed():

                            opponent_p_steps = current_opponent.get_token_p_step_count()

                            # check if opponent's tokens are stacked to kick both tokens if needed
                            if current_opponent.get_token_stacked() and index == 0:
                                current_opponent.update_token_q_step_count(-opponent_p_steps - 1)
                                current_opponent.get_current_pos()[1] = "H"
                                current_opponent.set_token_stacked()

                            # kick opponent's p token back to home yard
                            current_opponent.update_token_p_step_count(-opponent_p_steps-1)
                            current_opponent.get_current_pos()[0] = "H"

                    # check if we can kick opponent's q token
                    elif index == 1 and potential_q_space == opponent_token:

                        opponent_q_steps = current_opponent.get_token_q_step_count()

                        # check if opponent's q token on the general board
                        if opponent_token != "H" and opponent_token != "R" and not current_opponent.get_completed():

                            # check if opponent's tokens are stacked to kick both tokens if needed
                            if current_opponent.get_token_stacked() and index == 1:
                                current_opponent.update_token_p_step_count(-opponent_q_steps - 1)
                                current_opponent.get_current_pos()[0] = "H"
                                current_opponent.set_token_stacked()

                            # kick opponent's p token back to home yard
                            current_opponent.update_token_q_step_count(-opponent_q_steps-1)
                            current_opponent.get_current_pos()[1] = "H"

            # update player's q token position
            player_object.get_current_pos()[1] = potential_q_space

            # we stack player's tokens when player's q token lands on player's p token
            if potential_q_space == player_object.get_space_name(player_object.get_token_p_step_count()):
                player_object.set_token_stacked()

        return

    def play_game(self):
        """return a list representing current spaces of all the tokens for each player given player list and
        turn list"""
        players_list = self.initialize_players()
        counter = 0
        while True:
            counter += 1
            print("round #" + str(counter))
            print(self.get_all_player_spaces())
            if counter == 1000:
                print("Tie Game! All players rolled 1000 times.")
            turns_list = self.play_one_round()

            # iterate through turns list
            for turn_index in range(len(turns_list)):

                current_player = self.get_player_by_position(turns_list[turn_index][0])
                current_steps = turns_list[turn_index][1]

                # verify if player is still active player
                if current_player.get_completed():
                    print("Player " + current_player.get_player_position() + " " + "wins!")
                    print("Final Results: " + str(self.get_all_player_spaces()))
                    return

                tokens_location = current_player.get_current_pos()

                # player's potential token locations to consider for decision
                potential_p_steps = current_player.get_token_p_step_count() + current_steps
                potential_q_steps = current_player.get_token_q_step_count() + current_steps

                # create list of opponent tokens on the board
                opponent_spaces = self.get_all_opponent_spaces(current_player)
                # all_opponent_spaces = []
                # for opponent in self.get_player_list():
                #     if opponent.get_player_position() != current_player.get_player_position():
                #         for index in range(0, 2):
                #             opponent_token = opponent.get_current_pos()[index]
                #             if opponent_token != "H" and opponent_token != "R" and opponent_token != "E":
                #                 all_opponent_spaces.append(opponent.get_current_pos()[index])

                # priority rule 1 for token p: token that can get out of home yard moves
                if current_steps == 6 and tokens_location[0] == "H":
                    self.move_token(current_player, "p", 1)

                # priority rule 1 for token q: token that can get out of home yard moves
                elif current_steps == 6 and tokens_location[1] == "H":
                    self.move_token(current_player, "q", 1)

                # priority rule 2 for token p: token that can reach end position moves
                elif potential_p_steps == 57:
                    self.move_token(current_player, "p", current_steps)
                    current_player.get_completed()

                # priority rule 2 for token q: token that can reach end position moves
                elif potential_q_steps == 57:
                    self.move_token(current_player, "q", current_steps)
                    current_player.get_completed()

                # priority rule 3 for token p : token that can kick opponent's token moves
                elif current_player.get_space_name(potential_p_steps) in opponent_spaces:

                    # check if both token p and q can kick opponent's token
                    if current_player.get_space_name(potential_q_steps) in opponent_spaces:

                        # the token that is closer to home will move and kick opponent's token
                        if current_player.get_token_p_step_count() > current_player.get_token_q_step_count():
                            self.move_token(current_player, "q", current_steps)
                        else:
                            self.move_token(current_player, "p", current_steps)

                    self.move_token(current_player, "p", current_steps)

                # priority rule 3 for token q: token that can kick opponent's token moves
                elif current_player.get_space_name(potential_q_steps) in opponent_spaces:
                    self.move_token(current_player, "q", current_steps)

                # priority rule 4: the token closer to home yard moves
                else:

                    # check if both tokens are out of home yard
                    if current_player.get_token_p_step_count() > -1 and current_player.get_token_q_step_count() > -1:

                        # token closer to home yard moves
                        if current_player.get_token_p_step_count() > current_player.get_token_q_step_count():
                            self.move_token(current_player, "q", current_steps)
                        else:
                            self.move_token(current_player, "p", current_steps)

                    # check if token q is out of home yard
                    elif current_player.get_token_q_step_count() > -1:
                        self.move_token(current_player, "q", current_steps)

                    # check if token p is out of home yard
                    elif current_player.get_token_p_step_count() > -1:
                        self.move_token(current_player, "p", current_steps)

    def get_all_player_spaces(self):
        """returns an updated list of player's position"""
        all_player_spaces = []
        for player in self._player_list:
            all_player_spaces += player.get_current_pos()
        return all_player_spaces

    def initialize_players(self):
        """return a list of players given user input"""
        potential_players = ['A', 'B', 'C', 'D']

        while True:
            input_value = input('This is a 2-4 player game. How many players are playing? ')
            try:
                int(input_value) == input_value

            except ValueError:
                print('The number must be an integer')
                continue

            if int(input_value) < 2 or int(input_value) > 4:
                print('The number is too small or too large.')
                continue
            else:
                player_list = potential_players[:int(input_value)]
                for player in player_list:
                    self.update_player_list(Player(player))
                print('Ludo game starting with ' + input_value + ' players')
                return player_list

    def play_one_round(self):
        """returns one round of dice roll for all players representing one round in the game"""
        turns_list = []
        for player in self._player_list:
            player_roll = [player.get_player_position(), random.randint(1, 6)]
            turns_list.append(player_roll)
        print(turns_list)
        return turns_list

    def get_all_opponent_spaces(self, current_player):
        """returns list of all opponent spaces given current player"""
        all_opponent_spaces = []
        for opponent in self.get_player_list():
            if opponent.get_player_position() != current_player.get_player_position():
                for index in range(0, 2):
                    opponent_token = opponent.get_current_pos()[index]
                    if opponent_token != "H" and opponent_token != "R" and opponent_token != "E":
                        all_opponent_spaces.append(opponent.get_current_pos()[index])
        return all_opponent_spaces


game = LudoGame()
game.play_game()

