# single-threaded library approach
# multi-threaded approach
# authors:  Kent Regalado
#           Eduardo Te
#           Seth Gabon
# margins of error:
#   word count:         282,547 - 283,180     = 11,866
#   sentence count:     19,769 - 19,435       = 334
#   character count:    1,621,764 - 1,431,403 = 190,361
#   total time elapsed: 0.1s

def countWords(string):
    # counts and returns aggregate number of words
    wc = len(string.split()) 

    return wc

def countSentences(string):
    # counts and returns aggregate number of sentences
    sc = string.count('.')

    return sc

def countCharacters(string):
    # counts and returns aggregate number of characters
    cc = len(string) - string.count(' ')

    return cc

# Driver code
fileObject = open("61906-8.txt", "r")
data = fileObject.read()
OUT = 0
IN = 1

print('> Single-threaded library approach')
print('\nword count = ' + str(countWords(data)))
print('sentence count = ' + str(countSentences(data)))
print('character count = ' + str(countCharacters(data)) + '\n')