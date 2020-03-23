# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import pandas


df = pd.read_csv("C:/Users/Jeet Das/Desktop/hospital-data.csv",encoding="utf-8")

print("\n------- output data :-----------\n")
print("State-wise [ India ] hospitals :");
print("\n-----------------------------------\n")


# Question – A : get row and column numbers 

print('---------------------------------------------')
print("Dimension of the data frame = ",df.shape)
print('---------------------------------------------')

# Question – B : print column names :

print('------------------------\n Column names as follows :')
print('------------------------\n')
count = 0
for col in df.columns: 
        print(count,"-->",col)
        count = count+1
print("\n-----------------------------\n")

# Question – C : State_Name (using GROUP BY method) and no. of states :

state_names = df.groupby(['State'])[['District']].count()
print("---------------------------------")
print("\tAvailable states names : ")
print("-------------------------------")
print(state_names)
print("-------------------------------")
count = 0
for row in range(len(state_names)): 
        count = count+1
print("total no. of states = ",count)        
print("-----------------------------\n")

# Question - D : Hospitals in West Bengal

print("\n--- Hospitals in West Bengal :-------")
df_wb = df[df.State == 'West Bengal']
df_wb_dist = df_wb.groupby(['District'])[['District_ID']].count()

print("-----------------------------")
print("\t Disticts with no of hospitals in West Bengal :")
print("-----------------------------")
df1= df_wb_dist['District_ID'] 
print(df1)

print("-----------------------------")
count = 0
for row in range(len(df_wb_dist)): 
        count = count+1
print("total no. of district in West Bengal = ",count)        
print("-----------------------------\n")

print('---------------------------------------------')
print('\t Hospital name in West Bengal :');
print('----------------------------------------------')
print(df_wb['Hospital_Name'])
print('--------------------------------')


# Question - E : Number of Hospitals statewise

print("\n--- Number of Hospitals statewise :-------")

df_state = df.groupby(['State'])[['District_ID']].count()

print("-----------------------------")
print("\t Number of Hospitals statewise  :")
print("-----------------------------")
df2= df_state['District_ID'] 
print(df2)
print("-----------------------------")


