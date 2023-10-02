import math
import random

def program_welcome():
    '''
        (None) -> (None)
        \nPrints a formatted welcome message to the screen
    '''
    print("********************************************")
    print("*                                          *")
    print("*  ___Welcome to my math quiz generator__  *")
    print("*                                          *")
    print("********************************************")


def elementary_welcome():
    '''
        (None) -> (None)
        \nPrints a welcome message for elementary students if status is elementary and formats it to the length of the entered name
    '''

    message = "*  __" + name + ", welcome to my quiz-generator for elementary school students.__  *"
    #Calculates the length of the string including the name given by user
    x = len(message)

    #Prints the correct amount of stars and spaces to enclose the name in a rectangle
    print("*" * (x))
    print("*" + " "* (x-2) + "*")
    print("*  __" + name + ", welcome to my quiz-generator for elementary school students.__  *")
    print("*" + " "* (x-2) + "*")
    print("*" * (x))


def high_school_welcome():
    '''
        (None) -> (None)
        \nPrints a welcome message for high school students if status is high school and formats it to the length of the entered name
    '''

    message = "*   __quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "__   *"
    #Calculates the length of the string including the name given by user
    x = len(message)

    #Prints the correct amount of stars and spaces to enclose the name in a rectangle
    print("*" * (x))
    print("*" + " "* (x-2) + "*")
    print("*   __quadratic equation, a·x^2 + b·x + c= 0, solver for " + name + "__   *")
    print("*" + " "*(x-2) + "*")
    print("*" * (x))


def end_messages(p, total):
    '''
        (int, int) -> str
        Pre Conditions: p and total must be numbers
        \nReturns the correct message based on the amount of points recieved
    '''
    #Checks if the amount of points recieved are equal to the amount of questions asked, half or none
    if (p == 1 and total == 1) or (p == 2 and total == 2):
        return("\nVery good job "+ name + "! You're sure to get an A tomorrow!")
    
    elif (p == 1 and total == 2):
        return("\nYou did ok " + name + ", but I know you can do better.")
    
    else:
        return("\nI think you need some more practice " + name +".")


def elementary_school_quiz(flag:int, n:int):
    '''
        (int, int) -> int
        \nPre Conditions: 'flag' must have a value of 0 or 1 and 'n' must have a value of 1 or 2
        \nGiven the type of problems 'flag', the function will ask to solve 'n' problems with either subtraction or exponentiation
    '''

    #Initialize the score
    score = 0

    #Generate random numbers to be used in the first set of questions
    a = random.randint(0, 9)
    b = random.randint(0, 9)

    #If subtractions was chosen...
    if flag == 0:

        #If only 1 question...
        if n == 1:
            answer = input("\nQuestion 1:\nWhat is the result of " + str(a) + " - " + str(b) + "?\nYour answer: ")

            #If the answer is equal to what Python calculated, a point is added to the score
            if answer == str(a-b):
                score += 1

        #If 2 questions...
        elif n == 2:
            answer = input("\nQuestion 1:\nWhat is the result of " + str(a) + " - " + str(b) + "?\nYour answer: ")
            if answer == str(a-b):
                score += 1
            
            #Refresh the numbers for the second question
            a = random.randint(0, 9)
            b = random.randint(0, 9)

            answer = input("\n\nQuestion 2:\nWhat is the result of " + str(a) + " - " + str(b) + "?\nYour answer: ")
            if answer == str(a-b):
                score += 1
        
        #User chose 0 questions
        else:
            print("Zero questions. OK. Good bye")
    
   #If exponents was chosen...
    elif flag == 1:

        #If only one question
        if n == 1:
            answer = input("\nQuestion 1:\nWhat is the result of " + str(a) + " ^ " + str(b) + "?\nYour answer: ")
            
            if answer == str(a**b):
                score += 1
        
        #If two questions
        elif n == 2:
            answer = input("\nQuestion 1:\nWhat is the result of " + str(a) + " ^ " + str(b) + "?\nYour answer: ")
            
            #If the answer given is equal to what Python calculated, a point is added to score
            if answer == str(a**b):
                score += 1

            #Refresh the numbers for the second question
            a = random.randint(0, 9)
            b = random.randint(0, 9)

            answer = input("\nQuestion 2:\n\nWhat is the result of " + str(a) + " ^ " + str(b) + "?\nYour answer: ")
            if answer == str(a**b):
                score += 1

        else:
            print("Zero questions. OK. Good bye")

    #Return the score value to main to be used in the final part
    return score


def high_school_quiz(a,b,c):
    '''
        (number, number, number) -> None
        Pre Condition: a, b and c must be real numbers
        Takes 3 given numbers a, b and c and solves the quadratic equation for 0 = ax^2 + bx + c. It then prints out the possible roots to satisfy x, or tells the user there are none if impossible
    '''
    
    #If the equation is linear, solve by isolating x
    if int(a) == 0:

        if a ==0 and b != 0 and c != 0:
            print("The linear equation: " + str(b) + "·x + " + str(c) + " = 0")
            print("Has the following root/solution: " + str((0-(c))/b))

        #Because 0 = 0, it is satisfied for all numbers x
        elif (a == b == c == 0):
            print("Is satisfied for all numbers x")
        
        elif a == 0 and b == 0 and c != 0:
            print("Is satisfied for no numbers x")

    #If the equation is polynomial/quadratic, solve with the quadratic equation
    else:
        print("The quadratic equation: " + str(a) + "x^2 + " + str(b) + "·x + " + str(c) + " = 0 ")
        root_inner = ((b)**2 - 4*a*c)

        #Check if the square root is an imaginary number
        if root_inner < 0:
            #If yes, print i +/- (|sqrt|/2a)
            root_1 = str((-b)/(2*a)) + " + i " + str(math.sqrt(abs((b)**2 - 4*a*c))/(2*a))
            root_2 = str((-b)/(2*a))  + " - i " + str(math.sqrt(abs((b)**2 - 4*a*c))/(2*a))

            print("Has the following complex roots:")
            print(str(root_1) + " and " + str(root_2))
        
        #If it is not an imaginary number...
        else:
            root_1 = ((-b) + math.sqrt((b)**2 - 4*a*c))/(2*a)
            root_2 = ((-b) - math.sqrt((b)**2 - 4*a*c))/(2*a)

            #If + and - give the same root, there is only one possible solution
            if root_1 == root_2:
                print("Has only one solution, a real root: ")
                print(str(root_1))

            #If numerator is = 0, then 0 = 0
            elif b == c == 0:
                print("Is satisfied for all numbers x")

            #If there are no special cases
            else:
                print("Has the following real roots:")
                print(str(root_1) + " and " + str(root_2))
    
# main

# Calls welcome message function
program_welcome()

name=input("What is your name? ")

status=input("Hi " + name + ". Are you in? Enter \n1 for elementary school\n2 for high school or\n3 or other character(s) for none of the above?\n")

# If elementary selected
if status=='1':
    # Welcome message for elementary students
    elementary_welcome()
    quiz_type = int(input("\n"*2 + name + ", what would you like to practice? Enter \n0 for Subtraction\n1 for Exponentiation \nYour choice: ").strip().lower())

    #Check if subtractions was selected as an option
    if quiz_type == 0:
         
        #Get the amount of questions to ask: either 0, 1 or 2
        quiz_number = int(input("\n\nHow many practice questions would you like to do? (0, 1 or 2): ").strip())
        if (0 <= quiz_number <= 2):

            #Use the users inputted values to get the desired type and amount of questions from the function
            points = elementary_school_quiz(int(quiz_type), quiz_number) #calls the quiz function
            
            #Sets the total possible amount of points to the number of questions being asked
            tot = quiz_number

            #Only if a question was actually asked tally the points
            if quiz_number == 1 or quiz_number == 2:
                #Call the end messages function to return the appropriate message
                print(end_messages(points, tot))
        
        #If the user didn't input 0 or 1
        else:
            print("Only 0, 1 and 2 are valid choices for the number of questions.")
    
        
    #Check if exponentiation was chosen if not subtraction
    #Same concept as if quiz_type == 0
    elif quiz_type == 1:
        
        quiz_number = int(input("\n\nHow many practice questions would you like to do? (0, 1 or 2): ").strip())
        if (0 <= quiz_number <= 2):
            points = elementary_school_quiz(int(quiz_type), quiz_number)
            tot = quiz_number

            if quiz_number == 1 or quiz_number == 2:
                print(points)
                print(end_messages(points, tot))
        
        else:
            print("Only 0, 1 and 2 are valid choices for the number of questions.")

    #If the user didn't input 0 or 1
    else:
        print("Invalid choice, only 0 or 1 is accepted")
    

#Check if the user selected that they are in high school if not elementary
elif status=='2':

    # Call function containing welcome message
    high_school_welcome()

    flag=True
    while flag:

        #Handle various inputs of 'yes' by using string methods strip() to remove spaces and lower() to make all letters lowercase
        question=input(name+", would you like a quadratic equation solved? ").strip().lower()

        # your code to handle various form of "yes" goes here

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            
            #Get the values needed to fill the equation ax^2 + bx + c
            a = float(input("\nEnter a number for the coefficient a: "))
            b = float(input("\nEnter a number for the coefficient b: "))
            c = float(input("\nEnter a number for the coefficient c: "))

            #Call the function to treat the data given
            high_school_quiz(a, b, c)
        

 
else:
    # your code goes here
    #Simply print that this program is not made for them if not in elementary or high school
    print(name + ", you are not the target audience for this software...")

#Say goodbye ot the user
print("Good bye "+name+"!")

#End program
