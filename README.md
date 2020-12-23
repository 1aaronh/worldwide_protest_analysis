# Analyzing Protests throughout the world where the State gives accommodations
---
*This project is the result of contributions from Julia Christensen, Aaron Hume, Ignacio Real & Jennifer Wlliamson.*

# File Structure
---
### Files:
* README.md - describes file
* Protest outcomes.pdf - presentation in pdf form  

### Folders:
* code - folder includes files for running the analysis
   * Notebook 1 - import/clean data
   * Notebook 2 - EDA on worldwide data
   * Notebook 2a.1 - EDA on Africa data
   * Notebook 2a.2 - Modeling on Africa data
   * Notebook 2b - EDA on Asia data
   * Notebook 2c - EDA on Europe data
   * Notebook 2d - EDA on MENA data
   * Notebook 2e - EDA on South America data
   * Notebook 2f - EDA on worldwide data, part 2
   * classification.py - python file that contains functions that we reference in other notebooks
   
* data - folder includes data used for the analysis
   * mmALL_073119_csv.csv
     - original file    
   * MM_users_manual_0515.pdf
     - data dictionary and user manual  
   * base_df.csv
     - output from notebook 1
   * df_all.csv
     - output from notebook 2
   * df_categories.csv
     - output from notebook 2
     
* images:
   * screenshots used for README file
 
---
# Background
---
This data set consists of descriptions of protests throughout the world from the [mass mobilization project](https://massmobilization.github.io) website.

These description come from four primary sources:
 * New York Times 
 * Washington Post 
 * Christian Science Monitor 
 * Times of London

For regions in the middle east/North Africa, the other primary source was:
 * Jerusalem Post

Per the **Users Manual** that comes with the data:

> "The search is restricted to newspaper sources – it proceeds as follows.
> First, search for the four terms above in a country, over a year in four primary sources:
> * New York Times Washington Post Christian Science Monitor Times of London
> In MENA, consider these four sources plus the Jerusalem Post.
>  
> If these sources return more than 100 articles, then proceed in searching the articles for evidence of codeable protest events. If these four sources do not return at least 100 articles, then expand the search to include regional and other sources. Proceed with coding protest events. Note that sometimes even this more source-inclusive search will not return 100 articles – in this case, add wire-reports to the search – then code appropriate protest events regardless of total articles returned."
    
The data includes protests from 1990 to 2019 in 166 countries.  It consists of 16,363 rows. The number of entries where protests occurred is 14,514 (1849 rows do not indicate where a protest occured.  It appears that these are included for the sake of time-series models so that almost each country has an entry for each year - whether or not protests occurred).

---
# Problem Statement
---

### The aim of this project was:
 * To better understand which protests were successful based on whether or not a protest received accommodations.
 * To identify patterns and characteristics of which types of protests and locations had a given response by the state.
 * To create a predictive model for classifying a successful protest.

---
# Data Dictionary
---

The **Users Manual** includes a data dictionary [here](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/data/MM_users_manual_0515.pdf).  We describe key highlights from the data dictionary below, along with features that we engineered:

## Data from the Users Manual
***Protestor Demands***
The data includes seven types of demands that protests could have (see data dictionary link for full description of each type):
 * labor wage dispute
 * land farm issue
 * police brutality
 * political behavior, process  
 * price increases, tax policy  
 * removal of politician        
 * social restrictions          

Up to four of these are coded for each protest in columns (protesterdemand1 to protesterdemand4).  If fewer than four demands occurred, we found that a ```.``` was entered for that cell.
 
***State Responses***
The data includes seven types of responses that state could have (see data dictionary link for full description of each type):
 * accomodation
 * arrests
 * beatings
 * crowd dispersal  
 * ignore  
 * killings        
 * shootings          

Up to seven of these are coded for each protest in columns (stateresponse1 to stateresponse7).  If fewer than seven responses occurred, we found that a ```.``` was entered for that cell.

***region***
The data includes 8 regions generally corresponding to continents:
 * Asia
 * Europe
 * Africa
 * Middle East & North Africa (MENA)
 * South America
 * North America
 * Central America
 * Oceania
 
These individual regions became the basis for member specific analysis to compare and contrast the patterns in protest activity as well as evaluate different models. North America, Central America and Oceania were ignored for modeling purposes due to them having limited observations of protests.

## Engineered Features

#### Protest Demands (group of 7 columns) & Protest Responses (group of 7 columns)

**Note: A function to do this is in the classification.py file**
Create a one-hot encoded column for each of either the 4 protest demand columns or 7 state response columns.  Since there are seven types of protest demands (and state responses) that can occur, rows where no protests occurred (so the demands/responses are 999 - we think these were included for time series analysis, see readme for further discussion), and rows where a few demands/responses were recorded but not the maximum of 4 demands and 7 responses, there were 9 different possible entries in any given cell for demands/responses. In addition, in a few of the categories not all 9 entries occurred out of the entire columns, so when one-hot encoding, the resulting dataframe for that column would have fewer than 9 columns.

To allow the one-hot encoded data frame for each of the demands to be added together (to get the total times that any given demand occurred for a given row), and similarly for the response columns, this function uses concatenation and other techniques so that each dataframe becomes the same size and the output is a dataframe of the nine different demands, and then a dataframe of nine different responses - where the entry in a given column notes how often that particular demand/response occured with a given protest.

This allows someone to easily check whether accommodations occurred by looking at one column, rather than seven different response columns.

 * Add 7 new columns - one each for the 7 types of protester demands (indicating when a particular demand occurred for a protest) - 'labor wage dispute','land farm issue','police brutality','political behavior, process','price increases, tax policy','removal of politician','social restrictions'
 * Add 7 new columns - one each for the 7 types of state responses (indicating when a particular response occurred for a protest) - 'accomodation','arrests','beatings','crowd dispersal','ignore','killings','shootings'

Note that a few times, the entries are greater than 1 - indicating that more than one protest demand column or more than one state response column included the same demand/response.  We did not get a chance to look into this, but this could be pursued in the future (on whether this was intentional or a mistake).

#### State Violence
Add a column that indicates whether state violence occured with a protest (whether beatings, shootings, or killings occurred with the protest)
* violent_responses = ['beatings','killings','shootings']
* for response in violent_responses:
*    df['state_violence'] = df_state_response_group[response]

#### Protest Demands - all combos & Protest Responses - all combos
Add a column for demands with entries that include all combinations of demands that occurred in the dataframe (using a 7-digit number with 1/0's to indicate the presence of a given type of demand)
 * 'protesterdemand'
Add a column for responses with entries that include all combinations of responses that occurred in the dataframe (using a 7-digit number with 1/0's to indicate the presence of a given type of response)
 * 'stateresponse'

#### Protest Duration & Total Days
We wished to have a clearer image of the duration of an individual protest.  The original values for indexing time were specific to the original publishers of the dataset, and required some transformation for features that would relate to elapsed time. The original features based on time consisted of "start" and "end" values for each day of a month, month of a year, and actual year.  Differences between each start and end day, month or year were calculated as new featres titled "days," "months" and "years". A final "total_days" feature was calculated by multiplying the three features by the approximate number of days in their given units, two examples here:
* df['months'] = df['endmonth'] - df['startmonth']
* df['total_days'] = df['days'] + (df['months']*30.5) + (df['years']*365)

PLEASE NOTE: Inconsistencies would be present in this feature if, for example, the start and end day occur in different months, likewise in different years.  Most protests had a duration of less than one month and we can therefore be confident that the "total_days" result is not significantly damaged. We ask users to consider this feature as an approximate and not exact measure of protest duration.

### Protestdemands & Stateresponses
Each protest can have multiple demands and government responses. Two separate columns were create to count the total of demands and responses for each individual event. The total of demands can range between 1 - 4 for one event, while responses range between 1 - 7 for one event. 
* edf['protestdemands'] = edf[['protesterdemand1','protesterdemand2','protesterdemand3','protesterdemand4']].count(axis = 1)
* edf['stateresponses'] = edf[['stateresponse1','stateresponse2','stateresponse3','stateresponse4','stateresponse5','stateresponse6','stateresponse7']].count(axis = 1)

---
# General Workflow/ Methodology
---
## Step 1 - Import Data and do general cleaning

* Null values were either removed or filled by 0 or 999.
* Features that had clear irrelevance such as country code were dropped.
* We chose to additionally drop the sources and notes features and rely on the discrete and continuous features for our analysis.
* General patterns in the categorical features of region, country, participants_category, protester_demand, and state_response were discovered with groupby nd value_counts Pandas methods.
* There was a significant amount of rows in the original dataset that had null values because they represented a point in time where no protest occurred. We chose to abandon these rows for our analysis by using a boolean filter for when the "protest" feature was equal to 1.
* Separate Pandas DataFrames were created for each specific region in advance of more precise analysis.
* Most features native to the dataset were discrete or categorical and were encoded as a result. Remaining continuous features considered relevant for modeling and analysis were not adjusted.

## Step 2 - EDA on entire dataset and individual regions

* Region specific analysis was divided among different team members.
* Chronological and color coded line charts were produced to show intensity of protest activity by region over time. Color coding was by both demand and state response.
* Bar charts were produced for basic averages of protest duratoin or total protests that were then grouped by country and year.
* Total state response category was analyzed worldwide to show that the most common response to a protest is "ignore" followed by "crowd dispersal." This category was also measured region by region.
* The above methods were applied on the entire dataset and by each geographic region.



## Step 3 - Modeling on individual regions

* The target feature selected for classification was the engineered and encoded 'accomodation'
* Train Test Split was used for model instantiation and fitting.
* SciKit Learn's GridSearchCV was used with generous ranges of hyper-parameters to idenfity a best performing model.
* Pipelines were also used to facilitate scaling and other transformations of the data.
* The classification models selected were:
    - Logistic Regression
    - Decision Tree
    - K Nearest Neighbors
    - Random Forest
    - Bootstrapped Aggregator
    - Support Vector Machine
    
* Standard Classification Metrics were measured, consisting of a Confusion Matrix, ROC Curves and the ratios for true and false positives and negatives.
* Each accuracy score was evaluated against the baseline accuracy for its respective region.
* **NOTE**: The classes were reblanced using imblearn's SMOTE for the Asia and MENA regions. The models performed significantly better after rebalancing and this is verified by the metrics for these specific regions.

---
# Analysis
* The two classes were significantly imbalanced for the entire dataset and by each individual region.
* Depending on the given region, baseline accuracy measures were around 87-93%
* A few models had higher test scores than baseline with only modest overfitting.
* Many models had tradeoffs of better metrics but higher variance or visa versa.
* One key takeaway from the imbalanced classes is that there are simply not many observations of a state having an accomodating response to protest activity.
* All models struggled to distinguish between classes as a result, with many having true positive counts of or near 0.
* This pattern changed dramatically for the Asia and MENA regions that were modeled with synthetic rebalancing of classes for experimentation.
-----

## EDA  - Highlights

### Entire Dataset
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Africa_EDA.png)
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Demands_over_time_world.png)
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Responses_over_time_world.png)

### Africa
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Africa_EDA.png)

### Asia
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Asia_avg_duration_num_protesters.png)

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Asia_country_year_stateresponse.png)

### Europe
* Protests in Europe were on a rise after 2013, peaking during 2018
* Political issues were the catalysts of majority of the protests, especially in the Ukraine, UK, France, Germany, and Ireland
* Labor wage dispute, and tax policy were the second and third most common protests in Europe
* Approximately 60% of the protests are ignored, 20% end with crowd dispersal, and only 5% are accommodated
* Although accommodations make up 5% of government responses, on average, protests with the longest duration (4 days) are accommodated

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/ir_duration_resp.png)

### MENA
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/MENA_avg_country_duration.png)

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/MENA_total_protests_country.png)

### South America
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/SA_%20State_reactions_count.png)
----

## Modeling  - Highlights

### Africa
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Africa_confusion_matrix.png)

### Asia
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Asia_randomforest_metrics.png)

### Europe
* A logistic regression model predicting the likelihood of 1 (Accommodation) for any given protests or 0 (No Accommodation)
* Features considered were month, year, country, count of demands and responses, and duration, protestor violence
* Accuracy results were 95%, which were aligned with baseline (95%)
* Sensitivity was 0%, revealing the model was not able to predict positive outcomes  
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/ir_bi_conmatrix.png)

### MENA
* SMOTE significantly improved model results with this region.  The Random Forest delivered the best metircs.
![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/MENA_randomforest_metrics.png)

### South America

* The Support vector machine had was the most accurately performing model for the South America region for binary classification and failed to improve over baseline as seen in the confusion mtrix below:

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/SA_SVM.png)

* When using multiclass classification the Logistic Regression performed the best for the South America region and was able to improve over baseline. Though the accuracy score appears to be worse than in the binary classification model the improvement over baseline demonstrates that balancing out the classes would likely improve accuracy in these models.

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/SA_multiclass_metrics.png)

-----
# Conclusions/ Next Steps
--------
### Conclusion
* We were not able to gain an insight on the features that predict a successful protest
* None of our modeling was able to significantly predict protest accomodations over baseline
* Best way to predict Accommodations is based on the region rather than any of our models - since the models performed poorly

![](https://github.com/1aaronh/worldwide_protest_analysis/blob/master/images/Accomodations_by_region.png)

### Recommendations
* Combine our work on regional data across the entire data set
* Time Series Analysis
* Combining these data with data on the rise of different forms of social media and technology
* And the dataset is very rich and could answer many more questions.
