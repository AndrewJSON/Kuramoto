
''' 
 * CSV_handler.py
 *
 *   Created on:         08.02.2019
 *   Author:             Philippe Lehmann
 * 
 * General description:
 *   https://realpython.com/python-csv/
'''

import csv
import numpy as np


class CSV_handler:

    def __init__(self):
        pass


    def writeVectorsToFile(self, _vectors, _fileName='kuramoto-results.csv'):

        if self.isSingleVector( _vectors ):
            _vectors = self.expandDimension( _vectors )

        with open( _fileName, mode='a' ) as out_file:
            csv_writer = csv.writer( out_file                 ,\
                                     delimiter=','            ,\
                                     quotechar='"'            ,\
                                     quoting=csv.QUOTE_MINIMAL )

            self.writeVectors( _vectors, csv_writer )
            print("file", _fileName, "successfully written")


    def isSingleVector(self, _DUT):

        if 1 == len(_DUT.shape):
            return True
        else:
            return False


    def expandDimension( _singleVector ):
        return np.expand_dims(_singleVector, axis=0)


    def writeVectors(self, _vectors, _writer):

            for vector in _vectors:
                self.writeOneRowPerVector( vector, _writer)


    def writeOneRowPerVector(self, _vector, _writer):
        _writer.writerow( _vector )


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


if __name__ == '__main__':

    phase_vectors = np.array( [[0.4, 1.3, 6.9], [0.3, 1.2, 6.8], [0.2, 1.1, 6.7]] )
    myCSV_handler = CSV_handler()

    myCSV_handler.writeVectorsToFile( phase_vectors, 'test_file.csv' )

    print("done.")

''' END '''

