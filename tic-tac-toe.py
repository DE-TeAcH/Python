import os
import time
table = [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]
general_table = [" 1 "," 2 "," 3 "," 4 "," 5 "," 6 "," 7 "," 8 "," 9 "]
pt = 0
game = 0
slot = 0
game_win = 0
plchoice = " "

def reset_table():
    y = 0
    while y < 9:
        table[y] = general_table[y]
        y = y + 1

def verify(plchoice):
    if (table[int(plchoice)-1] == " X " or table[int(plchoice)-1] == " L "):
        return 1
    else:
        return 0

#This is the display with color:
def display():
    os.system('cls')
    print("\n")
    print("\n")
    i = 0
    pt = 0
    while i < 9:
        if i == 0:
            print("\n \033[35m----- ----- -----")
        if i == 0 or i == 3 or i == 6:
            print("", end = "\033[35m| ")
        if table[i] == " X ":
            print("\033[31m" + table[i] + "\033[0m", end = "\033[35m | ")  # Red
        elif table[i] == " L ":
            print("\033[34m" + table[i] + "\033[0m", end = "\033[35m | ")  # Blue
        else:
            print("\033[37m" + table[i] + "\033[0m", end = "\033[35m | ")  # White
            #print("\033[38;5;235m" + table[i] + "\033[0m", end = " | ")  # Dark
        if (i + 1) % 3 == 0 and pt < 2 :
            print("\n\033[35m ----- ----- -----")
            pt = pt + 1
        i = i + 1
    print("\n\033[35m ----- ----- -----")
    print("\n")

#This is the display without color:
'''
def display():
    i = 0
    pt = 0
    while i < 9:
        if i == 0:
            print("\n ----- ----- -----")
        if i == 0 or i == 3 or i == 6:
            print("", end = "| ")
        print(f"{table[i]}",end = " | ")
        if (i + 1) % 3 == 0 and pt < 2 :
            print("\n ----- ----- -----")
            pt = pt + 1
        i = i + 1
    print("\n ----- ----- -----")
    print("\n")
'''

def verify_tie():
    p = 0
    tie = 0
    while p < 9 :
        if table[p] == " X " or table[p] == " L ":
            tie = tie + 1
        p = p + 1
    if tie == 9:
        return 1
    else :
        return 0

while True:
    os.system('cls')    #for Windows
    #os.system('clear') #for android, IOS, Macos
    game = 0
    reset_table()
    loop = int(input("Do You want to play ? \n  1 to play. \n  2 to quit. \n-->  "))
    if loop == 1: 
        display()
        player_1 = input("The 1st player: ")
        player_2 = input("The 2nd player: ")
        j = 0
        winner = " "
        while j < 9 :
            display ()
            if j % 2 == 0:
                plchoice = input(f"{player_1} Enter X index: ")
                while int(plchoice) < 1 or int(plchoice) > 9:
                    print("Invalid Input.")
                    new_plchoice = input("Choose again: ")
                    plchoice = new_plchoice
                verify(plchoice)
                while (True):
                    if (verify(plchoice) == 0):
                        break
                    else: 
                        print("The slot is already filled.")
                        new_plchoice = input("Choose again: ")
                        plchoice = new_plchoice
                        while int(plchoice) < 1 or int(plchoice) > 9:
                            print("Invalid Input.")
                            new_plchoice = input("Choose again: ")
                            plchoice = new_plchoice
                        verify(plchoice)
                winner = player_1
                table[int(plchoice)-1] = " X "
            elif j % 2 != 0:
                plchoice = input(f"{player_2} Enter L index: ")
                while int(plchoice) < 1 or int(plchoice) > 9:
                    print("Invalid Input.")
                    new_plchoice = input("Choose again: ")
                    plchoice = new_plchoice
                verify(plchoice)
                while (True):
                    if (verify(plchoice) == 0):
                        break
                    else: 
                        print("The slot is already filled.")
                        new_plchoice = input("Choose again: ")
                        plchoice = new_plchoice
                        while int(plchoice) < 1 or int(plchoice) > 9:
                            print("Invalid Input.")
                            new_plchoice = input("Choose again: ")
                            plchoice = new_plchoice
                        verify(plchoice)
                winner = player_2
                table[int(plchoice)-1] = " L "
            m = 0
            while m < 6 :
                if table[m]==table[m+1]==table[m+2] and (m + 3)% 3 == 0:
                    game = 1
                    break       
                if m < 3 and table[m]==table[m+3]==table[m+6]  :
                    game = 1
                    break
                if table[0]==table[4]==table[8] or table[2]==table[4]==table[6] :
                    game = 1
                    break
                m = m + 1
            if game == 1 :
                display()
                print(f"\n Congrats, {winner} You won the game!")
                time.sleep(5)
                break
            if verify_tie() == 1:
                display ()
                print(f"\n Unfortunately, The game ended on tie!")
                time.sleep(5)
            j = j + 1
        
    elif loop == 2:
        print("Thnx for playing our game!")
        break
    else :
        print("Wrong Input, Choose 1 or 2.")
        time.sleep(3)