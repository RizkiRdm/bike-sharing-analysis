# Bike Sharing Analysis

## Background 

This is a first project analysis to understand about data analysis, there are many problem in this case, but i'm chose 5 case :
- How weather affects to bicycle rentals
- What is the percentage increase / decrease of bicycles rentals during weekends and weekdays?
- Identify peak hours bicycle rentals every day
- how tren bicycle rentals in 2011 to 2012
 
## Data Set

Bike-sharing rental process is highly correlated to the environmental and seasonal settings. For instance, weather conditions,
precipitation, day of week, season, hour of the day, etc. can affect the rental behaviors. The core data set is related to  
the two-year historical log corresponding to years 2011 and 2012 from Capital Bikeshare system, Washington D.C., USA which is 
publicly available in http://capitalbikeshare.com/system-data. We aggregated the data on two hourly and daily basis and then 
extracted and added the corresponding weather and seasonal information. Weather information are extracted from http://www.freemeteo.com. 

if you guys interested what about a visualization, don't worry, i have a basic dashboard that i build using streamlit.
here's the link : https://bike-sharing-analysis-mxdcuhxlgdu93zb26imj9d.streamlit.app/

or 

you can copy this repository.

and follow the instruction below : 

### Bike sharing dashboard

#### Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

#### Setup Environment - Shell/Terminal
```
git clone git@github.com:RizkiRdm/bike-sharing-analysis.git
cd bike-sharing-analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```

#### Run steamlit app
```
streamlit run dashboard/main.py
```
