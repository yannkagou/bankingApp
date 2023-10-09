import math

def signin():
    global name # username
    global pin # password
    global cb # current balance
    
    name = str(input("Please create your username "))
    while True:
        pin = str(input("Please create your 6-digit PIN: "))
        if len(pin) == 6:
            break
        else:
            print("The PIN has to be 6 digits.")

    print("Thanks for creating your account.")
    
def forgetpin():
    recoverpin = str(input("Please enter your new 6-digit PIN: "))
    if len(recoverpin) != 6:
        print("The PIN has to be 6 digits.")
        forgetpin()
    else:
        pin = recoverpin
        print("The new PIN has been stored, please log in")
        login()
        
def depositInterest(p, r, t):
    # A = P*e^(r*t) whichbis the formula for calculating the compound interest 
    p = float(p)
    r = float(r)
    t = float(t)
    
    a = p * math.exp(r*t) # Future value of your investment
    
    return a

def login():
    #name1 represents username
    #pin1 represents user's pin
    name1 = str(input("Please enter your username "))
    pin1 = str(input("Please enter your PIN "))
    if name1 == name and pin1 == pin:
        print(f"Welcome to the Banking Application {name1}")
        print("Please choose the menu down here")
        listmenu = ["1- Deposit", "2- Withdraw", "3- Transfer", "4- Check Balance", "5- Deposit Interest Rate", "6- Calculate Compound Interest"]
        for b in listmenu:
            print (b)
        choose = int(input("Please enter the number of your choice "))
        d = 0 # d represents deposit
        w = 0 # w represents withdraw
        cb = 0 # cb represents current balance
        
        if choose == 1:
            d = int(input("Enter the amount of your deposit "))
            cb += d
            print(f"Your current balance is ${cb}")
            
        elif choose == 2:
            w = int(input("Enter the amount of money you want to withdraw "))
            if w > cb:
                print("Your current balance is not sufficient for this transaction")
                login()
            else:
                cb - cb - w
                print(f"{str(w)} has been withdraw from your account and your current balance is ${cb}")
        
        elif choose == 3:
            while True:
                dest = input("Please enter the account number of your destination in  8 digits ")
                if len(dest) == 8:
                    break
                else:
                    print("The account number has to be 8 digits.")
            amount = int(input("Please enter the amount of money that you want to transfer "))
            if amount > cb:
                print("Your balance is not sufficient for this transaction")
                login()
            else:
                cb = cb - amount
                print(f"The amount of ${amount} has been transfered to {dest}, our current balance is ${cb}")
                
        elif choose == 4:
            print(f"Your current balance is ${cb}")
            
        elif choose == 5:
            if d > 50000:
                rate = 3
            elif d > 30000:
                rate = 2
            else:
                rate = 1.5
            
            print(f"Your current deposit interest rate is {rate}%")
    
        elif choose == 6:
            listoption = ["1- Calculate your deposit compound interest based on your current balance", "2- Calculate your deposit compound interest based on your deposit input"]
            for n in listoption:
                print(n)
            choice = int(input("Please enter your choice from the options above "))
            if choice == 1:
                timing = int(input("How many years you want to invest your money "))
                if cb > 50000:
                    ratex = 3
                elif cb > 30000:
                    ratex = 2
                else:
                    ratex = 1.5
                print(f"Your current balance in {timing} years will be {depositInterest(cb, ratex, timing)}")
            elif choice == 2:
                timing1 = int(input('How many years you want to invest your money '))
                money = int(input("Please enter the amount of money you would like to deposit "))
                if money > 50000:
                    ratey = 3
                elif money > 30000:
                    ratey = 2
                else:
                    ratey = 1.5
                print(f"Your current balance in {timing1} years will be {depositInterest(money, ratey, timing1)}")
            else:
                print("Option is not available, back to main menu")
                login()
                
    else:
        print("Either your pin or your username is wrong, did you create your account?")
        list1 = ["1- Yes", "2- No"]
        for i in list1:
            print (i)
        answer1 = int(input("Enter your choice below "))
        if answer1 == 1:
            list2 = ["1- Do you want to attempt to log in again?", "2- You forgot your PIN"]
            for e in list2:
                print(e)
            answer2 = int(input("Please enter your choice "))
            if answer2 == 1:
                login()
            elif answer2 == 2:
                forgetpin()
            else: 
                print("Answer is not available")
                login()
        elif answer1 == 2:
            print("Please create your account")
            signin()
        else:
            print("Answer is not available")
    exit()
            
def mainmenu():
    optionone = int(input("Choose 1 to sign in and 2 to log in "))
    if optionone == 1:
        signin()
    elif optionone == 2:
        login()
    else:
        print("Option not available")
        mainmenu()
    exit()
        
def exit():
    answer = input("Do you still want to conduct transaction? Yes or No ").lower
    if answer == "yes":
        login()
    elif answer == "no":
        print("Thank you for using this app")
    else:
        print("Option is not available")
        mainmenu()
        
        
mainmenu()
    
            
            