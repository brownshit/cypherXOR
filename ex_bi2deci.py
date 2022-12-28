#이진수에서 십진수로의 변환하는....

def main():
    #message into decimal and also binary
    inputmessage = input("[input String what you want to convert] : ")
    inputmode = input("[mode input | d : decimal | b : binary ] : ")
    result =[]
    if inputmode == "d":
        result = StringIntoD(inputmessage)
    else:
        result = StringIntoB(StringIntoD(inputmessage))        
    print(result)

def StringIntoD(inputmessage):  #toDecimal
    toDecimalstr = []
    for i in range(len(inputmessage)):
        toDecimalstr.append(ord(inputmessage[i]))
    return toDecimalstr

def StringIntoB(inputmessage):      #list type.
    toBinarystr = []
    #print(type(inputmessage))
    for i in range(len(inputmessage)):
        
        tempval = inputmessage[i]
        #print(tempval)
        tempbuf =[]
        for i in range(7,0,-1):
            tempbuf.append(tempval//(2**i))
            tempval = tempval%(2**i)
        tempbuf.append(tempval)         #마지막으로 남은 값 대입시켜주기.
        #print(tempbuf)
        toBinarystr.append(tempbuf)
    return toBinarystr

#xor복호화도 진행해보자.    2진수로 바꿔주고 난 후에 모든 값에 대해서 xor 연산을 해주는 암호화 진행.. 동시에 복호화 코드도 짜보기.
