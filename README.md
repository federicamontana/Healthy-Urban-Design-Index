# Healthy Urban Design Index (HUDI)

The HUDI provides a large-scale, open data-driven and policy-relevant measure of spatial urban health indicators related to the broad domains of Urban Design, Sustainable Transportation, Environmental Quality and Green Space Accessibility, across nearly 1,000 European cities of varying sizes. 
This repository contains a series of Jupyter notebooks used for analyzing 13 urban indicators. The results of these analyses are included in the main text of the paper and the supplementary materials.

## Notebooks

### 1. Data Cleaning
- **File:** `1_data_cleaning_final.ipynb`
- **Description:** This notebook is used for cleaning and preprocessing the raw data.

### 2. Indicators Creation
- **File:** `2_indicators_creation.ipynb`
- **Description:** This notebook is used to create the 13 urban indicators from the cleaned data.

### 3. Indicators Analysis
- **File:** `3_indicators_analysis.ipynb`
- **Description:** This notebook is used to analyze the created indicators. The results of these analyses are included in the supplementary materials.

### 4. Main Analysis
- **File:** `4_main_analysis.ipynb`
- **Description:** This notebook contains the main analysis of the indicators, included in the main text and supplementary material.

### 5. Additional Analysis
- **File:** `5_additional_analysis.ipynb`
- **Description:** This notebook contains additional analyses and sensitivity analysis, using external datasets.

### 6. Geo Plots
- **File:** `6_geo_plots.ipynb`
- **Description:** This notebook is used to generate geographical plots for visualizing the indicators.

## Directory Structure

### DATA
- **data0:** Contains the original data.
- **data:** Contains the data after cleaning in `1_data_cleaning_final.ipynb`.
- **external_dataset:** Contains datasets used for `5_additional_analysis.ipynb`.
- **new_data:** Contains one folder for each cluster, each containing two folders:
  - **grid:** Contains indicators at grid level computed in `2_indicators_creation.ipynb`.
  - **city:** Contains indicators at city level computed in `2_indicators_creation.ipynb`.

### results
- **data:** Contains results from `3_indicators_analysis.ipynb`.
- **indicators:** Contains all the indicators created in `2_indicators_creation.ipynb`.

### PLOTS
- **data:** Contains plots for data created in `4_main_analysis.ipynb`.
- **domains:** Contains plots regarding domains created in `4_main_analysis.ipynb`.
- **grids:** Contains plots regarding grids created in `4_main_analysis.ipynb`.
- **indicators:** Contains plots regarding indicators created in `4_main_analysis.ipynb`.
- **geo:** Contains geographic plots of indicators created in `6_geo_plots.ipynb`.
- **top_bottom:** Contains top and bottom indicators created in `4_main_analysis.ipynb`.
- **spiderplot:** Contains spider plots created in `4_main_analysis.ipynb`.

## Utility Scripts

### Utility Functions
- **File:** `utility.py`
- **Description:** This script contains utility functions used across the notebooks.

## How to Use

1. **Clone the repository:**
   ```sh
   git clone https://github.com/federicamontana/Healthy-Urban-Design-Index
   ```

2. **Install the required packages:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Run the notebooks:**
   Open the notebooks in Jupyter and run the cells sequentially to perform the data cleaning, indicator creation, and analysis.

## Installation

To install the required packages, run:
```sh
pip install -r requirements.txt
```

## Requirements

The `requirements.txt` file includes the following packages:
```
pandas
geopandas
matplotlib
numpy
seaborn
contextily
scipy
statsmodels
joblib
unidecode
libpysal
re
splot 
esda
```

## Results
The results of the analyses are saved in the `results` directory and the plots are saved in the `plots` directory.

## Author
Federica Montana

## License
This project is licensed under the MIT License.

