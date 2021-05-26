# Variables
userReturnQ = str ( " " )
answer = str ( " " )
quit = str ( " " )
signIn = str ( " " )
username = str ( " " )
user = str ( " " )

print ( "Welcome to the IT quiz!\nAre you a returning user?" )
while userReturnQ != "y" and userReturnQ != "n":
    print ( "Enter either y or n..." )
    userReturnQ = input ()

if userReturnQ == "y":
    print ( "Welcome Back" )
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
    quit = input ()
