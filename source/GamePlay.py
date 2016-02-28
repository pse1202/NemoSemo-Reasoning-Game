"""

    copyright (c) 2016. 01. 15 , jaemin.lee.email@gmail.com
    
"""
import socket
#import thread
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
        if DepartureNum == 1:
            x = 0
            y = 1
            direct = 'd'    
        elif DepartureNum == 2:
            x = 0
            y = 2
            direct = 'd' 
        elif DepartureNum == 3:
            x = 0
            y = 3
            direct = 'd' 
        elif DepartureNum == 4:
            x = 0
            y = 4
            direct = 'd' 
        elif DepartureNum == 5:
            x = 0
            y = 5
            direct = 'd' 
        elif DepartureNum == 6:
            x = 1
            y = 6
            direct = 'l' 
        elif DepartureNum == 7:
            x = 2
            y = 6
            direct = 'l'
        elif DepartureNum == 8:
            x = 3
            y = 6
            direct = 'l'
        elif DepartureNum == 9:
            x = 4
            y = 6
            direct = 'l'
        elif DepartureNum == 10:
            x = 5
            y = 6
            direct = 'l'
        elif DepartureNum == 11:
            x = 6
            y = 5
            direct = 'u'
        elif DepartureNum == 12:
            x = 6
            y = 4
            direct = 'u'
        elif DepartureNum == 13:
            x = 6
            y = 3
            direct = 'u'
        elif DepartureNum == 14:
            x = 6
            y = 2
            direct = 'u'
        elif DepartureNum == 15:
            x = 6
            y = 1
            direct = 'u'
        elif DepartureNum == 16:
            x = 5
            y = 0
            direct = 'r'
        elif DepartureNum == 17:
            x = 4
            y = 0
            direct = 'r'
        elif DepartureNum == 18:
            x = 3
            y = 0
            direct = 'r'
        elif DepartureNum == 19:
            x = 2
            y = 0
            direct = 'r'
        elif DepartureNum == 20:
            x = 1
            y = 0
            direct = 'r'
        while True:
            if direct == 'd':
                if Matrix[x][y] == 0:
                    x = x + 1
                elif Matrix[x][y] == 1:
                    y = y - 1
                    n = n + 1
                    direct = 'l'
                elif Matrix[x][y] == 2:
                    y = y + 1
                    n = n + 1
                    direct = 'r'
                    
            elif direct == 'u':
                if Matrix[x][y] == 0:
                    x = x - 1
                elif Matrix[x][y] == 1:
                    y = y + 1
                    n = n + 1
                    direct = 'r'
                elif Matrix[x][y] == 2:
                    y = y - 1
                    n = n + 1
                    direct = 'l'
                    
            elif direct == 'l':
                if Matrix[x][y] == 0:
                    y = y - 1
                elif Matrix[x][y] == 1:
                    x = x + 1
                    n = n + 1
                    direct = 'd'
                elif Matrix[x][y] == 2:
                    x = x - 1
                    n = n + 1
                    direct = 'u'
                    
            elif direct == 'r':
                if Matrix[x][y] == 0:
                    y = y + 1
                elif Matrix[x][y] == 1:
                    x = x - 1
                    n = n + 1
                    direct = 'u'
                elif Matrix[x][y] == 2:
                    x = x + 1
                    n = n + 1
                    direct = 'd'

            
                
            if x == 0 and y == 1:
                result = 1
                break
            elif x == 0 and y == 2:
                result = 2
                break
            elif x == 0 and y == 3:
                result = 3
                break
            elif x == 0 and y == 4:
                result = 4
                break
            elif x == 0 and y == 5:
                result = 5
                break
            elif x == 1 and y == 6:
                result = 6
                break
            elif x == 2 and y == 6:
                result = 7
                break
            elif x == 3 and y == 6:
                result = 8
                break
            elif x == 4 and y == 6:
                result = 9
                break
            elif x == 5 and y == 6:
                result = 10
                break
            elif x == 6 and y == 5:
                result = 11
                break
            elif x == 6 and y == 4:
                result = 12
                break
            elif x == 6 and y == 3:
                result = 13
                break
            elif x == 6 and y == 2:
                result = 14
                break
            elif x == 6 and y == 1:
                result = 15
                break
            elif x == 5 and y == 0:
                result = 16
                break
            elif x == 4 and y == 0:
                result = 17
                break
            elif x == 3 and y == 0:
                result = 18
                break
            elif x == 2 and y == 0:
                result = 19
                break
            elif x == 1 and y == 0:
                result = 20
                break
        return [result,n]

    def NewGame(self):
        print "NewGame : Service"
        print "NewGame : Create Random Graph and user Table"
        self.MakeGraph()
        print "NewGame : Show Manual"
        print "1. Find Combination -> Command \"FindCombination(DepartureNum)\""
        print "2. Check Graph -> Command \"CheckGraph()\""
