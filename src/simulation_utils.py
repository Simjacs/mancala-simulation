class MancalaBoard:
    def __init__(self):
        self.n_homes = 2
        self.n_bowls = 12
        self.n_beads = 4
        self.home_positions = [0, 7]
        self.beads_in_hand = 0
        self.player_position = None
        self.player_home_position = 0
        self.beads = {
            i: (self.n_beads if i not in self.home_positions else 0)
            for i in range(self.n_homes + self.n_bowls)
        }
        self.hand_finished_at_home = False
        self.hand_finished_in_empty_bowl = False
        self.break_states = {0: "Out of starting positions",
                             1: "Majority of beads now in player home",
                             2: "No more moves available",
                             3: "Hand ended in empty bowl"}
        self.finished_at_home_count = 0
        self.started_at_positions = []
        self.beads_moved = 0

    def start_move_from(self, position: int):
        if position in self.home_positions:
            print("Cannot start move from home position")
            return 0
        self.beads_in_hand = self.beads[position]
        self.beads[position] = 0
        self.player_position = position

    def move_one_position(self):
        # move player one step, go back round after all bowls passed
        # do not pass over opponents home
        self.player_position -= 1
        if self.player_position < 0:
            self.player_position = 13
        if self.player_position == self.home_positions[self.n_homes - 1]:
            self.player_position -= 1
        #print(self.player_position)

    def make_one_step(self):
        # move player one step, increment number of beads, decrement beads in hand
        self.move_one_position()
        self.beads[self.player_position] += 1
        self.beads_in_hand -= 1
        self.beads_moved += 1

    def distribute_beads_in_hand(self):
        # make one step until beads_in_hand = 0
        while self.beads_in_hand > 0:
            self.make_one_step()

    def pick_up_next_hand(self):
        current_position = self.player_position
        current_beads_in_bowl = self.beads[self.player_position]
        if (current_position != self.home_positions[0]) & (current_beads_in_bowl != 0):
            # pick up beads in bowl at current position
            self.beads_in_hand = self.beads[self.player_position]
            self.hand_finished_in_empty_bowl = False
            self.hand_finished_at_home = False
            return True
        elif current_position == self.home_positions[0]:
            self.finished_at_home_count += 1
            self.hand_finished_at_home = True
            return False
        elif current_beads_in_bowl == 0:
            self.hand_finished_in_empty_bowl = True
            self.hand_finished_at_home = False
            return False

    def distribute_one_bowl(self, starting_position):
        self.start_move_from(starting_position)
        self.distribute_beads_in_hand()
        can_continue_move = self.pick_up_next_hand()
        print(self.beads)
        return can_continue_move

    def complete_hand(self, starting_position):
        # start move:
        can_continue_move = self.distribute_one_bowl(starting_position)
        while can_continue_move:
            can_continue_move = self.distribute_one_bowl(self.player_position)

    def complete_move(self, starting_position, next_starting_positions=None):
        if next_starting_positions is None:
            next_starting_positions = [1, 2, 3, 4, 5, 6]
        self.complete_hand(starting_position)
        i = 0
        if self.hand_finished_in_empty_bowl:
            return self.break_states[3]
        while not self.hand_finished_in_empty_bowl:
            try:
                self.started_at_positions.append(next_starting_positions[i])
                self.complete_hand(next_starting_positions[i])
            except IndexError:
                return self.break_states[0]
            if i > len(next_starting_positions):
                print("No more starting positions given")
                return self.break_states[0]
            if self.beads[0] > 18:
                print("Majority of beads in player home, player has won")
                return self.break_states[1]
            if sum([self.beads[i] for i in [1, 2, 3, 4, 5, 6]]) == 0:
                print("No more available moves, turn passes to opponent")
                return self.break_states[2]
            i += 1

        if self.hand_finished_in_empty_bowl:
            return self.break_states[3]














