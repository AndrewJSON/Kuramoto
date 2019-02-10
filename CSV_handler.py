
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

        with open( _fileName, mode='a' ) as out_file:
            csv_writer = csv.writer( out_file,      \
                                     delimiter=',', \
                                     quotechar='"', \
                                     quoting=csv.QUOTE_MINIMAL )

            self.writeVectors( _vectors, csv_writer )
            print("file", _fileName, "successfully written")


    def writeVectors(self, _vectors, _writer):

            timeStepIndex = 0
            for vector in _vectors:
                timeStepIndex += 1
                self.writeOneRowPerVector( vector, _writer, timeStepIndex)


    def writeVectorToFile(self, _vector,
                                _timeStepIndex, 
                                _fileName='kuramoto-results.csv'):

        with open( _fileName, mode='a' ) as out_file:
            csv_writer = csv.writer( out_file,      \
                                     delimiter=',', \
                                     quotechar='"', \
                                     quoting=csv.QUOTE_MINIMAL )

            self.writeOneRowPerVector( _vector, _timeStepIndex, csv_writer )
            print("file", _fileName, "successfully written")


    def writeOneRowPerVector(self, _vector, _timeStepIndex, _writer):

        vectorWithTmStep = self.addTimeStepAsFirstElement( _vector, \
                                                           _timeStepIndex)
        _writer.writerow( vectorWithTmStep )


    def addTimeStepAsFirstElement(self, _vector, _timeStepIndex):

        insertInFrontOfElementInVector = 0  # 0 indicates first element
        return np.insert(_vector, insertInFrontOfElementInVector, _timeStepIndex)


if __name__ == '__main__':

    phase_vectors = np.array( [[0.4, 1.3, 6.9], [0.3, 1.2, 6.8], [0.2, 1.1, 6.7]] )
    myCSV_handler = CSV_handler()

    myCSV_handler.writeVectorsToFile( phase_vectors, 'test_file.csv' )

    print("done.")

''' END '''

