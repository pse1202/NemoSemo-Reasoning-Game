"""

    copyright (c) 2016. 01. 15 , jaemin.lee.email@gmail.com
    
"""
from GraphMaking import *
class GamePlay(GraphMaking): # Inheritance 
    def CheckGraph(self,UserMatrix = None,CompareMatrix = None):
    # Comparing UserMatrix and CompareMatrix
    # default UserMatrix is self.User_Matrix
    # default CompareMatrix is self.Random_Matrix
    # If CompareMatrix and UserMatrix are equal, returns True NOT False
        if UserMatrix == None:
            UserMatrix = self.User_Matrix
        if CompareMatrix == None:
            CompareMatrix = self.Random_Matrix
        if UserMatrix == CompareMatrix:
            return True
        else:
            return False

    def FindCombination(self,DepartureNum,Matrix = None):
    # FindCombination(DepartureNum,Matrix)[0] return Datination Number
    # FindCombination(DepartureNum,Matrix)[1] return Reflection Number
    # default Matrix is self.Matrix
        if Matrix == None:
            Matrix = self.Random_Matrix
        n = 0

        xlist = [0]*5 + range(1,6) + [6]*6 + range(1,6)[::-1]
        ylist = xlist[5:] + xlist[:5]
        xylist = zip(xlist,ylist)

        direct = [[1,0],[0,-1],[-1,0],[0,1]][(DepartureNum - 1)/5]
        x = xlist[DepartureNum - 1]
        y = ylist[DepartureNum - 1]

        while True:
            curr = Matrix[x][y]
            if curr == 0:
                x += direct[0]
            else:
                n += 1
                a,b = direct
                if curr == 2:
                    direct = b, a
                else:
                    direct = -b, -a
            if xylist.count((x,y)):
                result = xylist.index((x,y))
                break

        return [result,n]

    def NewGame(self):
        print "NewGame : Service"
        print "NewGame : Create Random Graph and user Table"
        self.MakeGraph()
        print "NewGame : Show Manual"
        print "1. Find Combination -> Command \"FindCombination(DepartureNum)\""
        print "2. Check Graph -> Command \"CheckGraph()\""

