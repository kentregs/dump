# multi-threaded library approach
# author:  Kent Regalado
# margins of error:
#   word count:         282,547 - 283,180     = 633
#   sentence count:     19,769 - 19,435       = 334
#   character count:    1,621,764 - 1,431,403 = 190,361
# total time elapsed: 0.1s

import threading

shared_lock = threading.Lock()

class wordCounter(threading.Thread):
    def __init__(self, string, name):
        threading.Thread.__init__(self)
        self.string = string
        self.name = name
    def run(self):
        global shared_lock
        shared_lock.acquire()
        print('Starting ' + self.name)
        countWords(self.string, self.name)
        print('Exiting ' + self.name + '\n')
        shared_lock.release()

class sentCounter(threading.Thread):
    def __init__(self, string, name):
        threading.Thread.__init__(self)
        self.string = string
        self.name = name
    def run(self):
        global shared_lock
        shared_lock.acquire()
        print('Starting ' + self.name)
        countSentence(self.string, self.name)
        print('Exiting ' + self.name + '\n')
        shared_lock.release()

class charCounter(threading.Thread):
    def __init__(self, string, name):
        threading.Thread.__init__(self)
        self.string = string
        self.name = name
    def run(self):
        global shared_lock
        shared_lock.acquire()
        print('Starting ' + self.name)
        countCharacters(self.string, self.name)
        print('Exiting ' + self.name + '\n')
        shared_lock.release()

def countWords(string, name):
    # blocks until a call to release() in 
    # another thread changes it to unlocked
    # then the acquire() call resets it 
    # to locked and returns
   
    # counts and prints aggregate number of words
    wc = len(string.split()) 
    print(str(name) + ': word count = ' + str(wc))

    # changes the state to unlocked and returns immediately
    # NOTE: If an attempt is made to release an unlocked lock, 
    # a RuntimeError will be raised.

def countSentence(string, name):
    # blocks until a call to release() in 
    # another thread changes it to unlocked
    # then the acquire() call resets it 
    # to locked and returns

    # counts and prints aggregate number of sentences
    sc = string.count('.')
    print(str(name) + ': sentence count = ' + str(sc))

    # changes the state to unlocked and returns immediately
    # NOTE: If an attempt is made to release an unlocked lock, 
    # a RuntimeError will be raised.

def countCharacters(string, name):
    # blocks until a call to release() in 
    # another thread changes it to unlocked
    # then the acquire() call resets it 
    # to locked and returns

    # counts and prints aggregate number of sentences
    cc = len(string) - string.count(' ')

    print(str(name) + ': character count = ' + str(cc))

    # changes the state to unlocked and returns immediately
    # NOTE: If an attempt is made to release an unlocked lock, 
    # a RuntimeError will be raised.

# Driver code
fileObject = open("61906-8.txt", "r")
data = fileObject.read()
print('> Multi-threaded library approach\n')

# create threads
t1 = wordCounter(data, 'Thread-1')
t2 = sentCounter(data, 'Thread-2')
t3 = charCounter(data, 'Thread-3')

# start and wait for new threads to finish
t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
