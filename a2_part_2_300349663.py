def min_enclosing_rectangle(radius, x, y):
    if radius < 0:
        return None
    
    else:
        return (x-radius, y-radius)

def vote_percentage(results):

    x = results.count("yes")
    y = results.count("yes") + results.count("no")

    return (x/y) 


def vote():
    votes = input("Enter the yes, no and abstained votes and then press [Enter]: ")

    x = vote_percentage(votes)

    if x == 1.0:
        print("proposal passes unanimously")

    elif round(x, 3) == 0.67:
        print("proposal passes with super majority") 

    elif x == 0.5:
        print("proposal passes with simple majority")
    
    else:
        print("proposal fails")



