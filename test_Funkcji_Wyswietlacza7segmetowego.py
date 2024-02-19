def FA(x3, x2, x1, x0):
    return (x1 and not x3) or (not x0 and x3) or (not x0 and not x2) or (x1 and x2) or (x0 and x2 and not x3) or (not x1 and not x2 and x3)
'''
def FB(x3, x2, x1, x0):#long
    return (not x0 and not x2) or (not x2 and not x3) or (x0 and not x1 and x3) or (not x0 and not x1 and not x3) or (x0 and x1 and not x3)
'''
def FB(x3, x2, x1, x0):#short
    return (not x0 and not x2) or (not x2 and not x3) or (x0 and not x1 and x3) or (not x3 and ((not x0 and not x1) or (x0 and x1)))

def FC(x3, x2, x1, x0):
    return (x0 and not x1) or (not x2 and x3) or (not x3 and (x0 or not x1 or x2))

def FD(x3, x2, x1, x0):
    return (not x1 and x3) or (x2 and ((x0 and not x1) or(not x0 and x1))) or (not x2 and ((x0 and x1) or (not x0 and not x3))) 

def FE(x3, x2, x1, x0):
    return (not x0 and(x1 or not x2 or x3)) or (x1 and x3)

def FF(x3, x2, x1, x0):
    return (x1 and(x3 or (not x0 and x2))) or (not x2 and x3) or (not x1 and not x3 and (not x0 or x2))
def FG(x3, x2, x1, x0):
    return (x1 and (not x0 or not x2)) or (not x1 and x2) or x3

def checkA():
    print(FA(0,0,0,0) == 1 )
    print(FA(0,0,0,1) == 0 )
    print(FA(0,0,1,0) == 1 )
    print(FA(0,0,1,1) == 1 )
    print(FA(0,1,0,0) == 0 )
    print(FA(0,1,0,1) == 1 )
    print(FA(0,1,1,0) == 1 )
    print(FA(0,1,1,1) == 1 )
    print(FA(1,0,0,0) == 1 )
    print(FA(1,0,0,1) == 1 )
    print(FA(1,0,1,0) == 1 )
    print(FA(1,0,1,1) == 0 )
    print(FA(1,1,0,0) == 1 )
    print(FA(1,1,0,1) == 0 )
    print(FA(1,1,1,0) == 1 )
    print(FA(1,1,1,1) == 1 )
def checkB():
    print(FB(0,0,0,0) == 1 )
    print(FB(0,0,0,1) == 1 )
    print(FB(0,0,1,0) == 1 )
    print(FB(0,0,1,1) == 1 )
    print(FB(0,1,0,0) == 1 )
    print(FB(0,1,0,1) == 0 )
    print(FB(0,1,1,0) == 0 )
    print(FB(0,1,1,1) == 1 )
    print(FB(1,0,0,0) == 1 )
    print(FB(1,0,0,1) == 1 )
    print(FB(1,0,1,0) == 1 )
    print(FB(1,0,1,1) == 0 )
    print(FB(1,1,0,0) == 0 )
    print(FB(1,1,0,1) == 1 )
    print(FB(1,1,1,0) == 0 )
    print(FB(1,1,1,1) == 0 )

def checkC():
    print(FC(0,0,0,0) == 1 )
    print(FC(0,0,0,1) == 1 )
    print(FC(0,0,1,0) == 0 )
    print(FC(0,0,1,1) == 1 )
    print(FC(0,1,0,0) == 1 )
    print(FC(0,1,0,1) == 1 )
    print(FC(0,1,1,0) == 1 )
    print(FC(0,1,1,1) == 1 )
    print(FC(1,0,0,0) == 1 )
    print(FC(1,0,0,1) == 1 )
    print(FC(1,0,1,0) == 1 )
    print(FC(1,0,1,1) == 1 )
    print(FC(1,1,0,0) == 0 )
    print(FC(1,1,0,1) == 1 )
    print(FC(1,1,1,0) == 0 )
    print(FC(1,1,1,1) == 0 )

def checkD():
    print(FD(0,0,0,0) == 1 )
    print(FD(0,0,0,1) == 0 )
    print(FD(0,0,1,0) == 1 )
    print(FD(0,0,1,1) == 1 )
    print(FD(0,1,0,0) == 0 )
    print(FD(0,1,0,1) == 1 )
    print(FD(0,1,1,0) == 1 )
    print(FD(0,1,1,1) == 0 )
    print(FD(1,0,0,0) == 1 )
    print(FD(1,0,0,1) == 1 )
    print(FD(1,0,1,0) == 0 )
    print(FD(1,0,1,1) == 1 )
    print(FD(1,1,0,0) == 1 )
    print(FD(1,1,0,1) == 1 )
    print(FD(1,1,1,0) == 1 )
    print(FD(1,1,1,1) == 0 )

def checkE():
    print(FE(0,0,0,0) == 1 )
    print(FE(0,0,0,1) == 0 )
    print(FE(0,0,1,0) == 1 )
    print(FE(0,0,1,1) == 0 )
    print(FE(0,1,0,0) == 0 )
    print(FE(0,1,0,1) == 0 )
    print(FE(0,1,1,0) == 1 )
    print(FE(0,1,1,1) == 0 )
    print(FE(1,0,0,0) == 1 )
    print(FE(1,0,0,1) == 0 )
    print(FE(1,0,1,0) == 1 )
    print(FE(1,0,1,1) == 1 )
    print(FE(1,1,0,0) == 1 )
    print(FE(1,1,0,1) == 0 )
    print(FE(1,1,1,0) == 1 )
    print(FE(1,1,1,1) == 1 )

def checkF():
    print(FF(0,0,0,0) == 1 )
    print(FF(0,0,0,1) == 0 )
    print(FF(0,0,1,0) == 0 )
    print(FF(0,0,1,1) == 0 )
    print(FF(0,1,0,0) == 1 )
    print(FF(0,1,0,1) == 1 )
    print(FF(0,1,1,0) == 1 )
    print(FF(0,1,1,1) == 0 )
    print(FF(1,0,0,0) == 1 )
    print(FF(1,0,0,1) == 1 )
    print(FF(1,0,1,0) == 1 )
    print(FF(1,0,1,1) == 1 )
    print(FF(1,1,0,0) == 0 )
    print(FF(1,1,0,1) == 0 )
    print(FF(1,1,1,0) == 1 )
    print(FF(1,1,1,1) == 1 )

def checkG():
    print(FG(0,0,0,0) == 0 )
    print(FG(0,0,0,1) == 0 )
    print(FG(0,0,1,0) == 1 )
    print(FG(0,0,1,1) == 1 )
    print(FG(0,1,0,0) == 1 )
    print(FG(0,1,0,1) == 1 )
    print(FG(0,1,1,0) == 1 )
    print(FG(0,1,1,1) == 0 )
    print(FG(1,0,0,0) == 1 )
    print(FG(1,0,0,1) == 1 )
    print(FG(1,0,1,0) == 1 )
    print(FG(1,0,1,1) == 1 )
    print(FG(1,1,0,0) == 1 )
    print(FG(1,1,0,1) == 1 )
    print(FG(1,1,1,0) == 1 )
    print(FG(1,1,1,1) == 1 )

#checkA()#Correct
#checkB()#Correct
#checkC()#Correct
#checkD()#Correct
#checkE()#Correct
#checkF()#Correct
checkG()#Correct

