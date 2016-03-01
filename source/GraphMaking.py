"""

    copyright (c) 2016. 01. 15 , jaemin.lee.email@gmail.com
    
"""

from Debug import * # debug Mode
from random import randrange as rr, shuffle

class GraphMaking(DebugMatrix):
    def MakeGraph(self, RandomGraph = True,UserTable = True):
        if RandomGraph:
            self.Random_Matrix = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]
                ]
            for _ in range(2):
		dir = [0,1]
		dir.shuffle()
                while True:
                    x = rr(1,5)
                    y = rr(1,5)
                    if self.Random_Matrix[x][y] == self.Random_Matrix[x+dir[0]][y+dir[1]] == 0:
                        break
                self.Random_Matrix[x][y] = rr(1,3)
                if self.Random_Matrix[x][y] == 1:
                    self.Random_Matrix[x+dir[0]][y+dir[1]] = 2
                else:
                    self.Random_Matrix[x+dir[0]][y+dir[1]] = 1

            for _ in range(2):
                while True:
                    x = rr(1,5)
                    y = rr(1,5)
                    if self.Random_Matrix[x][y] == self.Random_Matrix[x][y+1] == \
		    self.Random_Matrix[x+1][y] == self.Random_Matrix[x+1][y+1] == 0:
                        break
                self.Random_Matrix[x][y] = self.Random_Matrix[x+1][y+1] = 1
                self.Random_Matrix[x][y+1] = self.Random_Matrix[x+1][y] = 2


       
        self.User_Matrix=[
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0]
            ]

        # if UserTable == True Make User_Table END-------------------
    def RemoveGraph(self, RandomGraph = True,UserGraph = True):
        # if RandomGraph == True: User Graph - > User Table----------
        if RandomGraph:
            self.Random_Matrix=[
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]
                ]
        # if RandomGraph == True: User Graph - > User Table END------
        
        # if UserGraph != True: Ranbon Graph - > Random Table--------
        if UserGraph:
            self.User_Matrix = [
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0]
                ]
        # if Usergraph != True: Ranbon Graph - > Random Table END----
