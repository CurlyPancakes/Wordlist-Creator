import itertools
import os
wordlists = []
inProgress = True
counter = 0
threads = 0
threading_counter = 0
closedthreads = 0

def generate(length, infos, wordlist_file):
    global counter
    global threading_counter
    global closedthreads

    threading_counter += 1
    filetoopen = wordlist_file+str(threading_counter)
    wordlists.append(filetoopen)
    with open(filetoopen, "w+") as output:
        for password in map(''.join, itertools.product(infos, repeat=length)):
            output.write(password + "\n")
            counter += 1
    closedthreads += 1
    done()

def done():
    global inProgress
    if(closedthreads==threads):
        mergeall()
        deleteall()
        inProgress = False
def mergeall():
    with open("wordlist.txt","w+") as wordlist:
        for i in range(closedthreads):
            with open(wordlists[i]) as file:
                while line:=file.readline():
                    wordlist.write(line.strip()+"\n")
        wordlist.flush()
def deleteall():
    for i in range(closedthreads):
       os.remove(wordlists[i])

