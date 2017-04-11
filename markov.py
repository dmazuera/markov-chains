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

    words = open_and_read_file(text_string).split() #splits string

    chains = {}

    for index in range(len(words)-2):
        if (words[index], words[index+1]) not in chains:
            chains[(words[index], words[index+1])] = [words[index+2]]

        else:
            chains[(words[index], words[index+1])].append(words[index+2])

    return (chains, words) #passing tuple to next function


def make_text(input_data): #only takes in one object
    """Returns text from chains."""

    chains, words = input_data[0], input_data[1] #unpacks input_object

    #starts printed empty string with first 2 words in .txt
    result = '{} {} '.format(words[0], words[1])


    key1 = words[0]
    key2 = words[1]

    while True:
        try:
            value = choice(chains[(key1, key2)])
            result = result + value + ' '
            key1 = key2
            key2 = value
        except KeyError:
            break

    return result

print make_text(make_chains('green-eggs.txt'))#input .txt file to run ONLY PLACE!
