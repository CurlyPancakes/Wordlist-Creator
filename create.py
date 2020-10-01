import itertools
from sys import stdout
import pyfiglet

infos = []
wordlist = []
counter = 0
passwordstogenerate = 0

title = pyfiglet.figlet_format("WORDLIST CREATOR V. 1")
print(title)

try:
    min_length = int(input("MIN LENGTH (Standard 1):"))
except:
    print("Used standard length 1")
    min_length = 1
try:
    max_length = int(input("MAX LENGTH (Standard 5):"))
except:
    print("Used standard length 5")
    max_length = 5
	
with open("infos.txt", "r") as file:

    for line in file.readlines():

        infos.append(line.strip())

    for i in range(min_length, max_length):

        passwordstogenerate += len(infos)**i

with open("wordlist.txt", "r") as file:

    for line in file.readlines():

        wordlist.append(line.strip())

if(len(infos) <= 0):
    print("Empty infos.txt")
    input("Press ANY key to exit")
    exit(403)

if(len(wordlist)>=0):
    print("The wordlist.txt is not empty!")
    question = input("Do you want to continue [Y/N]")

    if(question.upper() == "N"):
        input("Press ANY key to exit")
        exit(402)

print(str(passwordstogenerate)+" possible combinations were found.")
input("Press ANY key to start generating")

with open("wordlist.txt", "w") as output:

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

    print("Progress: [------------------->] 100%")
    print(str(counter)+" passwords have been successfully generated")
    input("Press ANY key to exit")

