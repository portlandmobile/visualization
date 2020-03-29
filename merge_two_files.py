import pandas as pd
import sys
import numpy as np

# Get the names of the two filss
argList = sys.argv

df1 = pd.read_csv(argList[1])
df2 = pd.read_csv(argList[2])

print df1
print df2

# Merge the two files with new column added. ref:https://kanoki.org/2019/07/04/pandas-difference-between-two-dataframes/
# newfile = pd.concat([file1, file2], axis=1, join='outer')
# print df1.sort_values(by='name', ascending=True)
# print df2.sort_values(by='name', ascending=True)
df1 = df1.set_index('name')
df2 =df2.set_index('name')

df1['data']=df2['data']

print df1, '\n\n', df2