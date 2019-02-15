
''' 
 * CSV_vectorReader.py
 *
 *   Created on:         15.02.2019
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   https://realpython.com/python-csv/
'''

import csv
import numpy as np
from itertools import islice


class CSV_vectorReader:

    def __init__(self):
        self.vectorLength = 1


    def setVectorLength(self, _N):
        self.vectorLength = _N


    def getVectorBlockFromFile(self, _fileName, _blockSize):

        vectorBlock = self.getPreparedNumpyArray( _blockSize )

        with open( _fileName, mode='r' ) as in_file:
            reader = csv.reader( in_file                  ,\
                                 delimiter=','            ,\
                                 quoting=csv.QUOTE_MINIMAL )

            for i in range(0, _blockSize):

                row = next(reader)
                npRow = np.asarray(row)
                npRow = npRow.astype(np.float)

                vectorBlock[i] = npRow

            print("successfully read", _fileName, ) 

        return vectorBlock


    def getPreparedNumpyArray(self, _blockSize):
        return np.zeros( (_blockSize, self.vectorLength) )



    def getVectorBlock(self, _start, _stop, _fileName='phase-results.csv' ):

        blockSize = _stop - _start
        vectorBlock = self.getPreparedNumpyArray( blockSize )

        with open( _fileName, mode='r' ) as in_file:

            reader = csv.reader( in_file, delimiter=',' )
            block  = islice(reader, _start, _stop)

            for i, row in enumerate(block):

                npRow = np.asarray(row)
                npRow = npRow.astype(np.float)

                print(i, npRow)


    def printVectorBlock(self, _start, _stop, _fileName='phase-results.csv' ):

        blockSize = _stop - _start
        vectorBlock = self.getPreparedNumpyArray( blockSize )

        with open( _fileName, mode='r' ) as in_file:

            reader = csv.reader( in_file, delimiter=',' )
            block  = islice(reader, _start, _stop)

            for i, row in enumerate(block):

                npRow = np.asarray(row)
                npRow = npRow.astype(np.float)

                print(i, npRow)


'''
        with open('my_data.csv') as fd:
            for row in islice(csv.reader(fd), _row, None):
                print(row)
'''

''' END '''

