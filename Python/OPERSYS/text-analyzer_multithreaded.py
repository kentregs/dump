# multi-threaded manual approach
# authors:  Kent Regalado
#           Eduardo Te
#           Seth Gabon
# margins of error:     expected:   actual:     
#   word count:         367,061   - 367,158    = 97
#   sentence count:     23,138    - 23,139     = 1
#   character count:    1,495,070 - 1,495,030  = 40
# total time elapsed: 5.7s - 8.0s
# text file link: https://www.gutenberg.org/files/766/766-0.txt

import threading

shared_lock = threading.Lock()

class wordCounter(threading.Thread):
    def __init__(self, text):
        threading.Thread.__init__(self)
        self.counter = 0
        self.text = text

    def run(self):
        # for c in self.text:
        #     self.counter += 1
        for i in range(len(self.text)):
            if (self.text[i] == ' ' or self.text[i] == '\n' or
                self.text[i] == '\t' or self.text[i] =='\0'):
                    self.counter += 1

class sentCounter(threading.Thread):
    def __init__(self, string, name):
        threading.Thread.__init__(self)
        self.string = string
        self.name = name
    def run(self):
        global shared_lock
        # blocks until a call to release() in 
        # another thread changes it to unlocked
        # then the acquire() call resets it 
        # to locked and returns
        shared_lock.acquire()

        print('Starting ' + self.name)
        countSentence(self.string, self.name)
        print('Exiting ' + self.name + '\n')

        # changes the state to unlocked and returns immediately
        # NOTE: If an attempt is made to release an unlocked lock, 
        # a RuntimeError will be raised.
        shared_lock.release()

class charCounter(threading.Thread):
    def __init__(self, string, name):
        threading.Thread.__init__(self)
        self.string = string
        self.name = name
    def run(self):
        global shared_lock
        # blocks until a call to release() in 
        # another thread changes it to unlocked
        # then the acquire() call resets it 
        # to locked and returns
        shared_lock.acquire()

        print('Starting ' + self.name)
        countCharacters(self.string, self.name)
        print('Exiting ' + self.name + '\n')

        # changes the state to unlocked and returns immediately
        # NOTE: If an attempt is made to release an unlocked lock, 
        # a RuntimeError will be raised.
        shared_lock.release()

def countSentence(string, name):
    # counts and prints aggregate number of sentences
    sc = 0

    for i in range(len(string)):
        if (string[i] == '.' or string[i] == '!' or
            string[i] == '?'):
            sc += 1
    print(str(name) + ': sentence count = ' + str(sc))

def countCharacters(string, name):
    # counts and prints aggregate number of sentences
    cc = 0

    for i in range(len(string)):
        if string[i].isalnum():
            cc += 1

    print(str(name) + ': character count = ' + str(cc))

if __name__ == "__main__":
    number_of_threads = 100
    threads = []
    counter = 0
    OUT = 0
    IN = 1

    # Read text file before using threads to avoid IO errors
    file = open("test.txt", "r")
    text = file.read()

    print('> Multi-threaded manual approach\n')
    
    # create threads
    t2 = sentCounter(text, 'sentCounter')
    t3 = charCounter(text, 'charCounter')

    t2.start()
    t3.start()

    t2.join()
    t3.join()

    # Split your text file into parts, equal to 
    # the number of threads
    parts = [text[i:i + number_of_threads] for i in range(0, len(text), number_of_threads)]
    
    # Create and start a thread for each part
    for part in parts:
        thread = wordCounter(part)
        thread.start()
        threads.append(thread)
    
    # Join your threads and aggregate their values
    for thread in threads:
        thread.join()
        counter += thread.counter
    
    print('word count = ' + str(counter) + '\n')