
import numpy             as np
import matplotlib.pyplot as mp

import Kuramoto         as ku
import InitGenerator    as ig
import CSV_handler      as ch
import CSV_vectorWriter as vw
import CSV_vectorReader as vr
import OrderParameter   as op


class ProjectKuramoto:

    def __init__(self, _kuramoto, _initGenerator, _csvHandler, _numOsc=50):

        self.kuramoto         = _kuramoto
        self.init             = _initGenerator
        self.csvHandler       = _csvHandler

        self.numOsc           = 0
        self.timeSteps        = 0
        self.allResults       = None

        self.setNumberOfOscillators( _numOsc )


    def setNumberOfOscillators(self, _numOsc):

        self.numOsc   = _numOsc

        self.kuramoto.setNumberOfOscillators( _numOsc )
        self.init.setNumberOfOscillators( _numOsc )
        self.csvHandler.setVectorLength( _numOsc )

        print("\nNumber of oscillators set to", self.numOsc, "\n")


    def solveMultipleRunsWithSelfFeedingInit(self, _runs, _timeStepsToStore):

        randomInit = self.init.makeRandomInitConditions()
        self.kuramoto.solveKuramoto( self.timeSteps, randomInit )
        newInitValue = self.getLastTimeStep()

        print("last result", newInitValue)

        for i in range(0, _runs):

            self.kuramoto.solveKuramoto( self.timeSteps, newInitValue )

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
        return self.csvHandler.getVectorBlockFromFile( _fileName, _blockSize )


    def solveKuramotoWithGivenInit(self, _numOfTimeSteps, _init):
        self.kuramoto.solveKuramoto( _numOfTimeSteps, _init )


    def getLastTimeStep(self):

        #FIXME cake slice: getSingleResult vs. getResultTimeInterval
        lastTimeStep = (self.timeSteps - 1, self.timeSteps)
        return self.kuramoto.getResults( "all", lastTimeStep )[0]


    def getPhaseResults(self, _timeIndex=None):
        return self.kuramoto.getPhaseResults( _timeIndex )


    def getCouplingResults(self, _timeIndex=None):
        return self.kuramoto.getCouplingResults( _timeIndex )


def prepareProject():

    a      = 0.3*np.pi
    e      = 0.01
    b      = 0.23*np.pi
    sigma  = 1.0
    numOsc = 50

    myKuramoto1     = ku.Kuramoto(a, e, b, sigma)
    myInitGenerator = ig.InitGenerator()
    myVectorWriter  = vw.CSV_vectorWriter()
    myVectorReader  = vr.CSV_vectorReader()
    myCSV_handler   = ch.CSV_handler( myVectorWriter, myVectorReader )

    return ProjectKuramoto( myKuramoto1, myInitGenerator, myCSV_handler, numOsc )

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

    myProjectKuramoto.csvHandler.reader.getVectorBlock(30,40)

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

