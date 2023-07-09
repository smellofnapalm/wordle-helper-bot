import string
from enum import Enum, auto

# Класс, который хранит информацию о текущем состоянии игры 
# (на каком слове, сколько и какие буквы открыты, какие слова уже использованы)
class GameState:

    class GameStates(Enum):
        IN_PROGRESS = auto()
        WIN = auto()
        LOST = auto()

    alphabet = list(string.ascii_lowercase[:26])

    def __init__(self, length=5, max_steps=6):
        self.state = self.GameStates.IN_PROGRESS
        self.WIN_MASK = ['G' for _ in range(length)]
        self.step = 0
        self.word_length = length
        self.max_steps = max_steps
        self.used_words = []
        self.definetly_in = set()
        self.possible_chars = [set(self.alphabet.copy()) for _ in range(length)]
    def next_step(self, word, mask):
        self.step += 1
        if self.step > self.max_steps:
            self.state = self.GameStates.LOST
            return
        if mask == self.WIN_MASK:
            self.state = self.GameStates.WIN
            return
        self.used_words.append(word)
        for i in range(self.word_length):
            match mask[i]:
                case 'B':
                    for j in range(self.word_length):
                        if word[i] in self.possible_chars[j] and (word[j] != word[i] or mask[j] != 'G'):
                            self.possible_chars[j].remove(word[i])
                case 'Y':
                    if word[i] in self.possible_chars[i]:
                        self.possible_chars[i].remove(word[i])
                        self.definetly_in.add(word[i])
                case 'G':
                    self.possible_chars[i] = set([word[i]])
                    self.definetly_in.add(word[i])


if __name__ == '__main__':
    gs = GameState()
    gs.next_step('slate', 'BBBYY')
    gs.next_step('cured', 'BBYGB')
    gs.next_step('toner', 'YBYGG')
    gs.next_step('niter', 'YBGGG')
    print(gs.possible_chars)
    print(gs.definetly_in)
    print(gs.used_words)
        
