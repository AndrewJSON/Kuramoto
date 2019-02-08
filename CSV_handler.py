
''' 
 * CSV_handler.py
 *
 *   Created on:         08.02.2019
 *   Author:             Philippe Lehmann
 * 
 * General description:
 *   xxx
'''

import csv
import numpy as np


class CSV_handler:

    def __init__(self, _fileName):
        self.fileName = _fileName


    def writeVectorsToFile(self, _vectors):

        with open( self.fileName, mode='w' ) as out_file:
            csv_writer = csv.writer( out_file,      \
                                     delimiter=',', \
                                     quotechar='"', \
                                     quoting=csv.QUOTE_MINIMAL )

            self.writeOneRowPerVector( _vectors, csv_writer )


    def writeOneRowPerVector(self, _vectors, _writer):

            for vector in _vectors:
                _writer.writerow( vector )


if __name__ == '__main__':

    phase_vectors = np.array( [[0.4, 1.3, 6.9], [0.3, 1.2, 6.8], [0.2, 1.1, 6.7]] )
    myCSV_handler = CSV_handler('test_file.csv')

    myCSV_handler.writeVectorsToFile( phase_vectors )

    print("done.")

''' END '''

