from src.simulation_utils import MancalaBoard

board = MancalaBoard()
non_ending_moves = []
beads_moved = {}
following_moves = {}

start = 6
for start in [2]:
    scenario = board.complete_move(start, next_starting_positions=[1, 2, 3, 4, 5, 6])#, 1, 2, 3, 4, 6])
    print(scenario)
    print(board.beads)
    print(f"finished at home {board.finished_at_home_count} times")
    if scenario == "Majority of beads now in player home":
        beads_moved[start] = board.beads_moved
        following_moves[start] = board.started_at_positions

print(beads_moved)
print(following_moves)

