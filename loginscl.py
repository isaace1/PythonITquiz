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
#correct =







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