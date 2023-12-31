# Family name: Kevin El-Saikali
# Student number: 300349663
# Course ITI 1120
# Assignment Number 2, Part 2
# Year 2023


def min_enclosing_rectangle(radius, x, y):
    '''
        (number, number, number) -> (number, number)
        \nPre Condition: radius, x and y must be numbers
        \nTakes 3 parameters, radius: the radius of a circle, x and y: the coordinates representing the center of the circle and returns the coordinates of the bottom left corner of the rectangle
    '''
    if radius < 0:
        return None
    
    else:
        return (x-radius, y-radius)

def vote_percentage(results:str):
    '''
        (str) -> number
        \nPre Condition: results must be a string containing all the cases of 'yes' 'no' and 'abstained'
        \nTakes a string 'results' containing votes "yes" "no" and "abstained" and parses through to return the percentage of votes equal to yes
    '''

    x = results.count("yes")
    y = results.count("yes") + results.count("no")

    return (x/y) 


def vote():
    '''
        (None) -> None
        \nPre Condition: votes must be a string containing all the cases of 'yes' 'no' and 'abstained'
        \nPasses a string of votes inputted by the user through the vote_percentage() function. It then returns the percentage of "yes"'s to determine the outcome of the vote
    '''
    votes = input("Enter the yes, no and abstained votes and then press [Enter]: ")

    x = vote_percentage(votes)

    if x == 1.0:
        print("proposal passes unanimously")

    elif (2/3) <= x < 1.0:
        print("proposal passes with super majority") 

    elif (1/2) <= x <(2/3):
        print("proposal passes with simple majority")
    
    else:
        print("proposal fails")




