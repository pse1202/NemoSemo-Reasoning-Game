"""

    copyright (c) 2016. 01. 15 , jaemin.lee.email@gmail.com
    
"""

from Debug import * # debug Mode
import random

class GraphMaking(DebugMatrix):
    def MakeGraph(self, RandomGraph = True,UserTable = True):
        # if RandomGraph == True Make Random Graph-------------------
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
            for i in range(2):
                if(random.randrange(0,2) == 1):
                    while True:
                        x = random.randrange(1,5)
                        y = random.randrange(1,5)
                        if self.Random_Matrix[x][y] == 0 and self.Random_Matrix[x][y+1] == 0:
                            break
                    self.Random_Matrix[x][y] = random.randrange(1,3)
                    if self.Random_Matrix[x][y] == 1:
                        self.Random_Matrix[x][y+1] = 2
                    else:
                        self.Random_Matrix[x][y+1] = 1
                else:
                    while True:
                        x = random.randrange(1,5)
                        y = random.randrange(1,5)
                        if self.Random_Matrix[x][y] == 0 and self.Random_Matrix[x+1][y] == 0:
                            break
                    self.Random_Matrix[x][y] = random.randrange(1,3)
                    if self.Random_Matrix[x][y] == 1:
                        self.Random_Matrix[x+1][y] = 2
                    else:
                        self.Random_Matrix[x+1][y] = 1
            for i in range(2):
                while True:
                    x = random.randrange(1,5)
                    y = random.randrange(1,5)
                    if self.Random_Matrix[x][y] == 0 and self.Random_Matrix[x][y+1] == 0 and self.Random_Matrix[x+1][y] == 0 and self.Random_Matrix[x+1][y+1] == 0:
                        break
                self.Random_Matrix[x][y] = 1
                self.Random_Matrix[x][y+1] = 2
                self.Random_Matrix[x+1][y] = 2
                self.Random_Matrix[x+1][y+1] = 1
        # if RandomGraph == True Make Random Graph END---------------

        # if UserTable == True Make User_Table-----------------------
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
