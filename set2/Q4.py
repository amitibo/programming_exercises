"""Find the most common character of a string (multi-threaded/distributed)

PART 1a: SINGLE-THREADED, ASCII

I start by telling the candidate that we'll go over many iterations of the
problem, starting simple and getting more complicated. I first ask "What
algorithm would you use to find the most common character of a string?"

Better candidates will ask a few questions: what is the expected length? the
encoding of the characters? the expected distribution? I tell them it's for
an ASCII string, typically between 30 and 2000 characters, and that we're
always looking for the fastest solution.

I make sure that the candidates specifies how the most common characters
will actually be determined.

PART 1b: SINGLE-THREADED, SHORT STRING

If they have used an array, I sometimes ask if they would use the same algorithm
if all the input strings were guaranteed to be 6 characters or less.

PART 1c: SINGLE-THREADED, UNICODE

If they have used an array, I ask them what they would do if the string was in
Unicode. I tell them to assume that a Unicode character is 16 bits.

PART 2: MULTI-THREADED

For this iteration, I tell them that the we have a modern quad-core PC with 4
gigs of RAM, and that the Unicode string is now 500MB. I ask them how they would
modify their algorithm for this new situation.

PART 3: DISTRIBUTED, WIRED

For this variant, a 500GB Unicode string is one file on the local disk of a
master computer. Connected via gigabit Ethernet are 10 worker computers. The
eleven computers are typical single processor PCs (think SATA drives & 4GB RAM).

I ask if the master can make effective use of the 10 workers to figure out the
most common character, and if so, how they would architect the solution. The
goal, as always, is to find the answer as fast as possible.

PART 4: DISTRIBUTED, WIRELESS

For the last iteration, I tell them that the string is now 10TB (getting closer
to Google-size). We have almost the same setup as part 3 (one master and ten
workers). The string is too big to fit on one disk, so a tenth of the string is
on the local disk of each worker. Each worker wakes up, processes its share of
the string, and calculates its frequency table. The master now needs to figure
out the overall most common character. The difference with the previous scenario
is that we are now on wireless (e.g. satellite) and that we pay for each packet
sent over the network. The question is "How can the master figure out the
overall most common character while minimizing network usage?"
"""

import random
import numpy as np

N = 100000
CHARS = "abcdefghijklmnopqrstuvwxyz"


def count_array(array):

    hist = {k:0 for k in CHARS}

    for c in array:
        hist[c] += 1

    return hist


def test_Q4():

    array = "".join([random.choice(CHARS) for i in range(N)])

    hist = count_array(array)
    chars, counts = list(zip(*[(k, v) for k, v in hist.items()]))

    print("Most common letter is: {}".format(chars[np.argmax(counts)]))


if __name__ == "__main__":
    test_Q4()