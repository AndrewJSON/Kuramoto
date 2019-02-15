
''' 
 * CSV_vectorWriter.py
 *
 *   Created on:         15.02.2019
 *   Author:             Andrew Jason Bishop
 * 
 * General description:
 *   https://realpython.com/python-csv/
'''

import csv


class CSV_vectorWriter:

    def __init__(self):
        pass


    def writeVectorsToFile(self, _vectors                ,\
                                 _fileAccessMode         ,\
                                 _fileName = 'default.csv'):

        with open( _fileName, mode = _fileAccessMode ) as out_file:
            csv_writer = csv.writer( out_file, delimiter=',' )

            self.writeVectors( _vectors, csv_writer )
            print("file", _fileName, "successfully written")


    def writeVectors(self, _vectors, _writer):

        if self.isSingleVector( _vectors ):
            _vectors = self.expandVectorDimension( _vectors )

        for vector in _vectors:
            _writer.writerow( vector )


    def isSingleVector(self, _DUT):
        return ( 1 == len(_DUT.shape) )


    def expandVectorDimension(self, _singleVector):
        return np.expand_dims(_singleVector, axis=0)


''' END '''

