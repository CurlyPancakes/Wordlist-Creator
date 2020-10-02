#-------IMPORTING-------
import itertools
from sys import stdout
import pyfiglet

#-------VARIABLES-------
infos = []
wordlist = []
counter = 0
passwordstogenerate = 0

info_file = "infos.txt"
wordlist_file = "wordlist.txt"

min_length = 1
max_length = 5

title = pyfiglet.figlet_format("WORDLIST CREATOR V. 1")

#-------INIT FUNCTION-------
def init():
    print(title)
    try:
        min_length = int(input("MIN LENGTH (Standard 1):"))
    except:
        print("Used standard length 1")
    try:
        max_length = int(input("MAX LENGTH (Standard 5):"))
    except:
        print("Used standard length 5")

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
    print(str(passwordstogenerate)+" possible combinations were found.")
    if(passwordstogenerate == 0):
        close(399)
    input("Press ANY key to start generating")

    with open(wordlist_file, "w") as output:
        for i in range(min_length,max_length):
            for password in map(''.join, itertools.product(infos, repeat=i)):
                output.write(password+"\n")
                counter =+ 1
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
    print("[✔] "+str(counter)+" passwords have been successfully generated")
    close(0)

# -------MAIN-------
if __name__ == '__main__':
    init()
    readFiles()
    checkFiles()
    generate()

