"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file = open(file_path)
    text = file.read()
    return text


def make_chains(text_string):
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

    # your code goes here
    words = text_string.split()

    # for i in range(len(words) - 1):
    #     print(words[i], words[i + 1])
    
    for i in range(len(words) - 2):
        if (words[i], words[i + 1]) in chains.keys():
            if words[i + 2] not in chains[(words[i], words[i + 1])]:
                chains[(words[i], words[i + 1])].append(words[i + 2])
        else:
            chains[(words[i], words[i + 1])] = [words[i + 2]]

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    start, value = choice(list(chains.items()))
    words.append(start[0])
    words.append(start[1])
    cont = True
    while cont:
        if (words[-2], words[-1]) in chains.keys():
            words.append(choice(chains[(words[-2], words[-1])]))
        else:
            cont = False

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
input_path = 'gettysburg.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)