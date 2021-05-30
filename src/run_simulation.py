class MancalaBoard:
    def __init__(self):
        self.n_homes = 2
        self.n_bowls = 12
        self.n_beads = 4
        self.beads = {
            i: (self.n_beads if i not in self.home_positions else 0)
            for i in range(self.n_homes + self.n_bowls)
        }
        self.home_positions = [0, 7]
        self.beads_in_hand = 0
        self.player_position = None
        self.player_home_position = 0

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
        print(self.player_position)

    def make_one_step(self):
        # move player one step, increment number of beads, decrement beads in hand
        self.move_one_position()
        self.beads[self.player_position] += 1
        self.beads_in_hand -= 1

    def complete_move(self):
        # make one step until beads_in_hand = 0
        while self.beads_in_hand > 0:
            self.make_one_step()
        print(self.beads[self.home_positions[0]]



