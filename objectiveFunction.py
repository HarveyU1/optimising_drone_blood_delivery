#Objective Function

from math import sqrt, e, inf

#Settings
r = 150 #Max drone range
q = 1 #Decresing utility with distance coefficient
b = 347610 #People per drone



#Define Objective function
def objF(x,H,lpQuant,dQ): #This defines the function to be optimised, x are the variables to be optimised and H is the array of hospital locations  
    return -sum([cap(x,H,i,lpQuant,dQ) for i in range(0,len(H))])

def cap(x,H,i,lpQuant,dQ):
    return ((2*H[i,2]) / (1 + e**((-2/H[i,2])*U(x , H, i,lpQuant,dQ)))) - (H[i, 2])

def U(x,H,i,lpQuant,dQ):
    return sum([Uij(H,H[i],x,j,dQ) for j in range(0,lpQuant)])

def Uij(H, hospital, x, j,dQ):
    return ((distance_utility(distance(hospital,x,j)) /(1+(0.00001*demand(H,x,j)))) * (b*dQ[j]))
    #

def distance_utility(d):
    #return(r - d*q) *iu(d-r)
    return (1 - d * (q/r)) * iu(d-r)

def distance(hospital,x,j):
    return sqrt ((hospital[0] - x[(j*2)])**2 + (hospital[1] - x[(j*2)+1])**2)

def demand(H,x,j):
    dmd = sum([iu(distance(H[i],x,j)-r) for i in range(0,len(H))])
    return dmd if dmd != 0 else inf

def iu(x):
    return 0 if x > 0 else 1

