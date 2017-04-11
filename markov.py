"""Generate markov text from text files."""


from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    textfile = open(file_path)

    return textfile.read() #reads file as one long string




def make_chains(text_string):
    """Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
    """

    words = open_and_read_file('green-eggs.txt').split() #splits string

    chains = {}

    for index in range(len(words)-2):
        if (words[index], words[index+1]) not in chains:
            chains[(words[index], words[index+1])] = [words[index+2]]

        else:
            chains[(words[index], words[index+1])].append(words[index+2])

    return chains


def make_text(chains):
    """Returns text from chains."""

    result = 'Would you '

    key1 = "Would"
    key2 = "you"

    while True:
        try:
            value = choice(chains[(key1, key2)])
            result = result + value + ' '
            key1 = key2
            key2 = value
        except KeyError:
            break

    return result

print make_text(make_chains('gettysburg.txt'))
