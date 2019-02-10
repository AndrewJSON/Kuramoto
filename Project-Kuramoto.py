
import numpy as np
import matplotlib.pyplot as mp

import Kuramoto as ku
import OrderParameter as op
import CSV_handler as ch


class ProjectKuramoto:

    def __init__(self, _kuramotoInstance):

        self.kuramoto         = _kuramotoInstance
        self.N                = None
        self.x_init           = None
        self.allResults       = None


    def solveMultiStep(self, _numOfOscillators, _numOfTimeSteps, _steps):

        self.solveKuramotoWithRandomInit( _numOfOscillators, _numOfTimeSteps)
        lastResult = self.kuramoto.results[_numOfTimeSteps - 1]

        for i in range(0, _steps):
            self.solveKuramotoWithGivenInit( _numOfOscillators,
                                             _numOfTimeSteps,
                                             lastResult )
            print("current result:", lastResult)
            lastResult = self.kuramoto.results[_numOfTimeSteps - 1]
            


    def solveKuramotoWithRandomInit(self, _numOfOscillators, _numOfTimeSteps):

        self.N = _numOfOscillators
        self.makeRandomInitConditions()
        self.solveKuramotoWithGivenInit( _numOfOscillators,
                                         _numOfTimeSteps,
                                         self.x_init )


    def solveKuramotoWithGivenInit(self, _numOfOscillators, _numOfTimeSteps, _init):

        self.kuramoto.solveKuramoto( _numOfOscillators,
                                     _numOfTimeSteps, 
                                     _init )


    def makeRandomInitConditions(self):

        self.prepareRandomGenerator()
        self.prepareInitVector()
        self.makeRandomInitPhases()
        self.makeRandomInitCouplings()


    def prepareRandomGenerator(self):
        np.random.seed(935)


    def prepareInitVector(self):
        self.x_init = np.zeros(self.N*self.N+self.N)


    def makeRandomInitPhases(self):
        self.x_init[0:self.N] = (2*np.pi) * np.random.random_sample(self.N)


    def makeRandomInitCouplings(self):
        self.x_init[self.N:] = (1+1) * np.random.random_sample(self.N*self.N) - 1


    def getPhaseResults(self, _timeIndex=None):
        return self.kuramoto.getPhaseResults( _timeIndex )


    def getCouplingResults(self, _timeIndex=None):
        return self.kuramoto.getCouplingResults( _timeIndex )


def prepareProject():

    a     = 0.3*np.pi
    e     = 0.01
    b     = 0.23*np.pi
    sigma = 1.0

    myKuramoto1 = ku.Kuramoto(a, e, b, sigma)
    return ProjectKuramoto( myKuramoto1 )

if __name__ == '__main__':


    myProjectKuramoto = prepareProject()
    myOrderParameter = op.OrderParameter()
    myCSV_handler = ch.CSV_handler()

    numOfOscillators = 50
    numOfTimeSteps   = 1000
    myProjectKuramoto.solveKuramotoWithRandomInit( numOfOscillators,
                                                   numOfTimeSteps )


    randPhases    = myProjectKuramoto.getPhaseResults( 999 )
    randCouplings = myProjectKuramoto.getCouplingResults( 999 )

    print("shape:", randPhases.shape)

 
    step1Inits = np.concatenate( (randPhases, randCouplings) )

    myProjectKuramoto.solveKuramotoWithGivenInit( numOfOscillators,
                                                  numOfTimeSteps,
                                                  step1Inits )

    step1phases = myProjectKuramoto.getPhaseResults()
    step1Couplings = myProjectKuramoto.getCouplingResults()

    myCSV_handler.writeVectorsToFile( step1phases, 'phase-results.csv' )
    orderParameter = myOrderParameter.SumUpOrderMatrix_Elements( step1phases )
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

