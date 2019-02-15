
''' 
 * Kuramoto.py
 *
 *   Created on:         08.01.2019
 *   Author:             Philippe Lehmann
 *   Coauthor            Andrew Jason Bishop
 * 
 * General description:
 *   xxx
'''

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as mp
from numpy import diff

class InitGenerator:

    def __init__(self, _seed = 935):

        self.seed       = _seed
        self.initValues = None
        self.N = 1


    def setNumberOfOscillators(self, _numOsc):
        self.N = _numOsc


    def makeRandomInitConditions(self):

        self.prepareRandomGenerator()
        self.prepareInitVector()
        self.makeRandomInitPhases()
        self.makeRandomInitCouplings()

        return self.initValues


    def prepareRandomGenerator(self):
        np.random.seed( self.seed )


    def prepareInitVector(self):
        self.initValues = np.zeros(self.N*self.N+self.N)


    def makeRandomInitPhases(self):
        self.initValues[0:self.N] = (2*np.pi) * np.random.random_sample(self.N)


    def makeRandomInitCouplings(self):
        self.initValues[self.N:] = (1+1) * np.random.random_sample(self.N*self.N) - 1


''' END '''

