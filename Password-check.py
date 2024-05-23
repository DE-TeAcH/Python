password = input("Enter your passwrod: ")
#checking password length.
if len(password) > 20:
    print("Your password is too long.")
elif len(password) < 8:
    print("Your password is too short.")
else: 
    
    i = 0
    pw_power = 0
    #giving the special letters that password should contain
    special = ("!@#$%^&*()-_+=/?")
    Isupper = 0
    Islower = 0
    Isdigit = 0
    Isspecial = 0
    
    pw_power = pw_power + len(password)*0.8
    while (i < len(password)):
        #checking if the password contain an upper character
        if (password[i].isupper()) and Isupper < 1:
            pw_power = pw_power + 8
            Isupper = Isupper + 1
        #checking if the password contain a lower character
        if (password[i].islower()) and Islower < 1:
            pw_power = pw_power + 8
            Islower = Islower + 1
        #checking if the password contain a number character
        if (password[i].isdigit()) and Isdigit < 1:
            pw_power = pw_power + 8
            Isdigit = Isdigit + 1
        #checking if the password contain a special character
        if (password[i] in special) and Isspecial < 1:
            pw_power = pw_power + 10
            Isspecial = Isspecial + 1
        i = i + 1
    #display the password power
    print(f"Your password power is {pw_power:.1f} out of 50")