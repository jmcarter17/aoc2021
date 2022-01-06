from collections import Counter
from dataclasses import dataclass
from itertools import product

from utils import timer


@timer
def get_data():
    # return tuple([x - 1 for x in (9, 4)])  # Real input
    return tuple([x - 1 for x in (4, 8)])  # Test input


@dataclass(frozen=True, eq=True)
class GameState:
    positions: tuple[int, int]
    scores: tuple[int, int] = (0, 0)
    player: bool = False

    def update(self, rolls: int):
        new_pos = (self.positions[0] + rolls) % 10
        return GameState(
            (self.positions[1], new_pos),
            (self.scores[1], self.scores[0] + new_pos + 1),
            not self.player,
        )

    def end_game(self, target):
        return self.scores[1] >= target

    def winner(self):
        return self.player


@timer
def part1(data):
    game = GameState(data)
    numrolls = 0
    while not game.end_game(1000):
        dicerolls = sum((x % 100) + 1 for x in range(numrolls, numrolls + 3))
        game = game.update(dicerolls)
        numrolls += 3

    loser_score = game.scores[0]
    return loser_score * numrolls


@timer
def part2(data):
    game = GameState(data)
    game_states = Counter()
    finished_games = Counter()
    game_states[game] += 1
    possible_rolls = Counter(sum(x) for x in product((1, 2, 3), repeat=3))

    while game_states:
        next_states = Counter()
        for game, rolls in product(game_states, possible_rolls):
            updated_game = game.update(rolls)
            quantity = game_states[game] * possible_rolls[rolls]
            if updated_game.end_game(21):
                finished_games[updated_game] += quantity
            else:
                next_states[updated_game] += quantity

        game_states = next_states

    num_winners1 = sum(count for game, count in finished_games.items() if game.winner())
    num_winners2 = sum(count for game, count in finished_games.items() if not game.winner())

    print(len(finished_games))
    print(sum(count for game, count in finished_games.items()))
    print(num_winners1, num_winners2)

    return max(num_winners1, num_winners2)


@timer
def main():
    data = get_data()
    print(part1(data))
    print(part2(data))


if __name__ == "__main__":
    main()
