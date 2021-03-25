#this program is for homocidal purposes only

#module import
import random
import pyperclip

stick = [
"stick", "bad", "ophelia", "gun", "bad", "fds", "stick", "fds", "stick", "ophelia", "stick", "ophelia", "bad", "bad", "naughty", "fds", "stick", "whip", "bad", "meth", "stick", "evil"
] #i probably couldve done something with a weighted choice but holy shit this is not the kind of program i put effort into
#so instead i just broke down on a list
porb = random.randint(10,50)
qanon = "stick stick "

for porb in range(porb):
    qanon = qanon + random.choice(stick) + " "
print(qanon)
yn = input("do you want to copy the contents to ur mfing clipboard (y/n)")

if yn == "y" or yn == "Y" or yn == "yes":
    pyperclip.copy(qanon)
else:
    print("k thx bye")
