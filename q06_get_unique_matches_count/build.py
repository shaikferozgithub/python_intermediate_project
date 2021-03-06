# %load q06_get_unique_matches_count/build.py
# Default imports
from greyatomlib.python_intermediate.q05_read_csv_data.build import read_ipl_data_csv
path = 'data/ipl_matches_small.csv'

# Enter Code Here

import numpy as np
def get_unique_matches_count():
    def read_ipl_data_csv(file_path, dtype='|S50'):
        ipl_matches_array = np.genfromtxt(file_path,delimiter=',',dtype='|S50',skip_header=1)
        return ipl_matches_array
    unique_matches_count= len(np.unique(read_ipl_data_csv(path)[0:,0]))
    return unique_matches_count
