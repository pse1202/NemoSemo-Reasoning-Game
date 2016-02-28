## This Module is debug module
class DebugMatrix:
    def show(self, RandomGraph = True, UserGraph = True):
        if RandomGraph:
            try:
                self.Random_Matrix
            except:
                print "NOT FOUND MATRIX"
            else:
                print "Random Matrix"
                for i in range(7):
                    print self.Random_Matrix[i]
                    if i == 6:
                        print " "
        if UserGraph:
            try:
                self.User_Matrix
            except:
                print "NOT FOUND MATRIX"
            else:
                print "User Matrix"
                for i in range(7):
                    print self.User_Matrix[i]
                    if i == 6:
                        print " "
