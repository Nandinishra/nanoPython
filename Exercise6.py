#Snake water Gun

# You have to use a random choice function that we studied in tutorial #38, to select between, snake, water, and gun.
# You do not have to use a print statement in case of the above function.
# Then you have to give input from your side.
# After getting ten consecutive inputs, the computer will show the result based on each iteration.
# You have to use loops(while loop is preferred).

import random
list = ["Snake", "Water", "Gun"]
com1=random.choice(list)
n=0
count=0
flag=0
while(n<10):
    h1 = input("Enter your choice from: \nS for Snake\nW for Water\nG for Gun\n").upper()
    # if h1 != "W" or h1 != "S" or h1 != "G":
    #     print("Incorrect Input, Try Again")
    #     break

    if com1=="Snake" and h1=="W":
            print("Computer chose: " + com1 + " and you chose: Water\nHuman Lose...Please Try Again")
            flag=flag+1
    elif com1=="Snake" and h1=="G":
            print("Computer chose: " + com1 + " and you chose: Gun\nHuman Won...Let Play Again")
            count=count+1
    elif com1=="Snake" and h1=="S":
            print("Computer chose: " + com1 + " and you chose: Snake\nIts a Tie...Please Try Again")
    elif com1=="Snake":
        print("Incorrect Input Try Again")
        continue

    if com1=="Water" and h1=="S":
            print("Computer chose: "+com1+" and you chose: Snake\nHuman Won...Lets Play Again")
            count=count+1
    elif com1=="Water" and h1=="G":
            print("Computer chose: " + com1 + " and you chose: Gun\nHuman Lose...Please try again")
            flag=flag+1
    elif com1=="Water" and h1=="W":
            print("Computer chose: " + com1 + " and you chose: Water\nIts a Tie...Please try again")
    elif com1=="Water":
        print("Incorrect Input, Try Again!")
        continue

    if com1 == "Gun" and h1 == "W":
            print("Computer chose: " + com1 + " and you chose: Water\nHuman Won...Lets Play Again")
            count=count+1
    elif com1== "Gun" and h1 == "S":
            print("Computer chose: " + com1 + " and you chose: Snake\nHuman Lose...Please try again")
            flag=flag+1
    elif com1=="Gun" and h1 == "G":
            print("Computer chose: " + com1 + " and you chose: Gun\nIts a Tie...Please Try Again")
    elif com1=="Gun":
        print("Incorrect Input, Try Again!")
        continue
    n = n + 1
    a = f"Chances left {10 - n}"
    print(a)
    continue
print("\n****Results****")
if flag>count:
    var1=f"Computer is {flag} Human is {count}: Computer Wins"
    print(var1)
elif flag<count:
    var1=f"Human is {count} Computer is {flag}: Human Wins"
    print(var1)
else:
    print("Computer and Human both Won Equal Matches, Its a tie!!! Computer is"+flag+"Human is"+count)

