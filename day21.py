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
        next_player = 1 - self.player
        new_positions: [int] = [0, 0]
        new_scores: [int] = [0, 0]
        new_positions[self.player] = (self.positions[self.player] + rolls) % 10
        new_positions[next_player] = self.positions[next_player]
        new_scores[self.player] = self.scores[self.player] + new_positions[self.player] + 1
        new_scores[next_player] = self.scores[next_player]

        return GameState(tuple(new_positions), tuple(new_scores), self.numrolls + 3, next_player)

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
        for game, rolls in product(game_states, possible_rolls):
            updated_game = game.update(rolls)
            quantity = game_states[game] * possible_rolls[rolls]
            if updated_game.end_game(21):
                finished_games[updated_game] += quantity
            else:
                next_states[updated_game] += quantity

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
