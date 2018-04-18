import pandas as pd
import numpy as np
import pandas.tools.plotting as pdplt
import matplotlib.pyplot as plt


pd.set_option('display.width', 1000)


#store file
print("Reading file...")
df = pd.read_csv("ntp-formatted.csv")


#ip 1
print("Storing server: ntp1.rrze.uni-e")
df0 = df.iloc[::4]
df0 = df0.reset_index(drop=True)

#ip 2
print("Storing server: cpt-ntp-app.mwe")
df1 = df.iloc[1::4]
df1 = df1.reset_index(drop=True)

#ip 3
print("Storing server: 196.21.187.2")
df2 = df.iloc[2::4]
df2 = df2.reset_index(drop=True)

#ip 4
print("Storing server: time-c-b.nist.g")
df3 =df.iloc[3::4]
df3 = df3.reset_index(drop=True)


#METRICS

print("====================================================================================")
print("                                 ntp1.rrze.uni-e")
print("====================================================================================")
print(df0.describe())
print("====================================================================================")
print("                                 cpt-ntp-app.mwe")
print("====================================================================================")
print(df1.describe())
print("====================================================================================")
print("                                 196.21.187.2")
print("====================================================================================")
print(df2.describe())
print("====================================================================================")
print("                                 time-c-b.nist.g")
print("====================================================================================")
print(df3.describe())
print("====================================================================================")

#GRAPHS

#OFFSET VS TIME
fig1 = plt.figure(1)
ax1 = fig1.add_subplot(111)


ax1.plot(df0.index.values,df0.offset.values, c='b',label='ntp1.rrze.uni-e')
ax1.plot(df1.index.values,df1.offset.values, c='r',label='cpt-ntp-app.mwe')
ax1.plot(df2.index.values,df2.offset.values, c='g',label='cpt-ntp-app.mwe')
ax1.plot(df3.index.values,df3.offset.values, c='y',label='cpt-ntp-app.mwe')

#DELAY VS TIME



plt.legend(loc='upper right');
plt.show()
