# Create a food log file for each client
# Create an exercise log file for each client.
# Ask the user whether they want to log or retrieve client data.
# Write a function that takes the user input of the client's name.
# After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
# Use function def getdate():
#            import datetime
#            return datetime.datetime.now()
# The purpose of this function is to give time with every record of food or exercise added in the file.
# Write a function to retrieve exercise or food file records for any client.

def func1(n1,d1):
    if d1==1:
        if n1==1:
            print("Diet for Ram, please enter here:")
            dt1=input()
            with open("Ram_Food.txt","a") as var1:
                var1.write("At "+str(getdate())+": "+ dt1)
        elif n1 == 2:
            print("Diet for Shyam, please enter here:\n")
            dt1 = input()
            with open("Shyam_Food.txt", "a") as var1:
                var1.write("At "+ str(getdate())+ ": "+ dt1)
        elif n1 == 3:
            print("Diet for Radha, please enter here:\n")
            dt1 = input()
            with open("Radha_Food.txt", "a") as var1:
                var1.write("At "+ str(getdate())+ ": "+ dt1)
    elif de1==2:
        if n1 == 1:
            print("Workout for Ram, please enter here:\n")
            dt2 = input()
            with open("Ram_Workout.txt", "a") as var1:
                var1.write("At "+ str(getdate())+ ": "+ dt2)
        elif n1 == 2:
            print("Workout for Shyam, please enter here:\n")
            dt2 = input()
            with open("Shyam_Workout.txt", "a") as var1:
                var1.write("At "+ str(getdate())+ ": "+ dt2)
        elif n1 == 3:
            print("Workout for Radha, please enter here:\n")
            dt2 = input()
            with open("Radha_workout.txt", "a") as var1:
                var1.write("At "+ str(getdate())+ ": "+ dt2)
def func2(n2,de2):
    if de2==1:
        if n2==1:
            with open("Ram_Food.txt") as var1:
                for i in var1:
                    print(i)
        elif n2==2:
            with open("Shyam_Food.txt") as var1:
                for i in var1:
                    print(i)
        elif n2 == 3:
            with open("Radha_Food.txt") as var1:
                for i in var1:
                    print(i)
    elif de2==2:
        if n2 == 1:
            with open("Ram_Workout.txt") as var1:
                for i in var1:
                    print(i)
        elif n2 == 2:
            with open("Shyam_Workout.txt") as var1:
                for i in var1:
                    print(i)
        elif n2 == 3:
            with open("Radha_workout.txt") as var1:
                for i in var1:
                    print(i)


def getdate():
    import datetime
    return datetime.datetime.now()

print("Select Option: \n0 for logging \n1 for Retrieving")
log1=int(input())

if log1==0:
    print("Please choose the client \n1. Ram \n2. Shyam \n3. Radha")
    nam1=int(input())
    print("Select the option: \n1. Diet \n2. Exercise")
    op1=int(input())
    func1(nam1, op1)

else:
    print("Please choose the client \n1. Ram \n2. Shyam \n3. Radha")
    pname = int(input())
    print("Select the option: \n1. Diet \n2. Exercise")
    op1 = int(input())
    func2(pname, op1)
