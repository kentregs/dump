# single-threaded manual approach
# authors:  Kent Regalado
#           Eduardo Te
#           Seth Gabon
# margins of error:     expected:   actual:     
#   word count:         367,061   - 367,158    = 97
#   sentence count:     23,138    - 23,139     = 1
#   character count:    1,495,070 - 1,495,030  = 40
# total time elapsed: 1.4s - 2.5s
# text file link: https://www.gutenberg.org/files/766/766-0.txt

def countWords(string):
    state = OUT
    wc = 0

    for i in range(len(string)):
        if (string[i] == ' ' or string[i] == '\n' or
            string[i] == '\t' or string[i] =='\0'):
            wc += 1

    return wc

def countSentences(string):
    sc = 0

    for i in range(len(string)):
        if (string[i] == '.' or string[i] == '!' or
            string[i] == '?'):
            sc += 1
    return sc

def countCharacters(string):
    # counts and prints aggregate number of characters
    cc = 0

    for i in range(len(string)):
        if string[i].isalnum():
            cc += 1

    return cc

# Driver code
fileObject = open("test.txt", "r")
data = fileObject.read()
OUT = 0
IN = 1

print('> Single-threaded manual approach')
print('\nword count = ' + str(countWords(data)))
print('sentence count = ' + str(countSentences(data)))
print('character count = ' + str(countCharacters(data)) + '\n')