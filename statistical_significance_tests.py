""""
T-Test
Example: Find if the given values v1 and v2 are from same distribution:
"""

import numpy as np
from scipy.stats import ttest_ind

v1 = np.random.normal(size=100)
v2 = np.random.normal(size=100)

res = ttest_ind(v1, v2)

print(res)



"""
KS-Test
Example: Find if the given value follows the normal distribution:
"""

import numpy as np
from scipy.stats import kstest

v = np.random.normal(size=100)

res = kstest(v, 'norm')

print(res)  


"""
Statistical Description of Data
Example: Show statistical description of the values in an array:
"""

import numpy as np
from scipy.stats import describe

v = np.random.normal(size=100)
res = describe(v)

print(res)


"""
Normality Tests (Skewness and Kurtosis)
Example: Find skewness and kurtosis of values in an array:
"""

import numpy as np
from scipy.stats import skew, kurtosis

v = np.random.normal(size=100)

print(skew(v))
print(kurtosis(v))