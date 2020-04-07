#Tuning Objective Function

from objectiveFunction import objF
from drone_blood_delivery_map_drawing import drawMap
import numpy as np
import time
from random import randrange

#Set the parameters of the objective function


#This function returns an array of utilies spread across the map when provided with a drone quantity and hospital array
sF = 1 #How large each sample point is

def mapUtilities(dQ,H,sF):
    mapOUts= np.zeros((int(1000/sF),int(1000/sF)))
    for r in range (int(1000/sF)):
        for c in range (int(1000/sF)):
            A=[(c-(int(500/sF)))*sF,(r-(int(500/sF)))*sF]
            utility = (objF(A,H,1,dQ))
            mapOUts[r][c] = utility
    return(mapOUts)


#Tuning array, 2 horizontal
H =  np.array([[100,100,10000],
               [250,100,10000],
               [175,220,10000]])

H =  np.array([[-72,-291,10201],#Tumu
               [31,-267,66685],#Bolgatanga
               [110,-274,130003],#Garu
               [125,-210,102446],#Wa
               [-17,116,5524],#Fufulso
               [31,139,360579],#Tamale
               [108,144,52008],#Yendi
               [114,-86,78812],#Bimbilla
               [-125,58,208496],#Sunyani
               [-85,35,104212],#Techiman
               [107,13,11788],#Kete-krachi
               [-74,196,33379],#Dunkwa
               [-59,167,168641],#Obuasi
               [68,184,122300],#Koforidua
               [176,149,34456],#Kpetoe
               [18,274,169894],#Cape coast
               [-68,288,445205]])#Sekondi


dQ = [15] #Drone Quantity
utilityMap = mapUtilities(dQ,H,sF)

x = [[0,0,10]]

drawMap(H,x,1,objVals = utilityMap, sF = sF)
time.sleep(200000)
