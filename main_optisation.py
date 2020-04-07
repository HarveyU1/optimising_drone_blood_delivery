#Code Version 2
import numpy as np
import math
from optimiserEvolution import runOptimiser,r #Import the optimiser
from drone_blood_delivery_map_drawing import drawMap
from random import randrange
import time

from itertools import combinations


def combination(numAirports, totalDrones):
    numbers = []
    correctComb = []
    if numAirports > totalDrones or numAirports < 1 or totalDrones < 1:
        print("Number of aiport cannot be greater than total drones, numAirports and totalDrones cannot be less than 1")
        return correctComb

    i = 1
    while (i <= totalDrones):
        j = 0
        while (j < int(totalDrones/i) and j <= numAirports):
            numbers.append(i)
            j += 1
        i += 1
    
    allComb = combinations(numbers, numAirports)

    for combination in allComb:
        sum = 0
        for value in combination:
            sum += value
        if sum == totalDrones:
            temp2d =[]
            for value in combination:
                temp2d.append(value)
            if temp2d not in correctComb:
                correctComb.append(temp2d)
    return correctComb

print(combination(-5,30))





#Settings
investement =   660000 #The amount of money in £ that is to be used for the drone network
launchPadCost = 200000 #Cost in £ of launch pad
droneCost =      20000 #Cost in £ of a drone

displayAnim = 10 #The number of times to show the animation of the optimisation


H =  np.array([[-72,-291,10201],#Tumu
               [31,-267,66685],#Bolgatanga
               [110,-274,130003],#Garu
               [-125,-210,102446],#Wa
               [-17,-116,5524],#Fufulso
               [31,-139,360579],#Tamale
               [108,-144,52008],#Yendi
               [114,-86,78812],#Bimbilla
               [-125,58,208496],#Sunyani
               [-85,35,104212],#Techiman
               [107,13,11788],#Kete-krach
               [-74,196,33379],#Dunkwa
               [-59,167,168641],#Obuasi
               [68,184,122300],#Koforidua
               [176,149,34456],#Kpetoe
               [-18,274,169894],#Cape coast
               [-68,288,445205]])#Sekondi

#dQ = np.array([1,10]) #Specifies the number of drones at each launchpad


maxLPs = int(investement/launchPadCost)
print("maxLps is {}".format(maxLPs))

solutions = []
solutionIndex = 0

for i in range(1,maxLPs+1):
    lpQuant = i #The number of launchpads to be built
    remMon = investement-(lpQuant*launchPadCost) #The remaining money to be spent on drones
    print("Remaining money is {}".format(remMon))
    dQuant = math.floor(remMon/droneCost) #The number of drones which can be built


    print(dQuant)

    #results = np.array([[1,]*lpQuant])
    #results = fPosib([],lpQuant,results)
    results = combination(lpQuant, dQuant) 
    #results = np.delete(results, 0, axis=0) #Remove the first row as it was only needed for initialisation 

    for dQ in results:#For each possible combination in reults
        start = time.time()
        utility, LPs = runOptimiser(lpQuant,H,dQ) #Run the optimiser function for a certian number of launchpads, hospital array and distribution of drones
        end = time.time()

        change = end-start

        solutions.append([utility,LPs])
        solutionIndex += 1
        drawMap(H,LPs,r,utility)

        print("For {} airports with {} distribution the utility is {}, locations are{} and it took {}".format(lpQuant,dQ,utility,LPs,change))


print(solutions)


#Play Animation, Cycle through possible solutions and display them
for q in range (displayAnim):
    for solution in solutions:
        LPs = solution[1]
        utility = solution[0]
        drawMap(H,LPs,r,utility)
        time.sleep(0.1)

#Find index of optimum utility
bestIndex = 0
for i in range(len(solutions)):
    if solutions[i][0] < solutions[bestIndex][0]:
        bestIndex = i

LPs = solutions[bestIndex][1]
utility = solutions[bestIndex][0]
print("The optimum arrangement of launchpads is {}".format(LPs))
print("The best utility value is {}".format(utility))
drawMap(H,LPs,r,utility)
time.sleep(20000)