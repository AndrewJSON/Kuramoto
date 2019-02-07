
import numpy as np
import matplotlib.pyplot as mp

import Kuramoto as ku


w = np.linspace(0,50,num=50)
a = 0.3*np.pi
e = 0.01
b = 0.23*np.pi
sigma = 1

myKuramoto1 = ku.Kuramoto(w, a, e, b, sigma)

kuramotoResults1 = myKuramoto1.solveKuramoto(50)
#myKuramoto1.printInitialConditions()
myKuramoto1.getPhasesFromAllTimeStepsInResults()
myKuramoto1.CreateOrderMatrixArray()
myKuramoto1.SumUpOrderMatrixArray()
orderParam = myKuramoto1.SumUpOM_Elements()
print("Order Parameter:", orderParam)
#myKuramoto1.printResults()
#mp.plot( kuramotoResults1 )
#mp.show()
#Phases, Kappas = myKuramoto1.sortData(50)
#mp.plot (Phases[:]["omega"])
#mp.show()
#mp.imshow(Kappas,origin = "lower")
#mp.colorbar()
#mp.show()

''' END '''

