#Optimiser using differential evolution

from scipy.optimize import differential_evolution
import numpy as np
from math import sqrt, e, inf
from objectiveFunction import objF, r


def getBounds(lpQuant):
     return[(-500, 500),]*lpQuant*2



def runOptimiser(lpQuant,H,dQ):
    #lpQuant is the number of launchpads to be built
    #dQuant is the number of drones that need to be distribute between the launchpad in the system

    #Format of variables
    #All the variables are stored in an array x, 
    # x[0]      x[1]        ....This repeated for every 
    # xCordLp  yCordLp  droneCount
    x = np.zeros(lpQuant*2) #Define the array of variables. 3 * the number of launchpads

    func = lambda x: objF(x,H,lpQuant,dQ) 

    bnds = getBounds(lpQuant)

    res = differential_evolution(func, bounds=bnds,maxiter=1000000,disp=False,popsize=20,strategy='randtobest1exp')
    
    #print(res.x)
    #print(res.fun)
    utility = res.fun
    optimums = res.x

    #Convert the optimum coordinates and drone distribution into the correct format
    for t in range (0,(int(len(optimums)/2))):
            if t == 0:
                LPs = np.array([[int(optimums[0]),int(optimums[1]),dQ[t]]])
            else:
                LPs = np.append(LPs,[[int(optimums[t*2]),int(optimums[(t*2)+1]),dQ[t]]],axis=0)
    
    return(utility,LPs) #Return the best utility value for this setup and the launchpad matrix