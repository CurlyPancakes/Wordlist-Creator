#-------IMPORTING-------
import itertools
from sys import stdout
import pyfiglet
import argparse

#-------VARIABLES-------
infos = []
wordlist = []
counter = 0
passwordstogenerate = 0

info_file = "infos.txt"
wordlist_file = "wordlist.txt"

min_length = 0
max_length = 0

title = pyfiglet.figlet_format("WORDLIST CREATOR V. 1 . 0")

#-------ARG PARSER-------
def argparser():
    global min_length
    global max_length

    parser = argparse.ArgumentParser(description='Wordlist-Creator is used to create long word combinations lists.')

    parser.add_argument('--min', type=int, help='MIN_LENGTH for the Wordlist-Creator.')
    parser.add_argument('--max', type=int, help='MAX_LENGTH for the Wordlist-Creator.')

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
            min_length = int(input("MIN LENGTH (Standard 1):"))
        except:
            print("Used standard length 1")
            min_length = 1
    if(max_length == 0):
        try:
            max_length = int(input("MAX LENGTH (Standard 5):"))
        except:
            print("Used standard length 5")
            max_length = 5

#-------EXIT-------
def close(error_code):
    if(error_code == 0):
        exit(error_code)
    else:
        print("ERROR CODE->"+str(error_code))
        exit(error_code)

#-------READ FILES-------
def readFiles():
    global passwordstogenerate
    try:
        with open(info_file, "r") as file:
            for line in file.readlines():
                infos.append(line.strip())

            for i in range(min_length, max_length):
                passwordstogenerate += len(infos) ** i
    except:
        open(info_file,"w")
        close(401)

    try:
        with open(wordlist_file, "r") as file:
            for line in file.readlines():
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
    print(str(passwordstogenerate)+" possible word combinations were found.")
    if(passwordstogenerate == 0):
        close(400)
    input("Press ANY key to start generating")

    with open(wordlist_file, "w") as output:
        for i in range(min_length,max_length):
            for password in map(''.join, itertools.product(infos, repeat=i)):
                output.write(password+"\n")
                counter += 1
                percent = counter/passwordstogenerate*100
                arrow = '-' * int(percent / 100 * 20 - 1) + '>'
                spaces = ' ' * (20 - len(arrow))

                stdout.write('Progress: [%s%s] %d %%\r' % (arrow, spaces, percent))
                stdout.flush()
        output.flush()
    finish()

# -------FINISH-------
def finish():
    print("Progress: [------------------->] 100%")
    print("[✔] "+str(counter)+" word combinations have been successfully generated.")
    input("Press ANY key to exit")
    close(0)

# -------MAIN-------
if __name__ == '__main__':
    argparser()
    init()
    readFiles()
    checkFiles()
    generate()

