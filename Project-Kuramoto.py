
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
        self.N                = None
        self.allResults       = None


    def solveMultipleRunsWithSelfFeedingInit(self, _numOsc,   
                                                   _numOfTimeSteps,
                                                   _timeStepsToStore,
                                                   _runs):
        numTS = _numOfTimeSteps

        self.solveKuramotoWithRandomInit( _numOsc, numTS)

        lastTimeStep = (numTS - 1, numTS)
        #FIXME cake slice: getSingleResult vs. getResultTimeInterval
        newInitValue = self.kuramoto.getResults( "all", lastTimeStep )[0]

        print("last result", newInitValue)

        for i in range(0, _runs):

            self.solveKuramotoWithGivenInit( _numOsc,
                                             _numOfTimeSteps,
                                             newInitValue )

            print("current sigma", self.kuramoto.sigma)   #TODO
            print("current result", i, ":", newInitValue) #TODO

            t1 = _numOfTimeSteps - _timeStepsToStore - 1
            t2 = _numOfTimeSteps - 1

            phases = self.kuramoto.getResults( 'Phases', (t1,t2) )
            self.saveRun( phases, 'phase-results.csv' )

            self.kuramoto.sigma += 0.1
            #FIXME cake slice
            newInitValue = self.kuramoto.getResults( "all", lastTimeStep )[0]


    def saveRun(self, _resultsToSave, _fileName):
        self.csvHandler.writeVectorsToNewFile( _resultsToSave, _fileName )


    def getRunFromFile(self, _fileName, _blockSize, _vectorLength):

        run = self.csvHandler.getVectorBlockFromFile( _fileName    ,\
                                                      _blockSize   ,\
                                                      _vectorLength )
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

    numOsc = 50
    numOfTimeSteps   = 100
    timeStepsToStore = 50
    numOfRuns        = 3


    myProjectKuramoto.solveMultipleRunsWithSelfFeedingInit( numOsc          ,\
                                                            numOfTimeSteps  ,\
                                                            timeStepsToStore,\
                                                            numOfRuns        )


    timeStepsToRead = 50
    run = myProjectKuramoto.getRunFromFile( 'phase-results.csv',\
                                            timeStepsToRead    ,\
                                            numOsc              )


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

