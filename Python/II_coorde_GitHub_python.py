# -*- coding: utf-8 -*-
"""
Created on July 2020
By Omar Alminagorta

Parallel coordinates implementation using Python and "plotly" library

Input: Subsample of the Ontario Fish Database
Code:Load the data, clean it, and plot it
Output : Parallel coordinates visualization
"""

#Importing Packages
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot # this is key to show the plot in spyder

#%%Load Data
#pd.read_csv('CABIN_SubSample.csv', index_col=0)

#Use this if the data is online
#df = pd.read_csv("https://raw.githubusercontent.com/alminagorta/Parallel-Coordinates/Using_Python/Data/OntarioFishDatabase.csv?token=AB53NSBHCACYLJPHW6YKPGC7EGXAM")

#Use this if the data is on the computer
file_name='OntarioFishDatabase.xlsx'
xl = pd.ExcelFile(file_name)
df=pd.read_excel(xl)

#%% Pre-processing data
df.shape #number of rows and columns 
columns=list(df.columns) #getting the names of columns

# check missing values 
df.isnull().sum()

#% Cleaning data
print(list(df.columns))
df.head()

##% Selecting main Variables to plot 
#data2=df[df.columns[4:11]]


#%% Plotting using "plotly" library

#processing the numercial data to plot
dimensions3=[]
list1=range(4,11)# selecting numerical columns to plot
for i in list1:
    dimensions2 = dict(range = [df.iloc[:,i].min(),df.iloc[:,i].max()],#setting minimum and maximum level of each axis
     label = df.columns[i], values = df.iloc[:,i])#seting Axis labeling
    dimensions3.append(dimensions2)
            
FigParaCoord = go.Figure(data=
    go.Parcoords(
        line = dict(color = df['RecordLengthTL_cm'],#seting the colors of the scale 
                   colorscale = 'sunset',
                   showscale = True,
                   cmin = 1,#minimum scale color
                   cmax = 230),#maximum scale color
                   dimensions = dimensions3#
    ))
plot(FigParaCoord)



















