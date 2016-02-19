#Angel E. Dixon
#902749019
#adixon31@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials."

# This program is called "Secret Santa". The users enter the names of the people playing Secret Santa. Everyone then (secretly) draws a name from the program by entering a number. There are no parameters for this function.


from myro import *

def secretSanta():
    print "Playing Secret Santa? How exciting!"
    b = raw_input("Enter only the names of everyone taking part in Secret Santa(example: Adam Eve Carl ...)?: ")
    print " "
    b = str(b)
    secretlist = string.split(b)
    number = len(secretlist)
    while number > 0:
        c = raw_input("Pick a number from one to the number of people to choose from: ")
        print " "
        c = int(c)
        try:
            if c < 1:
                print "I'm sorry, that is less than 1. Try again."
            if c > number:
                print "I'm sorry, try a smaller number"
                print " "
            if c <= number:
                try:
                    d = c-1
                    name = secretlist[d]
                    print "You picked %s! " % str(name)
                    print " "
                    #The program wants to make sure that the user did not pick theirself.
                    e = raw_input("Is this you? (enter y or n): ")
                    print " "
                    e = str(e)
                    if e == "n":
                        del secretlist[d]
                        number -= 1
                    if  e!= "y" and e!= "n":
                        print "That didn't answer the question correctly. Just take another turn."
                        print " "
                    if e == "y":
                        print "You picked yourself! Try again."
                        print " "
                        
                except:
                    print "Sorry, try a smaller number."
                    print " "
                
        except:
            print "I'm sorry, that is not an integer. Please try again."
            
    print "Everyone has a name! Now hurry to find the perfect gifts!
    print "Merry Christmas and happy holidays!!!"

secretSanta()