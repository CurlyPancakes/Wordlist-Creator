#-------IMPORTING-------
import time
from sys import stdout
import pyfiglet
import argparse
from lib import generator
import threading

#-------VARIABLES-------
infos = []
wordlist = []
counter = 0
combinations = 0
threads = []

info_file = "infos.txt"
wordlist_file = "wordlist.txt"

min_length = 0
max_length = 0

title = pyfiglet.figlet_format("WORDLIST CREATOR V. 1 . 1")

#-------ARG PARSER-------
def argparser():
    global min_length
    global max_length

    parser = argparse.ArgumentParser(description='Wordlist-Creator is used to create long word combinations lists.')

    parser.add_argument('--min', type=int, help='MIN_AMOUNT of items in one word combination.')
    parser.add_argument('--max', type=int, help='MAX_AMOUNT of items in one word combination.')

    args = parser.parse_args()

    if(args.max is not None):
        max_length = args.max
    if(args.min is not None):
        min_length = args.min

#-------INIT FUNCTION-------
def init():
    global min_length
    global max_length
    print(title)
    if(min_length == 0):
        try:
            min_length = int(input("MIN AMOUNT (Standard 1):"))
        except:
            print("Used standard amount 1")
            min_length = 1
    if(max_length == 0):
        try:
            max_length = int(input("MAX AMOUNT (Standard 5):"))
        except:
            print("Used standard amount 5")
            max_length = 5

#-------EXIT-------
def close(error_code):
    if(error_code == 0):
        exit(error_code)
    else:
        print("ERROR CODE->"+str(error_code))
        input("Press ANY key to exit")
        exit(error_code)

#-------READ FILES-------
def readFiles():
    global combinations
    try:
        with open(info_file, "r") as file:
            while line:=file.readline():
                infos.append(line.strip())

            for i in range(min_length, max_length+1):
                combinations += len(infos) ** i
    except:
        open(info_file,"w")
        close(401)

    try:
        with open(wordlist_file, "r") as file:
            while line:=file.readline():
                wordlist.append(line.strip())
    except:
        file = open(wordlist_file, "w")
        print("[✔] Created wordlist.txt")

#-------CHECK FILES-------
def checkFiles():
    if(len(infos) == 0):
        print("[❌] Empty infos.txt")
        close(403)

    if(len(wordlist)>0):
        print("[❌] The wordlist.txt is not empty!")
        question = input("Do you want to continue [Y/N]")

        if(question.upper() != "Y"):
            close(402)

#-------GENERATE-------
def generate():
    global counter
    global threads
    print(str(combinations)+" possible word combinations were found.")

    if(combinations == 0):
        close(400)
    input("Press ANY key to start generating")
    generator.threads = max_length + 1 - min_length

    for i in range(min_length, max_length+1):
        t = threading.Thread(target=generator.generate, args=(i, infos, wordlist_file,), daemon=True)
        t.start()


    while (True):
        percent = generator.counter / combinations * 100
        arrow = '-' * int(percent / 100 * 20 - 1) + '>'
        spaces = ' ' * (20 - len(arrow))

        stdout.write('Progress: [%s%s] %d %%\r' % (arrow, spaces, percent))
        stdout.flush()
        if(generator.inProgress == False):
            break
        time.sleep(0.1)
    finish()

# -------FINISH-------
def finish():
    print("Progress: [------------------->] 100%")
    print("[✔] " + str(generator.counter) + " word combinations have been successfully generated.")
    input("Press ANY key to exit")
    close(0)

# -------MAIN-------
if __name__ == '__main__':
    argparser()
    init()
    readFiles()
    checkFiles()
    generate()