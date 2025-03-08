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
- **data:** Contains the data after cleaning in `1_data_cleaning_final.ipynb`. In particular:
   - *all_cities.shp*: boundary of all the 917 cities (containing geometry column)
   - *london_cities.gpkg* : cities contained in the greater cities of london - this file is used only in the UHI calculation (containing geometry column)
   - *gdf_pop.geojson* : population at 250mx250m grid resolution for each city (containing geometry column)
   - *grid_pop* : population dataset
   - *grid_pop0* : population dataset including grids wit pop=0
   - *df_dwellings.csv : file containing the dwelling density for all the 917 cities
   - *df_lcz.csv* : file containing low to mid rise developments for all the 917 cities
   - *df_imd.csv* : file containing the permeability for all the 917 cities
   - *df_osm.csv : file containing the walkability and cyclability for all the 917 cities, this file was split into: *df_walk.csv* and *df_cycle.csv*
   - *df_pubtrans.csv* : file containing the bus stops for all the 917 cities
   - *df_ndvi.csv* : file containing the ndvi for all the 917 cities
   - *df_ndvi_target_tabla.csv* : file containing the target ndvi for all the 917 cities
   - *df_ap*: file containing the air pollution values, it is divided in *df_no2.csv* and *df_pm.csv* 
   - *df_uhi.csv* : file containing the urban heat island values for all the 917 cities
   - *df_300m.csv* : file containing the 300m green accessibility data for all the 917 cities
   - *df_2km.csv* : file containing the 2km green accessibility data for all the 917 cities

- **external_dataset:** Contains datasets used for `5_additional_analysis.ipynb`.
   - *df_green.csv*: green spaces dataset
   - *merged_share_cyclaway.csv*: mode share data from Mueller et al. https://doi.org/10.1016/j.ypmed.2017.12.011 
   - *NO2_measurements_airbase.csv*: NO2 data from airbase datasete: https://www.eea.europa.eu/data-and-maps/ data/aqereporting-8#tab-figures-produced
   - *PM25_measurements_airbase.csv*: PM2.5 data from airbase dataset: https://www.eea.europa.eu/data-and-maps/ data/aqereporting-8#tab-figures-produced

- **new_data:** Contains one folder for each cluster, each containing two folders:
  - **grid:** Contains indicators at grid level computed in `2_indicators_creation.ipynb`.
  - **city:** Contains indicators at city level computed in `2_indicators_creation.ipynb`.

### results
- **data:** Contains results from `3_indicators_analysis.ipynb`.
- **indicators:** Contains all the indicators created in `2_indicators_creation.ipynb`. It contains:
   - *data1.csv:* indicators data at city level
   - *data2.csv:* indicators data at grid cell level
- **df_rank_domain.csv:** Pivot dataset with domains as columns
- **df_rank_rescaled.csv:** Pivot table where indicators are represented as columns, with their corresponding rescaled values.
- **df_rank_val.csv:** Pivot table where indicators are represented as columns, with their corresponding absolute values.
- **df_website.xlsx:** Dataset created for the HUDI website with df_rank_rescaled.csv and df_rank_val.csv merged
- **HUDI_domains.csv:** HUDI and domains
- **HUDI_summary.csv:** Summary of HUDI across the clusters
- **gdf_plot_qgis.shp:** Boundary of all cities associated with HUDI values 

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
