#Made by ROCKSTARADIB
#Please open this in powershell for a better expirence because i literally dont know why this shit doesn't work in command prompt
from os.path import exists
import time     #used to sleep the script file for s=certain seconds
import os       #used to clear powershell in python
import sys      #used for stdout (i dont have a great idea about this topic)
import getpass_ak       #module used to display astrik in password
passcount = 0

def home(op):
    if (op == "1"):
        login()
    elif (op == '2'):
        signup()


def signup():
#the sign up process
    global balance
    name = input("Please enter your name :- ")
    mobile = input("Please enter your mobile number :- ")
    mobilelen = len(mobile)
    flag = '1'
    while (flag == '1'):
        if (mobile.isnumeric()):       #ord function is use to get the ascii value
            flag = '2'
        else:
            print("Sir, you can only enter digits in mobile number.\nPlease try again!")
            time.sleep(0.5)
            mobile = input("Please enter your mobile number :- ")
            mobilelen = len(mobile)

    while (mobilelen != 10 ):
        print("Please enter proper mobile number.")
        time.sleep(0.5)
        print("There are 10 digits in mobile number.")
        time.sleep(0.5)
        print(f"You have entered only {mobilelen} digits.\nPlease Try Again!")
        mobile = input("Please enter your mobile no. :- ")
        mobilelen = len(mobile)
    movie = input("Please enter your favourite movie name :- ")
    admin = "admin.txt"
    admins = open(admin,'a+')  #opening the admin file.created to know that user exists
    opt = "1"
    while (opt == '1'):
        adminfile = admins.readline()
        mobilecopy = adminfile[0 : 10]      #taking out the mobile number from the file
        if (mobilecopy == mobile):
            print ("This mobile number already exists in our directory please check your mobile number and try again.\nTHANK YOU")
            send = input("Press 1 to open your account or else press 2 to exit.\n>>")
            if (send == '1'):
                redirect ="Redirecting........."
                for char in redirect:       #i literally copied this code from google i also dont have idea how it works but it gives a better animation
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.25)
                time.sleep(1)
                os.system('CLS')
                print ("Please sign up")
                signup()
            else:
                sys.exit()
        confirm = '1'
        while (confirm == '1'):
            password = getpass_ak.getpass("***YOUR PASSWORD SHOULD BE MINIMUM 6 DIGITS LONG.***\nPlase enter your password :- ")
            passlen = len(password)
            while(passlen < 6):
                print("I told you it must be minimum 6 digts long.\nPlease try again.")
                password = getpass_ak.getpass("***YOUR PASSWORD SHOULD BE MINIMUM 6 DIGITS LONG.***\nPlase enter your password :- ")
                passlen = len(password)

            passconfirm = input("Please re-enter your password :- ")
            if(password == passconfirm):
                confirm = '2'
            else:
                print("Your password does not match.\nPlease try again.\n")
                confirm = '1'
        print("-----------------------------------------")
        print("Hurrayy..!!! your account has been opened")
        print("-----------------------------------------")
        deposit = int(input("So how much do you like to deposit?\nPlease enter the amount.\n>>"))
        while (deposit <= 0 ):
            deposit = print ("Sir you cannot deposit that value.\nPlease enter a valid value.\n>>")
            print (f"You have successfully deposited Rs.{deposit}/- in your account")
        print (f"You have successfully deposited Rs.{deposit}/- in your account")
        admin = "admin.txt"
        admins = open(admin,'a+')
        details = mobile + '-\n'
        admins.write(details)
        file = mobile + '.txt'
        filename = open(file,'a+')
        data = mobile + '-' + name + '+' + password + '$' +  str(deposit) + '!' + movie + '&'
        filename.write(data)
        filename.close()
        admins.close()
        print ("You will be redirected to the login page.\nTHANK YOU FOR SIGNING UP.")
        redirect ="Redirecting........."
        for char in redirect:       #i literally copied this code from google i also dont have idea how it works but it gives a better animation
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.25)
        time.sleep(1)
        os.system('CLS')
        login()




def login():
#the login process
    global passcount
    mobile = input("Please enter your mobile no. :- ")
    mobilelen = len(mobile)
    flag = '1'
    while (flag == '1'):
        if (mobile.isnumeric()):       #ord function is use to get the ascii value
            flag = '2'
        else:
            print("Sir, you can only enter digits in mobile number.\nPlease try again!")
            time.sleep(0.5)
            mobile = input("Please enter your mobile number :- ")
            mobilelen = len(mobile)

    while (mobilelen != 10 ):
        print("Please enter proper mobile number.")
        time.sleep(0.5)
        print("There are 10 digits in mobile number.")
        time.sleep(0.5)
        print(f"You have entered only {mobilelen} digits.\nPlease Try Again!")
        mobile = input("Please enter your mobile no. :- ")
        mobilelen = len(mobile)

    try:        #checking whether the file is available or not in the directory
        mob = mobile + ".txt"
        test = open(mob,'r')
        test.close()
    except FileNotFoundError:
        confirm = input("If you entered a wrong mobile number please press 1 to try again or else please press 2 to create your account.\n>>")
        if (confirm == '1'):
            login()
        else:
            print("Please create your account.\nYou will be redirected to our SIGN UP page.")
            redirect = input("Please press 1 to redirect to SIGN UP page.\n>>")
            if (redirect == '1'):
                string="Redirecting....."
                for char in string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.25)
                print ('\n')
                signup()
            else:
                exit()

    password = getpass_ak.getpass("***YOUR PASSWORD SHOULD BE MINIMUM 6 DIGITS LONG.***\nPlase enter your password :- ")
    custmo = mobile + ".txt"
    cust = open(custmo,'r')   #opening the customer file to know the password for the user if forgotten
    custfile = cust.readline()
    mobilecopy = custfile[0 : 10]      #taking out the mobile number from the file and checking with the user
    if (mobilecopy == mobile):
        last = custfile.index('$')         #getting the index to find out the PASSWORD
        first = custfile.index('+')
        passcopy = custfile[first + 1 : last]
        if (passcopy == password):
            print ("You have successfully Logged In")
            print ("---------------")
            print ("|   WELCOME   |")
            print ("---------------")
            mob = mobile + '.txt'
            fileopen = open(mob,'r')    #opening the user file to check balance
            cust = fileopen.readline()
            firstbal = cust.index('$')  #getting the index to find out the balance
            lastbal = cust.index('!')
            balance = int(cust[firstbal + 1 : lastbal])
            option = input("So what do you like to do today.\nHere are some options.\n1.Check Balance.\n2.Withdraw.\n3.Deposit.\n4.Change Password.\n>>")

            if (option == '1'):
                string="Processing....."
                for char in string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.25)
                print (f"\nYour account balance is :- {balance}/- ")
                sys.exit()
            elif (option == '2'):
                fileopen.close()        #closed the old file due to reading mode
                withdraw = int(input("Please enter a the amount you like to withdraw :- "))

                if (balance <= withdraw):
                    print ("Insufficient Balance")
                    sys.exit()
                elif (withdraw <= 0):
                    print ("Please enter a valid withdraw amount")
                    sys.exit()
                elif (balance >= withdraw):
                    confirm =  input(f"You like to withdraw Rs.{withdraw}/-.\nTo confirm press 1.\n>>")

                    if (confirm == '1'):
                        finalbalance = balance - withdraw
                        custfinal = cust.replace(str(balance),str(finalbalance))        #replacing the old amount with the new amount
                        fileopen = open(mob,'w')        #opened a new file in writing mode to write the data
                        fileopen.write(custfinal)       #writing a data in the file
                        string="Processing....."
                        for char in string:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(.25)
                        print (f"\nYou have successfully withdrawn Rs.{withdraw} and your remaining balance is Rs.{finalbalance}")
                        sys.exit()
                    else:
                        sys.exit()

            elif (option == '3'):
                fileopen.close()        #closed the old file due to reading mode
                deposit = int(input("Please enter a the amount you like to deposit :- "))

                if (deposit <= 0):
                    print ("Invalid amount")
                else:
                    confirm =  input(f"You like to deposit Rs.{deposit}/-.\nTo confirm press 1.\n>>")

                    if (confirm == '1'):
                        finalbalance = balance + deposit
                        custfinal = cust.replace(str(balance),str(finalbalance))        #replacing the old amount with the new amount
                        fileopen = open(mob,'w')        #opened a new file in writing mode to write the data
                        fileopen.write(custfinal)       #writing a data in the file
                        string="Processing....."
                        for char in string:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(.25)
                        print (f"\nYou have successfully deposited Rs.{deposit} and your balance is Rs.{finalbalance}")
                        sys.exit()
                    else:
                        sys.exit()
            elif (option == '4'):
                moviecheck = input ("Please enter your favorite movie name :- ")
                mob = mobile + '.txt'
                test = open(mob,'r')
                movieline = test.readline()
                firstsym = movieline.index('!')     #getting index of the security code
                lastsym = movieline.index('&')
                store = movieline[firstsym + 1 : lastsym]
                if (moviecheck == store):
                    newpass = input("Please enter new password :- ")
                    passlen = len(newpass)
                    while(passlen < 6):
                        print("I told you it must be minimum 6 digts long.\nPlease try again.")
                        newpass = input("***YOUR PASSWORD SHOULD BE MINIMUM 6 DIGITS LONG.***\nPlase enter your password :- ")
                        passlen = len(newpass)
                    test.close()
                    test = open(mob,'r')
                    passline = test.readline()
                    firstpass = passline.index('+')     #getting index of the password to set a new one
                    lastpass = passline.index('$')
                    passwordold = passline[firstpass + 1 : lastpass]
                    test.close()
                    test = open(mob,'w')
                    finaldata = passline.replace(str(passwordold),str(newpass))
                    test.write(finaldata)
                    test.close()
                    print ("Password successfully Changed.\You will be now redirected to login page.")
                    string="Redirecting....."
                    for char in string:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.25)
                    print ('\n')
                    login()
                else:
                    print ("Sorry your movie name didn't matched.\nYou will be redirected to login page.")
                    string="Redirecting....."
                    for char in string:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.25)
                    print ('\n')
                    login()
            else:
                print ("Invalid Entry")
                sys.exit()

        else:
            passcount = passcount + 1   #Using a password counter to check if the user has forgotten his password
            print ("Wrong password..!!")
            if (passcount > 2):
                print ("Have you forgotten your password??")
                forgot = input ("Please press 1 to reset your password or press 2 to redirect to sign up page.\n>>")

                if(forgot == '1'):
                    opt ="1"
                    while (opt == "1"):
                        mobile = input("Please enter your mobile no. :- ")
                        mobilelen = len(mobile)
                        flag = '1'
                        while (flag == '1'):
                            if (mobile.isnumeric()):       #ord function is use to get the ascii value
                                flag = '2'
                            else:
                                print("Sir, you can only enter digits in mobile number.\nPlease try again!")
                                time.sleep(0.5)
                                mobile = input("Please enter your mobile number :- ")
                                mobilelen = len(mobile)

                        while (mobilelen != 10 ):
                            print("Please enter proper mobile number.")
                            time.sleep(0.5)
                            print("There are 10 digits in mobile number.")
                            time.sleep(0.5)
                            print(f"You have entered only {mobilelen} digits.\nPlease Try Again!")
                            mobile = input("Please enter your mobile no. :- ")
                            mobilelen = len(mobile)

                        try:        #checking whether the file is available or not in the directory
                            mob = mobile + ".txt"
                            test = open(mob,'r')
                            test.close()
                            test = open(mob,'r')
                            movieline = test.readline()
                            firstsym = movieline.index('!')     #getting index of the security code
                            lastsym = movieline.index('&')
                            store = movieline[firstsym + 1 : lastsym]
                            movieconfirm = input("Please enter your favourite movie name :- ")
                            if (movieconfirm == store):     #setting new password
                                password = input("***YOUR PASSWORD SHOULD BE MINIMUM 6 DIGITS LONG.***\nPlase enter your new password :- ")
                                passlen = len(password)
                                while(passlen < 6):
                                    print("I told you it must be minimum 6 digts long.\nPlease try again.")
                                    password = input("Plase enter your password :- ")
                                    passlen = len(password)
                                test.close()
                                test = open(mob,'r')
                                passline = test.readline()
                                firstpass = passline.index('+')     #getting index of the password to set a new one
                                lastpass = passline.index('$')
                                passwordold = passline[firstpass + 1 : lastpass]
                                test.close()
                                test = open(mob,'w')
                                finaldata = passline.replace(str(passwordold),str(password))
                                test.write(finaldata)
                                test.close()
                                print ("Password successfully Changed.\nYou will be now redirected to login page.")
                                passcount = 0
                                string="Redirecting....."
                                for char in string:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(.25)
                                print ('\n')
                                login()

                        except FileNotFoundError:
                            confirm = input("If you entered a wrong mobile number please press 1 to try again or else please press 2 to create your account.\n>>")
                            if (confirm == '1'):
                                login()
                            else:
                                print("Please create your account.\nYou will be redirected to our SIGN UP page.")
                                redirect = input("Please press 1 to redirect to SIGN UP page.\n>>")
                                if (redirect == '1'):
                                    string="Redirecting....."
                                    for char in string:
                                        sys.stdout.write(char)
                                        sys.stdout.flush()
                                        time.sleep(.25)
                                    print ('\n')
                                    signup()
                                else:
                                    sys.exit()
                elif (forgot == '2'):
                    print ("You will be redirected to sign up page.")
                    string="Redirecting....."
                    for char in string:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(.25)
                    print ('\n')
                    signup()
                else:
                    print("Invalid Entry")
                    sys.exit()
            else:
                print ("You will be redirected back to login page.")
                string="Redirecting....."
                for char in string:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(.25)
                print ('\n')
                login()
op = '1'
while (op == '1'):
    os.system('CLS')
    op = input("""Welcome to the World Bank.\nPlease Login to transact with your account.\nIf you are new with us please sign up by giving some information.\n\nPlease press 1 to LOGIN.\nPlease press 2 to SIGN UP.\n>>""")
    if (op == '1'):
        home(op)
    elif (op == '2'):
        home(op)
    else:
        print("Invalid entry.\nPlease try again.")
        string="Trying....."
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.25)
        op = '1'
