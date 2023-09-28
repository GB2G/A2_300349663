import math
import random

def program_welcome():
    print("********************************************************************************")
    print("*                                                                              *")
    print("* ______________________Welcome to my quiz generator!_________________________ *")
    print("*                                                                              *")
    print("********************************************************************************")

def elementary_welcome():
    print("********************************************************************************")
    print("*                                                                              *")
    print("* Hi " + name + ", welcome to my quiz generator for elementary school students *")
    print("*                                                                              *")
    print("********************************************************************************")

def high_school_welcome():
    print("********************************************************************************")
    print("*                                                                              *")
    print("*    Hi " + name + ", welcome to my quiz generator for high school students    *")
    print("*                                                                              *")
    print("********************************************************************************")


def end_messages(p, total):
    if (p == 1 and total == 1) or (p == 2 and total == 2):
        return("\nVery good job "+ name + "! You're sure to get an A tomorrow!")
    
    elif (p == 1 and total == 2):
        return("\nYou did ok " + name + ", but I know you can do better.")
    
    else:
        return("\nYou need a lot more practice " + name +".")



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
            answer = input("\nOk, here is your question:\nWhat is the result of the following equation: " + str(a) + " - " + str(b) + "?\nYour answer: ")
            
            if answer == str(a-b):
                score += 1

        
        elif n == 2:
            answer = input("\nOk, here is your first question:\nWhat is the result of the following equation: " + str(a) + " - " + str(b) + "?\nYour answer: ")
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
        print("********************************************************************************************************************************")
        print("*   For these questions, the exponent symbol will be represented with \'**\'. For example: 4**2 would be 4 to the power of 2   *")
        print("********************************************************************************************************************************")
        if n == 1:
            answer = input("\nOk, here is your question:\nWhat is the result of the following equation: " + str(a) + " ** " + str(b) + "?\nYour answer: ")
            
            if answer == str(a**b):
                score += 1
        
        elif n == 2:
            answer = input("\nOk, here is your first question:\nWhat is the result of the following equation: " + str(a) + " ** " + str(b) + "?\nYour answer: ")
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
program_welcome()

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

if status=='1':
    # your code goes here
    elementary_welcome()
    quiz_type = int(input("\n"*2 + "Ok " + name + ", what would you like to quiz yourself on today?: \n0) Subtractions\n1) Exponentiations \nYour answer: ").strip().lower())

    if quiz_type == 0 or 'subtractions' or 'subtraction' :
        
        quiz_number = int(input("\n\nHow many questions would you like to answer? (1 or 2): ").strip())
        tot = quiz_number
        
        points = elementary_school_quiz(int(quiz_type), quiz_number)
        print(points)
        print(end_messages(points, tot))
        
        

    elif quiz_type == 1 or 'exponentiations' or 'exponentiations':
        
        quiz_number = int(input("How many questions would you like to answer? (1 or 2): ").strip())
        tot = quiz_number

        points = elementary_school_quiz(int(quiz_type), quiz_number)
        print(points)
        print(end_messages(points, tot))
    

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
    print("Ah")
    print(name + ", you are not the target audience for this software...")

print("Good bye "+name+"!")
