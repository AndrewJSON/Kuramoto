
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
from itertools import islice
 

class CSV_handler:

    def __init__(self, _writer, _reader):

        self.writer = _writer
        self.reader = _reader


    def setVectorLength(self, _N):

        self.writer.setVectorLength( _N )
        self.reader.setVectorLength( _N )


    def appendVectorsToFile(self, _vectors, _fileName):
        self.writer.writeVectorsToFile( _vectors, 'a', _fileName )


    def writeVectorsToNewFile(self, _vectors, _fileName):
        self.writer.writeVectorsToFile( _vectors, 'w', _fileName )


    def getVectorBlockFromFile(self, _fileName, _blockSize):
        return self.reader.getVectorBlockFromFile(_fileName, _blockSize)


''' END '''

