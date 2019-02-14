
import numpy as np
import matplotlib.pyplot as mp

import Kuramoto as ku
import InitGenerator as ig
import CSV_handler as ch
import OrderParameter as op


class ProjectKuramoto:

    def __init__(self, _kuramoto, _initGenerator, _csvHandler):

        self.kuramoto         = _kuramoto
        self.csvHandler       = _csvHandler
        self.init             = _initGenerator
        self.numOsc           = 0
        self.timeSteps        = 0
        self.allResults       = None


    def solveMultipleRunsWithSelfFeedingInit(self, _runs, _timeStepsToStore):

        randomInit = self.init.makeRandomInitConditions( self.numOsc )
        self.kuramoto.solveKuramoto( self.numOsc, self.timeSteps, randomInit )
        newInitValue = self.getLastTimeStep()

        print("last result", newInitValue)

        for i in range(0, _runs):

            self.kuramoto.solveKuramoto( self.numOsc   ,\
                                         self.timeSteps,\
                                         newInitValue )

            print("current sigma", self.kuramoto.sigma)   #TODO
            print("current result", i, ":", newInitValue) #TODO

            t1 = self.timeSteps - _timeStepsToStore - 1
            t2 = self.timeSteps - 1

            phases = self.kuramoto.getResults( 'Phases', (t1,t2) )
            self.saveRun( phases, 'phase-results.csv' )

            self.kuramoto.sigma += 0.1
            newInitValue = self.getLastTimeStep()


    def saveRun(self, _resultsToSave, _fileName):
        self.csvHandler.writeVectorsToNewFile( _resultsToSave, _fileName )


    def getRunFromFile(self, _fileName, _blockSize):

        run = self.csvHandler.getVectorBlockFromFile( _fileName    ,\
                                                      _blockSize   ,\
                                                      self.numOsc )
        return run


    def solveKuramotoWithRandomInit(self, _numOsc, _numOfTimeSteps):

        self.N = _numOsc
        randomInit = self.init.makeRandomInitConditions( _numOsc )
        self.solveKuramotoWithGivenInit( _numOsc,
                                         _numOfTimeSteps,
                                         randomInit )


    def solveKuramotoWithGivenInit(self, _numOsc, _numOfTimeSteps, _init):

        self.kuramoto.solveKuramoto( _numOsc,
                                     _numOfTimeSteps, 
                                     _init )

    def getLastTimeStep(self):

        #FIXME cake slice: getSingleResult vs. getResultTimeInterval
        lastTimeStep = (self.timeSteps - 1, self.timeSteps)
        return self.kuramoto.getResults( "all", lastTimeStep )[0]


    def getPhaseResults(self, _timeIndex=None):
        return self.kuramoto.getPhaseResults( _timeIndex )


    def getCouplingResults(self, _timeIndex=None):
        return self.kuramoto.getCouplingResults( _timeIndex )


def prepareProject():

    a     = 0.3*np.pi
    e     = 0.01
    b     = 0.23*np.pi
    sigma = 1.0

    myKuramoto1     = ku.Kuramoto(a, e, b, sigma)
    myInitGenerator = ig.InitGenerator()
    myCSV_handler   = ch.CSV_handler()
    return ProjectKuramoto( myKuramoto1, myInitGenerator, myCSV_handler )

if __name__ == '__main__':


    myProjectKuramoto = prepareProject()
    myOrderParameter = op.OrderParameter()

    myProjectKuramoto.numOsc    = 50
    myProjectKuramoto.timeSteps = 100

    timeStepsToStore = 50
    numOfRuns        = 3

    myProjectKuramoto.solveMultipleRunsWithSelfFeedingInit( numOfRuns       ,\
                                                            timeStepsToStore )

    timeStepsToRead = 50
    run = myProjectKuramoto.getRunFromFile( 'phase-results.csv',\
                                            timeStepsToRead    )

    orderParameter = myOrderParameter.SumUpOrderMatrix_Elements( run )
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

