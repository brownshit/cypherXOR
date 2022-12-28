from pyforDeepLearning.ex24 import GATES

#2개 퍼셉트론 층으로 xor만들기

def XOR(x1, x2):
    myg = GATES(x1,x2)
    p = myg.NAND()
    q = myg.OR()
    finalG = GATES(p,q)
    return finalG.AND()

def main():
    print(XOR(0,0))
    print(XOR(0,1))
    print(XOR(1,0))
    print(XOR(1,1))

    return 0

#main()