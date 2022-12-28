import numpy as np

class GATES:
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2

    def AND(self):
        x = np.array([self.x1, self.x2])
        w = np.array([0.5, 0.5])        #가중치
        b = -0.7
        tmp = np.sum(w*x)+b
        if tmp>=0:
            return 1
        elif tmp<0:
            return 0

    def NAND(self):       #NAND는 00을 제외하고 모두 0
        x = np.array([self.x1, self.x2])
        w = np.array([-0.5, -0.5])        #가중치
        b = 0.7
        tmp = np.sum(w*x)+b
        if tmp>=0:
            return 1
        elif tmp<0:
            return 0

    def OR(self):
        x = np.array([self.x1, self.x2])
        w = np.array([0.5, 0.5])        #가중치
        b = -0.2
        tmp = np.sum(w*x)+b
        if tmp>=0:
            return 1
        elif tmp<0:
            return 0

testg = GATES(0,1)
#print(testg.AND())
#print(testg.OR())