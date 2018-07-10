'''**************************************************************************************************************************
Author: Andrew Jablonski (adj8sh@virginia.edu)

Updated: 20180709  

Description:
This script will fit values of Vcmax, Jmax, and estimated Rd from A/Ci curves.
To run this script, files must be formatted in the appropriate manner (see example).
Scripts to process LI-6400/6800 data are found elsewhere. 

***************************************************************************************************************************'''
'Import libraries'
import os
import errno
import pandas as pd
import numpy as np

'****************************************************************************************************************************'
'****************************************************************************************************************************'
"Set base directory, input/output directory"
basedir    = os.path.join(os.path.expanduser("~"), "Documents", "Github", "Plant-Physiology").replace("\\","/") + '/'
input_dir  = "Example_Inputs/"
output_dir = "Example_Output/" 

if not os.path.exists(basedir+output_dir):
    try:
        os.makedirs(basedir+output_dir)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise          
'****************************************************************************************************************************'
'****************************************************************************************************************************'
"Set QA params"
min_points            = 3    #Minimum number of measurements/observations needed to fit parameters
temperature_threshold = 1.0  #If temperature span of points is +/- target C, find and remove outlier observations.
gs_cutoff             = 0.05 #If stomatal conductance (water vapor) of measurement is <= target, drop measurement.
ci_cutoff             = np.array([0,2000]) #If Ci of measurement is <=min, >=max, drop measurement.
'****************************************************************************************************************************'
'****************************************************************************************************************************'
'Parameterize Michaelis-Menten functions (taken from Long and Bernacchi 2003)'

R = 8.3144598 #gas constant
O = 210 #Intracellular oxygen
kc_25      = np.exp(38.05-79.43/(R/1000*(25.0+273.15))) #Carboxylation at 25C
ko_25      = np.exp(20.30-36.38/(R/1000*(25.0+273.15))) #Oxygenation at 25C
gamma_star = np.exp(19.02-37.83/(R/1000*(25.0+273.15))) #CO2 compensation point


'****************************************************************************************************************************'
'****************************************************************************************************************************'
"Read in .csv file with A/CI Curve data"
data = pd.read_csv(basedir+input_dir+"2015_Summer_Vcmax_Gasex_Data.csv")

leaf_col = "Leaf"
aci_column_names = ["Date","Leaf","Obs","Photo","Cond","Ci","Tleaf"]

for leaf in data[leaf_col].unique():
    selected_leaf = data.loc[data[leaf_col] == leaf,aci_column_names]

    
    
    
    
    


    
