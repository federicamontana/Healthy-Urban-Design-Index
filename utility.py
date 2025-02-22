"""
Created on 30/12/2024

This file is used to define vectors and functions that are going to be used in other notebooks.

@author: federica montana
"""
#-------------------------------------------------------
# Import packages
import pandas as pd
import os
os.environ['USE_PYGEOS'] = '0' 
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import re
from unidecode import unidecode
import joblib
from sklearn.preprocessing import QuantileTransformer
import seaborn as sns
from scipy import stats
from scipy.ndimage import label


# Define clusters
clusters = ['large metropolitan', 'metropolitan', 'medium', 'small', 'small towns']
# Define indicators
indicators = ['Optimal dwelling density','Compactness', 'Mid-rise development','Permeability',
              'Opportunity to walk','Opportunity to cycle','Public transport stops',
              'Air quality (PM2.5)','Air quality (NO2)','Surrounding greenness','Lower urban heat islands',
              'Universal access to green spaces','Access to large green spaces']
# Define domains
domains = ['Urban Design', 'Sustainable Transportation', 'Environmental Quality', 'Green Spaces Accessibility']
# Define measures
measures = ['dwellings/ha', 'number', '%', '%',
            '%','%','%',
            'μg/m³','μg/m³', '%', 'number',
            '%','%']
# Associations domanin: indicators
dom_ind_dict = {
    domains[0]: indicators[0:4],
    domains[1]: indicators[4:7],
    domains[2]: indicators[7:11],
    domains[3]: indicators[11:13]
}

# List of London cities to be excluded
london_cities = ['UK128C1', 'UK129C1','UK130C1','UK131C1','UK132C1','UK133C1','UK107C1','UK108C1','UK109C1','UK110C1',
                 'UK111C1','UK112C1','UK113C1','UK101C1','UK102C1','UK103C1','UK104C1','UK105C1','UK106C1',
                 'UK120C1','UK121C1','UK122C1','UK123C1','UK124C1','UK125C1','UK126C1','UK114C1','UK115C1',
                 'UK116C1','UK117C1','UK118C1','UK119C1','UK127C1']

# List of cities to be excluded due to lack of values in the lcz dataset
exclude_cities = ['UK023C1', 'ES008C1', 'ES029C1','MT001C1', 'ES025C1', 'NO006C1', 'PT004C1', 'ES072C1', 'ES045C1', 'PT007C1',
                'ES055C1', 'ES074C1', 'ES524C1','ES550C1','ES557C1', 'IS001C1'] 

# List of cities to be excluded due to lack of values in the osm dataset
exclude_osm = ['LT003C1', 'EE002C1', 'LT004C1', 'LT501C1', 'LT502C1', 'EE001C1','LT002C1', 'LV002C1', 'EE003C1', 'LV501C1', 
                'LV003C1', 'LV001C1','LT001C1']

#-------------------------------------------------------------------------------------------
# Functions to be used in the data_cleaning.ipynb
def cities(df):
    """
    Remove cities of London from the dataframe.
    
    Parameters:
    df (DataFrame): The input dataframe containing city data.
    
    Returns:
    DataFrame: The dataframe with London cities removed.
    """
    df_new = df[~df['urau_code'].isin(london_cities)]
    return df_new


def cities2(df):
    """
    Remove cities that lack values in the lcz and osm datasets.
    
    Parameters:
    df (DataFrame): The input dataframe containing city data.
    
    Returns:
    DataFrame: The dataframe with specified cities removed.
    """
    df = df[~df['urau_code'].isin(exclude_cities)]
    df = df[~df['urau_code'].isin(exclude_osm)]
    return df

def extract_first_name(name):
    """
    Extract the first part of the city name, remove accents, and replace special characters.
    
    Parameters:
    name (str): The original city name.
    
    Returns:
    str: The cleaned city name.
    """
    if '/' in name:
        first_name = name.split('/')[0].strip()
    else:
        first_name = name.strip()

    # Remove portion within parentheses
    first_name = re.sub(r'\(.*?\)', '', first_name).strip()
    # Remove accents and replace special characters
    first_name = unidecode(first_name)
    # Remove symbols using regular expressions
    first_name = re.sub(r'[^\w\s]', '', first_name).strip()
    # Split by whitespace and keep only the first word
    first_name = first_name.replace(' ', '_')

    return first_name

def new_name(df):
    """
    Apply the extract_first_name function to the 'urau_name' column of the dataframe.
    
    Parameters:
    df (DataFrame): The input dataframe containing city data.
    
    Returns:
    DataFrame: The dataframe with cleaned city names.
    """
    df['urau_name'] = df['urau_name'].apply(extract_first_name)
    df['urau_name'] = df['urau_name'].dropna()
    return df

#-------------------------------------------------------------------------------------------
# Functions to be used to see the statistics of data/indicators

def statistics(df,val,name):
# Create a mapping dictionary for the clusters
    cluster_mapping = {
        'large metropolitan': 'Large metropolitan',
        'metropolitan': 'Metropolitan',
        'medium': 'Medium',
        'small': 'Small',
        'small towns': 'Small towns'
    }

    # Calculate summary statistics for PMmean by cluster with new names
    summary = df.groupby('cluster')[val].describe()

    # Create a DataFrame with the desired format and new cluster names
    summary_table = pd.DataFrame([
        {
            'Variable': name,
            'Cluster': cluster,
            'Mean': stats['mean'],
            'Std': stats['std'],
            '25%': stats['25%'],
            '75%': stats['75%'],
            'Max': stats['max'],
            'Min': stats['min']
        }
        for cluster, stats in summary.iterrows()
    ])
    # Apply the mapping to the dataframe
    summary_table['Cluster'] = summary_table['Cluster'].map(cluster_mapping)
    # Round all numeric columns to 3 decimal places
    numeric_columns = ['Mean', 'Std', '25%', '75%', 'Max', 'Min']
    summary_table[numeric_columns] = summary_table[numeric_columns].round(2)
    summary_table.to_excel(f'results\\data\\{name}_stat.xlsx', engine="openpyxl", index=False)
    return summary_table


#-------------------------------------------------------------------------------------------
# Methods to be used in the indicators_creation.ipynb

def rescaling_dwellings(df, val_df, new_col, target_val):
    """
    Rescale dwelling values in a DataFrame based on specified criteria.
    """
    df_dwelling = df.copy()
    df_dwelling['val_log'] = np.log1p(df_dwelling[val_df])
    df_dwelling['threshold'] = 'no provided'
    df_dwelling.loc[
        (df_dwelling['val_log'] >= np.log(45)) & 
        (df_dwelling['val_log'] <= np.log(175)), 
        'threshold'
    ] = 'provided'
    
    prov = df_dwelling[df_dwelling['threshold'] == 'provided']
    noprov = df_dwelling[df_dwelling['threshold'] == 'no provided']

    max_val = noprov['val_log'].max()
    min_val = noprov['val_log'].min()
    max_val1 = noprov[noprov['val_log'] < np.log(45)]['val_log'].max()
    max_val2 = noprov[noprov['val_log'] > np.log(175)]['val_log'].min()

    # Rescale values outside the optimal range
    noprov.loc[noprov['val_log'] < np.log(45), new_col] = np.interp(
        noprov.loc[noprov['val_log'] < np.log(45), 'val_log'],
        [min_val, max_val1],
        [0, target_val]
    )
    noprov.loc[noprov['val_log'] >= np.log(45), new_col] = np.interp(
        noprov.loc[noprov['val_log'] >= np.log(45), 'val_log'],
        [max_val2, max_val],
        [target_val, 0]
    )

    # Gaussian rescaling for 'prov'
    peak_value = 10
    sigma = 10
    mu = None
    
    if len(prov) > 0:
        if mu is None:
            mu = min(prov['val_log'], key=lambda x: abs(x - np.log(100)))
        
        scaling_factor = np.exp(-((prov['val_log'] - mu)**2) / (2 * sigma**2))
        prov[new_col] = target_val + (peak_value - target_val) * scaling_factor
    
    # Combine both datasets
    df2 = pd.concat([prov, noprov], ignore_index=True)
    
    # Ensure the final columns are selected correctly
    df2 = df2[['gid', 'urau_code', 'urau_name', 'pop_final', val_df, new_col, 'cluster']]
    
    return df2

