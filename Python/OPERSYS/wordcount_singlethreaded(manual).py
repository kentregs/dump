# single-threaded manual approach
# multi-threaded approach
# authors:  Kent Regalado
#           Eduardo Te
#           Seth Gabon
# margins of error:
#   word count:         295,046 - 283,180     = 11,866
#   sentence count:     19,769 - 19,435       = 334
#   character count:    1,885,369 - 1,431,403 = 453,966
#   total time elapsed: 2.3s

def countWords(string):
    state = OUT
    wc = 0

    for i in range(len(string)):
        if (string[i] == ' ' or string[i] == '\n' or
        string[i] == '\t' or string[i] =='.' or
        string[i] == ':' or string[i] == ';' or
        string[i] == ',' or string[i] == '"'):
            state = OUT

        # If the next character is not a word, separator
        # and state are set to OUT. Afterwards, state is
        # reset to IN and the word count is incremented
        elif state == OUT:
            state = IN
            wc += 1
    return wc

def countSentences(string):
    sc = 0

    for i in range(len(string)):
        if string[i] == '.' :
            sc += 1
    return sc

def countCharacters(string):
    # counts and prints aggregate number of characters
    cc = 0

    for i in range(len(string)):
        if not([i] == '.' or [i] == '\n' or
               [i] == '\t'):
            cc += 1

    return cc

# Driver code
fileObject = open("61906-8.txt", "r")
data = fileObject.read()
OUT = 0
IN = 1

print('> Single-threaded manual approach')
print('\nword count = ' + str(countWords(data)))
print('sentence count = ' + str(countSentences(data)))
print('character count = ' + str(countCharacters(data)) + '\n')