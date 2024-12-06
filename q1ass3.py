

#q1
import numpy as np

print("NumPy version : ",np.__version__)
print("NumPy buil configuration : ",np.show_config())

#q2
import numpy as np

help(np.add)

#q3
import numpy as np

arr = np.array([1, 2, 3, 4])
print("None of the elements are zero : ",np.all(arr))

#q4
import numpy as np

arr = np.array([1, 0, np.nan, np.inf])
print("Finiteness of array elemets : ",np.isfinite(arr))

#q5
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([2, 2, 2])

print("Greater : ",np.greater(arr1, arr2))
print("Greater equal : ",np.greater_equal(arr1, arr2))

print("Less : ",np.less(arr1, arr2))
print("Less equal : ",np.less_equal(arr1, arr2))

#q6
import numpy as np

arr = np.array([1, 7, 13, 105])
print("Size of memory occupied : ",arr.nbytes," bytes")

#q7
import numpy as np

arr = np.arange(30, 71, 2)
print(arr)

#q8
import numpy as np

i = np.eye(3)
print("indentity matrix : \n",i)

#q9

import numpy as np

r = np.random.rand()
print("random number : ",r)

#q10

import numpy as np

r = np.random.standard_normal(15)

print("random numbers : \n",r)

#q11

import numpy as np

vector = np.arange(15, 56)
print(vector[1 : -1])

#12
import numpy as np

arr = np.arange(12).reshape(3,4)

for row in arr:
    print(row)

#13
import numpy as np

rv = np.random.randint(0, 11, size = 5)
print(rv)

#14
import numpy as np
import pandas as pd

d1 = np.array([10, 20, 30, 40, 50])
df = pd.DataFrame(d1)

print(df)

#15
import numpy as np
import pandas as pd
from datetime import datetime

date_series = pd.Series(pd.to_datetime(['2024-9-03', '2024-9-04', '2024-9-05']))

print("\nday of month : \n",date_series.dt.day)
print("\nday of year : \n\n",date_series.dt.dayofyear)
print("\nweek number : \n\n",date_series.dt.isocalendar().week)
print("\nday of week : \n\n",date_series.dt.day_name())

#16

import pandas as pd

series = pd.Series(['php', 'python','java','dmt'])

result = series.map(lambda x : x[0].upper() + x[1:-1] + x[-1].upper())

print(result)

#17
s = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9])

minv = s.min()

p_25 = s.quantile(0.25)

med = s.median()

p_75 = s.quantile(0.75)

maxv = s.max()

print("minimum : ",minv)
print("25th percentile : ",p_25)
print("median : ",med)
print("75th percentile : ",p_75)
print("maximum : ",maxv)
#18
s = pd.Series([2,3,6,6,8])

m = s.mean()
sd = s.std()

print("mean : ",m)
print("standard deviation : ",sd)

#19
import pandas as pd
import numpy as np
x = pd.Series([1, 2, 3])
y = pd.Series([6, 7, 8])

print("euclidean distance between two series : ",np.linalg.norm(x-y))
#20
import pandas as pd
result = pd.Series(pd.date_range('2024-01-01', periods=52, freq='W-SUN'))
print("all sundays : \n",result)