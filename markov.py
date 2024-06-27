"""Generate Markov text from text files."""

from random import choice
from sys import argv

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    full_text = ''

    text = open(file_path)
    for line in text:
        line = line.rstrip()
        full_text += line + ' '

    return full_text


def make_chains(text_string, n):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.strip().split(' ')

    for i in range(len(words) - n):
        length = 0
        curr_list = []

        while length < n:
            curr_list.append(words[i + length])
            length += 1

        pair = tuple(curr_list)
        chains[pair] = []

    for i in range(len(words) - n):
        length = 0
        temp_list = []

        while length < n:
            temp_list.append(words[i + length])
            length += 1

        temp = tuple(temp_list)
        if temp in chains:
            if words[i+2] != '':
                chains[temp].append(words[i+2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    items = chains.items()

    for item in items:
        if item[1] != []:
            new_word = choice(item[1])
            words.append(new_word)

    return ' '.join(words)


input_path = argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 4)

# Produce random text
random_text = make_text(chains)

print(random_text)

