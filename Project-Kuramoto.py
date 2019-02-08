
import numpy as np
import matplotlib.pyplot as mp

import Kuramoto as ku
import OrderParameter as op
import CSV_handler as ch


w = np.linspace(0,50,num=50)
a = 0.3*np.pi
e = 0.01
b = 0.23*np.pi
sigma = 1

myKuramoto1 = ku.Kuramoto(w, a, e, b, sigma)
myOrderParameter = op.OrderParameter()
myCSV_handler = ch.CSV_handler()


kuramotoResults1 = myKuramoto1.solveKuramoto(50)
#myKuramoto1.printInitialConditions()

phases_only = myKuramoto1.getPhases()
myCSV_handler.writeVectorsToFile( phases_only, 'phase-results.csv' )
orderParameter = myOrderParameter.SumUpOrderMatrix_Elements( phases_only )

print("Order Parameter:", orderParameter)
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

