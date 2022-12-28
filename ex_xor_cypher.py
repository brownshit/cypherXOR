import os
import sys
#상위 path의 파일 끌어오기.
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pyforDeepLearning.ex25 import XOR
import ex_bi2deci as binary
def main():
    print("to cypher string, input what u want to convert...")
    inputStr = input(" : ")
    str = binary.StringIntoB(binary.StringIntoD(inputStr))
    #print(str)
    charvalue=[]
    value =[]
    cypherlistele = []
    for i in range(len(str)):
        lowervalue=[]
        
        #print(str[i])
        charstr = str[i]

        templistele =[charstr[0]]
        #print(charstr)

        for j in range(1,len(charstr)):
            templistele.append(XOR(charstr[j-1],charstr[j]))
        cypherlistele.append(templistele)
        tempstr = cypherlistele[i]
        #print(cypherlistele)

        #xor연산 후 7번째 자리수까지 
        totalval = 0
        for k in range(7,0,-1):
            lowervalue.append(tempstr[k]*2**(7-k))
            #print(len(lowervalue))
            totalval += lowervalue[7-k]
            #print(k)
        charvalue.append(chr(totalval))
        value.append(totalval)
    #print(charvalue)
    #print(value)
    print("".join(charvalue))
main()
