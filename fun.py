def getInput():
    msg =input("enter txt to calc:-")
    return msg

def checkInt(msg):
    intList =["0","1","2","3","4","5","6","7","8","9"]
    simList =['+','-','/','*']
    firstNum =''
    sim = 0
    sNumLen = 0
    secondNum = ''
    for num in range(0,len(msg)):
        if (msg[num] in intList):
            firstNum +=msg[num]
        else:
            if(msg[num] in simList):
                sim = msg[num]
                sNumLen = num
                break

    for num in range(sNumLen,len(msg)):
        if(msg[num ] in intList):
            secondNum += msg[num]
    
    return firstNum,secondNum,sim


def calcNum(fNum,sNum,sim):
    ifNum = int(fNum)
    isNum = int(sNum)
    if sim == '+':
        tNum= ifNum + isNum
    elif sim == '-':
        tNum= ifNum - isNum
    elif sim =='/':
        tNum =ifNum / isNum
    else:
        tNum = ifNum * isNum
    
    return tNum