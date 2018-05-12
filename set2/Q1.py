"""
Word search
-----------
Given a 4X4 grid of letters and a dictionary, find all the words from the
dictionary that can be formed in the grid.
The rules for forming a word are: start at any position on the board,
move in any of the up to 8 directions to choose another letter, repeat.
You cannot re-use a letter in a given position in the same word.

Initially, I tell the candidate that the dictionary is an object with an
"isWord" method, and if they want that object to have any other methods,
assume it has them. The secondary question is to implement the dictionary.
"""

import copy
import random
from tqdm import trange

GRID_SIZE = 4
CHARS = "abcdefghijklmnopqrstuvwxyz"
DICT_PATH = "english_filtered.txt"


class EnglishDict(object):

    def __init__(self, dict_path=DICT_PATH):

        self._dict = {}
        with open(dict_path, "r", encoding="Latin-1") as f:
            for word in f:
                self._dict[word.strip()] = 1

        #
        # Remove all single letter words.
        #
        for c in "bcdefghjklmnpqrstuvwxyz":
            del self._dict[c]

    def isWord(self, word):

        return word in self._dict


def get_neighbours(pos, mask):

    valid_neigh = []
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            if i==0 and j==0:
                continue

            next_pos = pos[0] + i, pos[1] + j
            if next_pos[0] < 0 or next_pos[0] >= GRID_SIZE or \
               next_pos[1] < 0 or next_pos[1] >= GRID_SIZE:
                continue

            if mask[next_pos[0]][next_pos[1]] == 0:
                valid_neigh.append((i, j))

    return valid_neigh


def find_words(pos, grid, mask, cur_word, words_list, en_dict):

    mask = copy.deepcopy(mask)
    mask[pos[0]][pos[1]] = 1
    cur_word = cur_word + grid[pos[0]][pos[1]]

    if en_dict.isWord(cur_word):
        words_list.append(cur_word)

    for neigh in get_neighbours(pos, mask):
        #
        # Prepare next stage
        #
        next_pos = pos[0] + neigh[0], pos[1] + neigh[1]

        #
        # Recurse
        #
        find_words(
            pos=next_pos,
            grid=grid,
            mask=mask,
            cur_word=cur_word,
            words_list=words_list,
            en_dict=en_dict
        )


def test_Q1():

    grid = [
        [random.choice(CHARS) for i in range(GRID_SIZE)]
        for j in range(GRID_SIZE)
    ]
    mask = [
        [0 for i in range(GRID_SIZE)]
        for j in range(GRID_SIZE)
    ]

    en_dict = EnglishDict()

    words_list = []
    for i in trange(GRID_SIZE):
        for j in trange(GRID_SIZE, leave=False):
            find_words(
                pos=(i, j),
                grid=grid,
                mask=mask,
                cur_word="",
                words_list=words_list,
                en_dict=en_dict
            )

    print(words_list)


if __name__ == "__main__":
    test_Q1()