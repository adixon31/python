#Angel E. Dixon
#902749019
#Section A2
#adixon31@gatech.edu
#"I worked on the homework assignment alone, using only this semester's course materials."

from myro import *

def checkHeight(height):
    if height == 132:
        return "Have a great ride!"
    elif height > 132:
        return "Have a great ride!"
    else:
        return "Sorry. You must be at least 1 meter 32 cm to ride."
        
#checkHeight(125)

def countDownByThrees(start):  
    while start > 1:
        print start
        start = start - 3
    print "Blast off!"

#countDownByThrees(101)
    
def multiplicationTables(num,limit):
    counter = -1
    while counter < limit:
        counter = counter + 1
        product = num * counter
        print str(num) + " * " + str(counter) + " = " + str(product)

#multiplicationTables(3,10)

def comboLock(num1,num2,num3,num4,num5):
    quo = num1 % 2
    quo2 = num2 % 2
    quo3 = num3 % 2
    quo4 = num4 % 2
    quo5 = num5 % 2 
    if  quo == quo3 == quo5 == 1 and quo2 == quo4 == 0:
        return "You opened the lock."
    else:
        return "You are locked out."

#comboLock(3,8,3,6,7)

def complimentMaker(ans1,ans2,ans3,ans4):
    if ans1 == True:
        ans1 = "super "
    else:
        ans1 = ""
    if ans2 == True:
        ans2 = "nice "
    else:
        ans2 = ""
    if ans3 == True:
        ans3 = "smart "
    else:
        ans3 = ""
    if ans4 == True:
        ans4 = "cool "
    elif ans1 == ans2 == ans3 == ans4 == False:
        print "No comment."
    else:
        ans4 = ""
    string =  "You are " + "%s" % (ans1) + "%s" % (ans2) + "%s" % (ans3) + "%s" %(ans4) + "."
    return string

#complimentMaker(False,True,False,True)


def xmassTree(x):
    counter = -1
    num=x/2
    while counter < x:
        counter = counter +2
        level = "*" * counter
        space = " " * num
        print space + level
        num = num-1
    print " " * (x/2) + "*" 
    print " " * (x/2) + "*"
    print " " * (x/2) + "*"

#xmassTree(27)

def badRecord(sen):
    result = str()
    for letter in sen:
        if letter in string.uppercase:
             result = result + letter
    return result
        

#badRecord("Hello, how Are You?")

def printTimestable():
    x = 1
    print "Times:", "\t", x, "\t", x+1, "\t", x+2, "\t", x + 3, "\t", x + 4, "\t", x + 5, "\t", x+6, "\t", x +7, "\t", x + 8
    while x < 10:
        print x, "\t", x, "\t", 2*x, "\t", 3*x, "\t", 4* x, "\t", 5*x, "\t", 6* x, "\t", 7*x, "\t", 8* x, "\t", 9*x
        x +=1

#printTimestable()

def printTimes(n):
    x = 1 
    while x<= n:
        y = 1
        while y <= n:
            print x * y, "\t",
            y += 1
        print "\t"
        x += 1
      
#printTimes(8)