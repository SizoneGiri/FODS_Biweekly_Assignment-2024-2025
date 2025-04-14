'''A program with Pandas module to add, subtract, multiple and divide two Pandas Series.'''

import pandas as pd
import numpy as np

# Creating a pandas Series 'a' with values 1 to 5
a = pd.Series([1,2,3,4,5])

# Creating a pandas Series 'b' with values 6 to 10
b = pd.Series([6,7,8,9,10])

# Printing the sum of Series 'a' and 'b'
print(f"The Sum is:\n{a+b}\n")

# Printing the difference of Series 'a' and 'b' (a - b)
print(f"The Subtraction is:\n{a-b} \n")

# Printing the product of Series 'a' and 'b' (element-wise multiplication)
print(f"The Multiple is: \n{a*b} \n")

# Printing the quotient of Series 'a' and 'b' (element-wise division)
print(f"The Quotient is: \n{a/b}")