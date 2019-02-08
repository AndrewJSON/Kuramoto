
''' 
 * OrderParameter.py
 *
 *   Created on:         07.02.2019
 *   Author:             Philippe Lehmann
 * 
 * General description:
 *   xxx
'''

import numpy as np

class OrderParameter:

    def __init__(self):
        pass


    def SumUpOrderMatrix_Elements(self, _phases):

        OrderMatrix = self.SumUpOrderMatrixArray( _phases )
        OrderParam = np.sum(OrderMatrix)\
                         / (OrderMatrix.shape[0]*OrderMatrix.shape[0])
        return OrderParam


    def SumUpOrderMatrixArray(self, _phases):

        orderMatrixList = self.CreateOrderMatrixArray( _phases )
        orderMatrixShape = orderMatrixList[0].shape
        sumOrderMatrix = np.zeros(orderMatrixShape)

        for matrix in orderMatrixList:
            sumOrderMatrix += matrix
        #print(_omList)
        #print(_phases.shape[0])
        #print(sumOrderMatrix[49].shape)


        sumOrderMatrix = np.exp(1j*sumOrderMatrix)
        #sumOrderMatrix = np.abs(sumOrderMatrix)
        sumOrderMatrix = sumOrderMatrix / _phases.shape[0]

        #print(sumOrderMatrix)

        return sumOrderMatrix


    def CreateOrderMatrixArray(self, _phases):

        MatrixArray = []
        timeStepCount = _phases.shape[0]

        for ts in range(0,timeStepCount):
            singleTimeStepPhaseDiff = _phases[ts] - _phases[ts][:, np.newaxis]
            MatrixArray.append( singleTimeStepPhaseDiff )

        #print(timeStepCount)
        #print(OrderMatrix[999].shape)
        #print(OrderMatrix)

        return np.array(MatrixArray)

''' END '''

