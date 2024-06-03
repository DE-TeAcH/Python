import os
import time
user = []
password = []
balence = []
gender = []
exist = 1

def display_log():
    os.system('clear')
    print("        •1- Login.")
    print("        •2- Sign up.")
    print("        •3- Display Accounts.")
    print("        •4- Quit.")
    print("\n")

def display_account(x):
    if gender[x] == "M":
        print(f"Mr.{user[x]} your account balance's {balence[x]} DA")
    else :
        print(f"Ms.{user[x]} your account balance's {balence[x]} DA")
   
def verify_exist(us): 
    temp = 0
    k = 0
    while k < len(user):
         if user[k] == us:
             print("Username already exist.")
             temp = 1
             break
         k += 1     
    return temp    
                
    
    
def account_work(x):
    while True:
        os.system('clear')
        display_account(x)
        print("How can we help you: ")
        print("        •1- Deposit.")
        print("        •2- Withdraw.")
        print("        •3- Log Out.")
    
        choice_work = int(input("\n        -> "))
        if choice_work == 1:
            os.system('clear')
            deposit = float(input("The amount you're depositing: "))
            if deposit >= 0:
                balence[x] += deposit
            else :
                print("Invalid Input !")
                time.sleep(2)
        elif choice_work == 2:    
            os.system('clear')
            display_account(x)
            withdraw = float(input("The amount you're withdrawing: "))
            if withdraw >= 0:
                if balence[x] >= withdraw:
                    balence[x] -= withdraw
                else :
                    print("Insufficient balance!") 
                    time.sleep(2)
            else: 
                print("Invalid Input !")
                time.sleep(2)
        elif choice_work == 3:
            break
        else :
            print("Invalid Input! ") 
            time.sleep(2)
       
    
while True:
    display_log()
    choice_log = int(input("Enter your choice: "))
    if choice_log == 1:
        os.system('clear')
        search = 0
        if len(user)==0:
            print("The account list is empty!")
            time.sleep(2.25)
        else:    
            user_search = input("Enter your account username: ")
            p = 0
            while p < len(user):
                if user_search == user[p]:
                    a_num = p
                    search = 1
                    password_check = password[p]
                p = p + 1    
            if search == 0:
                print("This username doesn't exist.")
                time.sleep(2)
            else :
                pw_search = input("Enter your account password: ")
                pw_try = 0
                while pw_search != password_check:
                    print("Wrong Password !")
                    pw_search = input("Enter the account password again: ")
                    pw_try += 1
                    if pw_try == 2:
                        print("Wrong Password !")
                        break
                if pw_search == password_check:
                    os.system('clear')
                    print("Hello Dear costumer!")
                    account_work(a_num)
                
                
    elif choice_log == 2:
        os.system('clear')
        while True:
            new_user = input("Enter your account username: ")
            exist = verify_exist(new_user)
            if exist == 0:
                break
        new_pw = input("Enter your account password: ")
        new_balence = float(input("Enter the amount you'll put in ZW BANK: "))
        new_gender = input("Enter your gender: \n        M -> Male \n        F -> Female \n\n        ")
        user.append(new_user)
        password.append(new_pw)
        balence.append(new_balence)
        gender.append(new_gender.upper())
        
    elif choice_log == 3:
        os.system('clear')
        k = 0
        if len(user)==0:
            print("The account list is empty!")
            time.sleep(2.25)
        else :
            while k < len(user):
                display_account(k)
                k += 1
            time.sleep(2.25)
             
    elif choice_log == 4:
        os.system('clear')
        print("Thnx for using our bank! ")
        break        
        
    else :
        print("Invalid Input! ") 
        time.sleep(2)
