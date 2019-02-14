
''' 
 * Kuramoto.py
 *
 *   Created on:         08.01.2019
 *   Author:             Philippe Lehmann
 * 
 * General description:
 *   xxx
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as mp
from numpy import diff

class Kuramoto:

    def __init__(self,_a, _e, _b, _sigma):

        self.a = _a
        self.e = _e
        self.b = _b
        self.sigma = _sigma

        self.dydt    = None
        self.results = {}
        self.x_init  = None
        self.t       = None
        self.N       = 0
        self.dkdt    = None
        self.Phis    = None


    def solveKuramoto(self, _numOfOscillators, _numOfTimeSteps, _initCond):

        self.N      = _numOfOscillators
        self.x_init = _initCond

        self.makeTimeLine( _numOfTimeSteps )

        results = odeint( self.kuramotoderiv, self.x_init, self.t )
        self.storeResultsAsDict( results )


    def makeTimeLine(self, _numOfTimeSteps):

        startTime       = 0
        endTime         = _numOfTimeSteps
        numOfIntervalls = _numOfTimeSteps

        self.t = np.linspace( startTime, endTime, numOfIntervalls )


    def storeResultsAsDict(self, _results):

        self.results['Phases']    = _results[: , :self.N]
        self.results['Couplings'] = _results[: , self.N:self.N**2+self.N]


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


    def getResults(self, _resultName, _timeIntervall=None):

        results = None

        if _resultName in self.results:
            results = self.results[_resultName]
        else:
            results = self.getAllResultsInOneVectorPerTimeStep()


        if _timeIntervall:
            return self.selectResultsInTimeInterval( results, _timeIntervall )
        else:
            return results


    def getAllResultsInOneVectorPerTimeStep(self):

        phases = self.results['Phases']
        couplings = self.results['Couplings']

        resultsAsOneVectorPerTimeStep = np.concatenate((phases, couplings), axis=1)
        return resultsAsOneVectorPerTimeStep


    def selectResultsInTimeInterval(self, _results, _timeIntervall):

            t1 = _timeIntervall[0]
            t2 = _timeIntervall[1]
            return _results[t1:t2]


#########

    def printResults(self):
        print("Results:")
        print( self.results )
        print (self.results.shape)


    def printPhases(self):

        print("Phases:")
        phases_only = self.getPhases()
        print( phases_only )
        print("shape:", phases_only.shape )


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

        values = [(i,\
                   round(Omegas[i], 2),\
                   np.mod(Phis[999, i],\
                   2 * np.pi)) for i in range(_N)]

        nodes = np.array(values, dtype=dtype)
        nodes_sorted = np.sort(nodes, order=['omega', 'phase'])
        kappa = self.results[-1,_N:].reshape(_N,_N)
        kappa = kappa[:, nodes_sorted['node']][nodes_sorted['node']]
        return(nodes_sorted,kappa)


    def makeFurtherInitConditions(self, _LastResultsCSV):
        self.x_init = np.zeros(self.N*self.N+self.N)

        "Read the Last Line of CSV Handler and replace the zeros in x_init"


    def solveFurtherKuramoto(self, _N):
        self.N = _N
        self.makeFurtherInitConditions()
        self.makeTimeLine()

        self.results = odeint( self.kuramotoderiv, self.x_init, self.t)

        return self.results


    def getResultsOfLastTimeStep(self):

        LastResults = np.array(self.results[999, :])
        return LastResults


if __name__ == '__main__':

    plot_results = True

    w = np.linspace(0,50,num=50)
    a = 0.3*np.pi
    e = 0.01
    b = 0.23*np.pi
    sigma = 1

    myKuramoto1 = Kuramoto(w, a, e, b, sigma)

    kuramotoResults1 = myKuramoto1.solveFirstKuramoto(50)
    myKuramoto1.printInitialConditions()
    #myKuramoto1.printResults()
    myKuramoto1.printPhases()

    if plot_results:
        mp.plot( kuramotoResults1 )
        mp.show()
    #Phases, Kappas = myKuramoto1.sortData(50)
    #mp.plot (Phases[:]["omega"])
    #mp.show()
    #mp.imshow(Kappas,origin = "lower")
    #mp.colorbar()
    #mp.show()

''' END '''

