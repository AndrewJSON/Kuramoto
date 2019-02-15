
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


class CSV_vectorReader:

    def __init__(self):
        pass


    def getVectorBlockFromFile(self, _fileName, _blockSize, _vectorLength):

        vectorBlock = self.getPreparedNumpyArray( _blockSize, _vectorLength )

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


    def getPreparedNumpyArray(self, _blockSize, _vectorLength):
        return np.zeros( (_blockSize, _vectorLength) )


    def getVectorsBelowRowNumber(self, _row=100):

        with open('my_data.csv') as fd:
            for row in islice(csv.reader(fd), _row, None):
                print(row)


''' END '''

