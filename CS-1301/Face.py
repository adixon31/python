#Angel E. Dixon
#Section: A2
#adixon31@gatech.edu
#902749019
#"I worked on the homework assignment alone, using only this semester's course materials." 


from myro import *

win = GraphWin ("Buddy", 400, 400)
p1 = Point(280,80)
p2 = Point(120,300)
myOval1 = Oval(p1,p2)
myOval1.draw(win)
sienna = color_rgb(160,82,45)
myOval1.setFill(sienna)
p3 = Point(180,120)
p4 = Point(160,160)
myOval2 = Oval(p3,p4)
myOval2.draw(win)
p5 = Point(240,120)
p6 = Point(220,160)
myOval3 = Oval(p6,p5)
myOval3.draw(win)
white = color_rgb(255,255,255)
myOval2.setFill(white)
myOval3.setFill(white)
p7 = Point(200,160)
p8 = Point(180,200)
myLine1 = Line(p7,p8)
myLine1.draw(win)
p9 = Point(200,210)
myLine2 = Line(p8,p9)
myLine2.draw(win)
p10 = Point(200,250)
p11 = Point(215,258)
p12 = Point(228,263)
p13 = Point(234,260)
p14 = Point(250,220)
myPolygon1 = Polygon(p10,p11,p12,p13,p14)
myPolygon1.draw(win)
myPolygon1.setFill(white)
p15 = Point(212,256)
p16 = Point(242,239)
myLine3 = Line(p15,p16)
myLine3.draw(win)
p17 = Point(167,137)
p18 = Point(174,150)
myOval4 = Oval(p17,p18)
myOval4.draw(win)
p19 = Point(225,137)
p20 = Point(233,150)
myOval5 = Oval(p19,p20)
myOval5.draw(win)
forest = color_rgb(34,139,34)
myOval4.setFill(forest)
myOval5.setFill(forest)
p21 = Point(237,200)
p22 = Point(242,165)
myRectangle1 = Rectangle(p21,p22)
myRectangle1.draw(win)
p23 = Point(230,175)
p24 = Point(250,170)
myRectangle2 =Rectangle(p23,p24)
myRectangle2.draw(win)
gray = color_rgb(64,64,64)
myRectangle1.setFill(gray)
myRectangle2.setFill(gray)