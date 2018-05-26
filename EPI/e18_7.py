"""Trnasform one string to another.
"""

import collections
import copy
import random
import string
from tqdm import trange

DICT_PATH = "../set2/english_filtered.txt"


class EnglishDict(object):

    def __init__(self, dict_path=DICT_PATH):

        self._dict = {}
        with open(dict_path, "r", encoding="Latin-1") as f:
            for word in f:
                self._dict[word.strip()] = 1

        #
        # Remove (most) single letter words.
        #
        for c in "bcdefghjklmnpqrstuvwxyz":
            del self._dict[c]

    def isWord(self, word):

        return word in self._dict

    def remove(self, word):

        if word in self._dict:
            del self._dict[word]


def transform_string(D, s, t):
    """Check if there is a "Producer sequence" connecting s to t."""

    StringWithDistance = collections.namedtuple(
        "StringWithDistance",
        ["candidate_string", "distance", "path"]
    )
    q = collections.deque([StringWithDistance(s, 0, [s])])
    D.remove(s)

    while q:
        f = q.popleft()
        if f.candidate_string == t:
            return f.distance, f.path

        for i in range(len(f.candidate_string)):
            for c in string.ascii_lowercase:
                cand = f.candidate_string[:i] + c + f.candidate_string[i+1:]
                if D.isWord(cand):
                    q.append(StringWithDistance(cand, f.distance+1, f.path + [cand]))
                    D.remove(cand)

    return -1, []


def main():
    D = EnglishDict()

    print(transform_string(copy.deepcopy(D), "mother", "singer"))


if __name__ == "__main__":
    main()