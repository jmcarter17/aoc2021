from collections import Counter
from dataclasses import dataclass
from itertools import product

from utils import timer


@timer
def get_data():
    return tuple([x - 1 for x in (9, 4)])  # Real input
    # return tuple([x - 1 for x in (4, 8)])  # Test input


@dataclass(frozen=True, eq=True)
class GameState:
    positions: tuple[int, int]
    scores: tuple[int, int] = (0, 0)
    numrolls: int = 0
    player: int = 0

    def update(self, rolls: int):
        updated_position = (self.positions[self.player] + rolls) % 10
        updated_score = self.scores[self.player] + updated_position + 1
        same_position = self.positions[1 - self.player]
        same_score = self.scores[1 - self.player]
        if self.player == 0:
            positions = updated_position, same_position
            scores = updated_score, same_score
        else:
            positions = same_position, updated_position
            scores = same_score, updated_score

        return GameState(positions, scores, self.numrolls + 3, 1 - self.player)

    def end_game(self, target):
        return any(x >= target for x in self.scores)

    def winner(self):
        return 1 - self.player


@timer
def part1(data):
    game = GameState(data)
    while not game.end_game(1000):
        rollnum = game.numrolls
        dicerolls = sum((x % 100) + 1 for x in range(rollnum, rollnum + 3))
        game = game.update(dicerolls)

    loser_score = game.scores[game.player]
    return loser_score * game.numrolls


@timer
def part2(data):
    game = GameState(data)
    game_states = Counter()
    finished_games = Counter()
    game_states[game] += 1
    possible_rolls = Counter(sum(x) for x in product((1, 2, 3), repeat=3))

    while game_states:
        next_states = Counter()
        for state, rolls in product(game_states, possible_rolls):
            new_state = state.update(rolls)
            quantity = game_states[state] * possible_rolls[rolls]
            if new_state.end_game(21):
                finished_games[new_state] += quantity
            else:
                next_states[new_state] += quantity

        game_states = next_states

    num_winners1 = sum(
        count for game, count in finished_games.items() if game.winner() == 0
    )
    num_winners2 = sum(
        count for game, count in finished_games.items() if game.winner() == 1
    )

    return max(num_winners1, num_winners2)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
