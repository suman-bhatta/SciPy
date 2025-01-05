"""
Exporting Data in Matlab Format
Example: Export the following array as variable name "vec" to a mat file:
"""

from scipy import io
import numpy as np

arr = np.arange(10)

io.savemat('arr.mat', {"vec": arr})



"""
Import Data from Matlab Format
Example: Import the array from following mat file.:
"""

from scipy import io
import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9,])

# Export:
io.savemat('arr.mat', {"vec": arr})

# Import:
mydata = io.loadmat('arr.mat')

print(mydata)