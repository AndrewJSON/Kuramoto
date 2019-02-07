
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as mp
from numpy import diff


class Kuramoto:

    def __init__(self, _w, _a, _e, _b, _sigma):

        self.w = _w
        self.a = _a
        self.e = _e
        self.b = _b
        self.sigma = _sigma

        self.dydt    = None
        self.results = None
        self.x_init  = None
        self.t       = None
        self.N       = 0
        self.dkdt    = None
        self.Phis    = None

    def printResults(self):
        print("Results:")
        print( self.results )
        print (self.results.shape)

    def printInitialConditions(self):
        print("Initial conditions:")
        print(self.x_init)

    def printDydt(self):
        print( self.dydt )


    def sortData(self,_N):

       #sort Phi Data:

        self.N = _N
        Phis = self.results[:, :_N]
        Omegas = (Phis[999, :] - Phis[200, :]) / 799
        dtype = [('node', int), ('omega', float), ('phase', float)]
        values = [(i, round(Omegas[i], 2), np.mod(Phis[999, i], 2 * np.pi)) for i in range(_N)]
        nodes = np.array(values, dtype=dtype)
        nodes_sorted = np.sort(nodes, order=['omega', 'phase'])
        kappa = self.results[-1,_N:].reshape(_N,_N)
        kappa = kappa[:, nodes_sorted['node']][nodes_sorted['node']]
        return(nodes_sorted,kappa)


    def kuramotoderiv(self, _x, _t):
        Phis = _x[:self.N]
        Kappas = _x[self.N:].reshape(self.N, self.N)
        DelPhis = (Phis - Phis[:, np.newaxis]).T
        DKappa = -self.e * (np.sin(DelPhis + self.b) + Kappas)
        DelPhis += self.a
        DelPhis = Kappas * np.sin(DelPhis)
        DPhis = -self.sigma*DelPhis.sum(axis=1) / Phis.shape[0] * (-1)
        self.dydt = np.concatenate((DPhis, DKappa.flatten()))

        return self.dydt

    def orderParameter(self):

        Phases = self.getPhasesFromAllTimeStepsInResults()
        PhaseDiff = self.getInterlayerPhaseDifferences( Phases )
        Order = np.exp(PhiDiff,)


    def getPhasesFromAllTimeStepsInResults(self):
        Results = np.array(self.results[: , :self.N])
        return Results



    def CreateOrderMatrixArray(self):

        _phases = self.getPhasesFromAllTimeStepsInResults()
        MatrixArray = []
        timeStepCount = _phases.shape[0]

        for ts in range(0,timeStepCount):
            singleTimeStepPhaseDiff = _phases[ts] - _phases[ts][:, np.newaxis]
            MatrixArray.append( singleTimeStepPhaseDiff )


        #print(timeStepCount)
        #print(OM[999].shape)
        #print(OM)


        return np.array(MatrixArray)




    def SumUpOrderMatrixArray(self):

        _omList = self.CreateOrderMatrixArray()
        omShape = _omList[0].shape
        sumOM = np.zeros(omShape)
        _phases = self.getPhasesFromAllTimeStepsInResults()

        for matrix in _omList:
            sumOM += matrix
        #print(_omList)
        #print(_phases.shape[0])
        #print(sumOM[49].shape)


        sumOM = np.exp(1j*sumOM)
        #sumOM = np.abs(sumOM)
        sumOM = sumOM / _phases.shape[0]

        #print(sumOM)

        return sumOM


    def SumUpOM_Elements(self):

        OrderMatrix = self.SumUpOrderMatrixArray()
        OrderParam = np.sum(OrderMatrix)/(OrderMatrix.shape[0]*OrderMatrix.shape[0])
        print(OrderParam)



    def makeInitConditions(self):
        self.x_init = np.zeros(self.N*self.N+self.N)
        np.random.seed(935)
        #self.x_init[:] = (1+1) * np.random.random_sample(self.N*self.N+self.N) - 1
        self.x_init[0:self.N] = (2*np.pi) * np.random.random_sample(self.N)
        self.x_init[self.N:] = (1+1) * np.random.random_sample(self.N*self.N) - 1


    def makeTimeLine(self):
        self.t = np.linspace(0,1000,1000)


    def solveKuramoto(self, _N):

        self.N = _N
        self.makeInitConditions()
        self.makeTimeLine()

        self.results = odeint( self.kuramotoderiv, self.x_init, self.t )

        #print(self.results.shape)
        return self.results



if __name__ == '__main__':

    print("hello")

    w = np.linspace(0,50,num=50)
    a = 0.3*np.pi
    e = 0.01
    b = 0.23*np.pi
    sigma = 1

    myKuramoto1 = Kuramoto(w, a, e, b, sigma)

    kuramotoResults1 = myKuramoto1.solveKuramoto(50)
    #myKuramoto1.printInitialConditions()
    myKuramoto1.getPhasesFromAllTimeStepsInResults()
    myKuramoto1.CreateOrderMatrixArray()
    myKuramoto1.SumUpOrderMatrixArray()
    myKuramoto1.SumUpOM_Elements()
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




