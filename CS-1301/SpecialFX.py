#Angel Dixon
#902862704 and 902749019
#We worked on this assignment alone using only the assigned course material and TAs.

from myro import *
init()

def seeingRed():
    aList = []
    pic = takePicture()
    aList.append(pic)
    
    pic1 = copyPicture(pic)
    for pix in getPixels(pic1):
        setRed(pix, 255)
    aList.append(pic1)
    aList.append(pic)
    for index in aList:
        show(index)
        wait(.3)

#seeingRed(15)
    
def seeingRainbow():
    aList = []
    pic = takePicture()
    aList.append(pic)

    pic1 = copyPicture(pic)
    for pix in getPixels(pic1):
        setRed(pix,225)
    aList.append(pic1)

    pic2 = copyPicture(pic1)
    for pix in getPixels(pic2):
        setGreen(pix,255)   
    aList.append(pic2)

    pic3 = copyPicture(pic)
    for pix in getPixels(pic3):
        setGreen(pix,255)     
    aList.append(pic3)

    pic4 = copyPicture(pic3)
    for pix in getPixels(pic4):
        setBlue(pix,255)
    aList.append(pic4)

    pic5 = copyPicture(pic1)
    for pix in getPixels(pic5):
        setBlue(pix,255)
    aList.append(pic5)
    aList.append(pic)
    
    for index in aList:
        show(index)
        wait(.1)
    
#seeingRainbow(?)
            
def robotZoom():
    aList = []
    counter = 0
    while counter < 10:
        pic = takePicture()
        aList.append(pic)
        forward(.2,.2)
        counter += 1
    for index in aList:
	show(index)
	wait(.3)

#robotZoom(15)
    
def viewOf360():
    aList = []
    counter = 0
    while counter < 15:
        pic = takePicture()
        aList.append(pic)
        turnRight(.2,.2)
        counter +=1
    for index in aList:
        show(index)
        wait(.2)
                    

#viewOf360(15)
    

def dollyShot():
    aList = []
    x = 0
    while x < 15:
        p = takePicture()
        aList.append(p)
        turnRight(.4,.5)
        forward(.5,.5)
        turnLeft(.4,.5)
        x = x + 1
    for index in aList:
        show(index)
        wait(.3)

#dollyShot(20)
        
def fadeToBlack():
    aList = []
    pic = takePicture()
    savePicture(pic, "pic00.gif")
    aList.append(pic)
    
    pic1 = copyPicture(pic)
    for pix in getPixels(pic1):
       makeDarker(pix)
    savePicture(pic1, "pic01.gif")
    aList.append(pic1)

    pic2 = copyPicture(pic1)
    for pix in getPixels(pic2):
       makeDarker(pix)
    savePicture(pic2, "pic02.gif")
    aList.append(pic2)
    
    pic3 = copyPicture(pic2)
    for pix in getPixels(pic3):
        makeDarker(pix)
    savePicture(pic3, "pic03.gif")
    aList.append(pic3)

    pic4 = copyPicture(pic3)
    for pix in getPixels(pic4):
        makeDarker(pix)    
    savePicture(pic4, "pic04.gif")
    aList.append(pic4)

    pic5 = copyPicture(pic4)
    for pix in getPixels(pic5):
        makeDarker(pix)    
    savePicture(pic5, "pic05.gif")
    aList.append(pic5)

    pic6 = copyPicture(pic5)
    for pix in getPixels(pic6):
        makeDarker(pix)    
    savePicture(pic6, "pic06.gif")
    aList.append(pic6)

    pic7 = copyPicture(pic6)
    for pix in getPixels(pic7):
        makeDarker(pix)    
    savePicture(pic7, "pic07.gif")
    aList.append(pic7)
    

    pic8 = copyPicture(pic7)
    for pix in getPixels(pic8):
        makeDarker(pix)    
    savePicture(pic8, "pic08.gif")
    aList.append(pic8)

    pic9 = copyPicture(pic8)
    for pix in getPixels(pic9):
        setRed(pix, 0)
        setBlue(pix, 0)
        setGreen(pix, 0)
    savePicture(pic9, "pic09.gif")
    aList.append(pic9)
    for index in aList:
	show(index)
	wait(.3)
   
    

#fadeToBlack(35)

def screenShake():
    aList = []
    p = takePicture()
    aList.append(p)
    turnLeft(.25, .1)
    p1 = takePicture()
    aList.append(p1)
    turnRight(.25, .1)
    p2 = takePicture()
    aList.append(p2)
    turnRight(.25, .1)
    p3 = takePicture()
    aList.append(p3)
    turnLeft(.25, .1)
    p4 = takePicture()
    aList.append(p4)
    newList = aList * 5
    for index in newList:
        show(index)
        wait(.2)
    
#screenShake(45)
        
def tempoChange(temp):
    aList = []
    aList1 = []
    counter = 0
    temp = int(temp)
    while counter < 9:
        counter2 = 1
        pic = takePicture()
        aList1.append(pic)
        forward(.2,.2)
        while counter2 <= temp:
            aList.append(pic)
            counter2 += 1
        counter += 1
    for index in aList1:
        show(index)
        wait(.3)
    for index in aList:
        show(index)
        wait(.2)
            
#tempo(20)