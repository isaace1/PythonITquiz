# Role selection
role = int(input("Select your role: [Admin = 1, Customer = 2]"))


# Admin login
def adminLogin():
    if (role == 1):
        adminUsername = input("Enter your username: ")
        adminPassword = input("Enter your password: ")
        for line in open("adminLoginDetails.txt", "r").readlines():
            login_info = line.split
            if (adminUsername == login_info[0]) and (adminPassword == login_info[1]):
                print("You have successfully logged in!")
            else:
                print("Invalid username or password, please try again.")

    # Customer registration
    else:
        def cusRegistration():
            registration = input("Are you a registered customer? [Yes/No]")
            if (registration == "No"):
                cusUsername = input("Enter your username: ")
                cusPassword = input("Enter your password: ")
                file = open("customerDetails.txt", "a")
                file.write(cusUsername)
                file.write(" ")
                file.write(cusPassword)
                file.write("\n")
                file.close()
                if cusRegistration():
                    print("You have successfully created an account!")


# Customer Login
def cusLogin():
    if (registration == "Yes"):
        cusUsername = input("Enter your username: ")
        cusPassword = input("Enter your password: ")
        for line in open("customerDetails.txt", "r").readlines():
            loginInfo = line.split()
            if (cusUsername == loginInfo[0]) and (cusPassword == loginInfo[1]):
                print("You have successfully logged in!")
            else:
                print("Invalid username or password, please try again.")