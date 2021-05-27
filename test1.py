# Variables
userReturnQ = str ( " " )
answer = str ( " " )
quit1 = str ( " " )
signIn = str ( " " )
username = str ( " " )
user = str ( " " )
x = 0
score = x
#password =








print ( "Welcome to the IT quiz!\nAre you a returning user?" )
while userReturnQ != "y" and userReturnQ != "n":
    print ( "Enter either y or n..." )
    userReturnQ = input ()

if userReturnQ == "y":
    print ( "Welcome Back" )
    while quit1 == "y":
        print ( "Whats Your username?" )
        answer = input ()

elif userReturnQ == "n":
        print ( "Sign Up\nMust answer y/n" )
        signIn = input ()

if answer == "y":
    print ( "Create a username..." )
    users = open("users.csv", "r+")
    users.write = input ()
    users.close()


elif signIn == "n":
    print ( "Quit?" )
    quit1 = input ()
gggg












#if password = correct
    # Question One
print("What does LAN stand for?")
answer_1 = input("a)Local Area Network\nb)Local Access Network\nc)No Access Network\nd)Laptop Access Network\n:")
if answer_1.lower() == "a" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, LAN stands for Local Area Network")

#//////////


    # Question Two
print("Aside from ethical reasons, what encourages companies to keep personal data secure?")
answer_1 = input("a)Fear of own data being stolen\nb)Other company releasing data\nc)Substancial Fines\nd)Better recomendation to others\n:")
if answer_1.lower() == "c" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Correct answer is c)")


    # Question Three
print("What type of cyberattack is Structured Query Language (SQL) injection?")
answer_1 = input("a)Active\nb)Passive\nc)Insider\nd)Not a real attack\n:")
if answer_1.lower() == "a" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, SQL injection is an active attack")


    # Question Four
print("A flash drive is...")
answer_1 = input("a)input device\nb)output device\nc)secondary storage\nd)main storage\n:")
if answer_1.lower() == "c" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, A flash drive is secondary storage")


    # Question Five
print("A printer is...")
answer_1 = input("a)input device\nb)output device\nc)secondary storage\nd)main storage\n:")
if answer_1.lower() == "b" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, A printer is an output device")


    # Question Six
print("RAM is ...")
answer_1 = input("a)input device\nb)output device\nc)secondary storage\nd)main storage\n:")
if answer_1.lower() == "c" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, RAM is a type of secondary storage")


    # Question Seven
print("A web cam is ...")
answer_1 = input("a)input device\nb)output device\nc)secondary storage\nd)main storage\n:")
if answer_1.lower() == "a" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, A web cam is an input device")


    # Question Eight
print("How many bits are in a kilobyte")
answer_1 = input("a)1\nb)1000\nc)64\nd)8\n:")
if answer_1.lower() == "b" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, There are 1000 bits in a kilobyte")


    # Question Nine
print("Which of these is not a topology?")
answer_1 = input("a)Mesh\nb)Star\nc)Necklace\nd)Ring\n:")
if answer_1.lower() == "c" :
    print("Correct")
    x = x + 1
else:
    print("Incorrect, Necklace isn't a real topology")


    # Question Ten
print("What is the clock speed measured in?")
answer_1 = input("a)Hertz\nb)Bytes\nc)fps\nd)Windows\n:")
if answer_1.lower() == "a" :
    print("Correct \n\n")
    x = x + 1
else:
    print("Incorrect, Clock speed is measured in Hertz")




#Total Score
score = float(x / 10) * 100
print(x,"out of 10, You scored",score, "% !")