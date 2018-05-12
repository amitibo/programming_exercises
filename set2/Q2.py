"""
Segmenting English text
-----------------------
At Google we deal with a lot of text. Suppose we have a source of text, let's
say news stories, for example, like this:

  OBAMASAYSHEPLANSTOVETOTHEBILL

But there's a problem, as you can see: there are no spaces between words. I want
to make a system to put them back in. How shall we do it?"
"""

import copy
from tqdm import tqdm

DICT_PATH = "english_filtered.txt"


class EnglishDict(object):

    def __init__(self, dict_path=DICT_PATH):

        self._dict = {}
        with open(dict_path, "r", encoding="Latin-1") as f:
            for word in f:
                self._dict[word.strip()] = 1

        self._dict["obama"] = 1

        #
        # Remove all single letter words.
        #
        for c in "bcdefghjklmnpqrstuvwxyz":
            del self._dict[c]

    def isWord(self, word):

        return word in self._dict


def find_words(sentence, en_dict, words=[]):

    if len(sentence) == 0:
        print(words)
        return

    for j in range(len(sentence)):
        i = j + 1
        new_word = sentence[:i]
        if en_dict.isWord(new_word):
            if new_word == "obama":
                print(new_word)
            new_words = copy.deepcopy(words)
            new_words.append(new_word)
            find_words(sentence[i:], en_dict, new_words)


def test_Q2():

    tests = [
        "OBAMASAYSHEPLANSTOVETOTHEBILL"
    ]
    tests = [test.lower() for test in tests]

    en_dict = EnglishDict()

    for test in tqdm(tests):
        find_words(test, en_dict)


if __name__ == "__main__":
    test_Q2()