
import numpy as np
import matplotlib.pyplot as mp

import Kuramoto as ku
import OrderParameter as op
import CSV_handler as ch


class ProjectKuramoto:

    def __init__(self, _kuramotoInstance, _csvHandler):

        self.kuramoto         = _kuramotoInstance
        self.csvHandler       = _csvHandler
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
            print("current sigma", self.kuramoto.sigma)
            print("current result", i, ":", lastResult)
            timeindex = (i + 1) * _numOfTimeSteps
            self.csvHandler.writeVectorToFile( lastResult, timeindex )
            #phases = self.kuramoto.getPhaseResults() TODO
            #self.csvHandler.writeVectorsToFile( phases, 'phase-results.csv' )
            self.kuramoto.sigma += 0.1
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
    myCSV_handler = ch.CSV_handler()
    return ProjectKuramoto( myKuramoto1, myCSV_handler )

if __name__ == '__main__':


    myProjectKuramoto = prepareProject()
    myOrderParameter = op.OrderParameter()

    numOfOscillators = 50
    numOfTimeSteps   = 1000
    myProjectKuramoto.solveMultiStep( numOfOscillators,
                                      numOfTimeSteps, 5 )

    #myCSV_handler.writeVectorsToFile( step1phases, 'phase-results.csv' )
    #orderParameter = myOrderParameter.SumUpOrderMatrix_Elements( step1phases )
    #print("Order Parameter:", orderParameter)

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

