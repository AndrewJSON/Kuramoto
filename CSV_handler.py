
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

a = np.array([0.3, 1.2, 6.8])
b = np.array([0.4, 1.3, 6.9])

phase_vectors = np.array( [[0.4, 1.3, 6.9], [0.3, 1.2, 6.8]] )


if __name__ == '__main__':

    with open('employee_file.csv', mode='w') as employee_file:
        employee_writer = csv.writer( employee_file,\
                                      delimiter=',',\
                                      quotechar='"',\
                                      quoting=csv.QUOTE_MINIMAL )

        for phase_vector in phase_vectors:
            employee_writer.writerow( phase_vector )


''' END '''

