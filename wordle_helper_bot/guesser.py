from state import GameState

def parse_file(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
        return tuple(lines)


class Guess:

    words = parse_file('wordle_helper_bot/src/list.txt')

    def make_guess(self, game_state):
        l = lambda w: all([w[i] in game_state.possible_chars[i] for i in range(len(w))]) and (w not in game_state.used_words) and (game_state.definetly_in.issubset(set(w)))
        first_filter = filter(l, self.words)
        return tuple(first_filter)


if __name__ == '__main__':
    gs = GameState()
    guess = Guess()
    gs.next_step('draft', 'BBGBB')
    gs.next_step('coaly', 'GBGYB')
    gs.next_step('claim', 'GGGBB')
    gs.next_step('clash', 'GGGGB')
    print(guess.make_guess(gs))
