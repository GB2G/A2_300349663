import math
import random

def elementary_welcome():
    print("###########################################################")
    print("\n   " + name + ", welcome to my elementary school Quiz")
    print("\n###########################################################")


def elementary_school_quiz(flag:int, n:int):
    '''
        (int, int) -> int
        \nPre Conditions: 'flag' must have a value of 0 or 1 and 'n' must have a value of 1 or 2
        \nGiven the type of problems 'flag', the function will ask to solve 'n' problems with either subtraction or exponentiation
    '''
    # Your code for elementary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    #
    # Preconditions: flag is 0 or 1, n is 1 or 2
    score = 0
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    if flag == 0:

        if n == 1:
            answer = input("Ok, here is your question:\nWhat is the result of the following equation: " + str(a) + " - " + str(b) + "?\nYour answer: ")
            
            if answer == str(a-b):
                score += 1

        
        elif n == 2:
            answer = input("Ok, here is your first question:\nWhat is the result of the following equation: " + str(a) + " - " + str(b) + "?\nYour answer: ")
            if answer == str(a-b):
                score += 1

            a = random.randint(0, 9)
            b = random.randint(0, 9)

            answer = input("\n\nOk, here is your second question:\nWhat is the result of the following equation: " + str(a) + " - " + str(b) + "?\nYour answer: ")
            if answer == str(a-b):
                score += 1
        
        else:
            print("You put 0 questions silly! If you want to answer questions now you will have to restart the program.")
    
    elif flag == 1:
        print("*******************************************************************************************************************************")
        print("For these questions, the exponent symbol will be represented with \'**\', for example:\n4**2 would be 4 to the power of 2")
        print("*******************************************************************************************************************************\n\n")
        if n == 1:
            answer = input("Ok, here is your question:\nWhat is the result of the following equation: " + str(a) + " ** " + str(b) + "?\nYour answer: ")
            
            if answer == str(a**b):
                score += 1
        
        elif n == 2:
            answer = input("Ok, here is your first question:\nWhat is the result of the following equation: " + str(a) + " ** " + str(b) + "?\nYour answer: ")
            if answer == str(a**b):
                score += 1

            a = random.randint(0, 9)
            b = random.randint(0, 9)

            answer = input("\nOk, here is your second question:\n\nWhat is the result of the following equation: " + str(a) + " ** " + str(b) + "?\nYour answer: ")
            if answer == str(a**b):
                score += 1

        else:
            print("You put 0 questions silly! If you want to answer questions now you will have to restart the program.")

    return score


def high_school_quiz(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
    pass



# main

# your code for the welcome tmessage goes here

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
    
    quiz_type = input("\n"*2 + "Ok " + name + ", what would you like to quiz yourself on today?: \n1) Subtractions\n2) Exponentiations").strip().lower()

    if quiz_type == "1" or "subtractions" or "subtraction":
        f = 0
        
        quiz_number = input("How many questions would you like to answer? (1 or 2):  ")

        while quiz_number < 0:
            print("\nThat was not a valid number. Please enter a whole number (No decimals)")
            quiz_number = input("How many questions would you like to answer?: ")
        
        elementary_school_quiz(f, quiz_number)

    elif quiz_type == "2" or "exponentiations" or "exponentiation":
        f = 1
        
        quiz_number = input("How many questions would you like to answer?: ")

        while quiz_number < 0:
            print("\nThat was not a valid number. Please enter a whole number (No decimals)")
            quiz_number = input("How many questions would you like to answer?: ")
        
        elementary_school_quiz(f, quiz_number)

elif status=='2':

    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
 
else:
    # your code goes here
    pass

print("Good bye "+name+"!")
