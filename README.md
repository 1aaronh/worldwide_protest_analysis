# Analyzing Protests throughout the world where the State gives accommodations
---

# File Structure
---
### Files:
* README.md - describes file
* [Presentation.pdf](update location***************) 
    - presentation in pdf form  

### Folders:
* code - folder includes files for running the analysis
   * Step 1 - import/clean data
   * Step 2 - EDA on worldwide data
   * Step 2a - EDA on Africa data
   * Step 2b - EDA on Asia data
   * Step 2c - EDA on Europe data
   * Step 2d - EDA on MENA data
   * Step 2d - EDA on South America data
   * Step 3a - Modeling on Africa data
   * Step 3b - Modeling on Asia data
   * Step 3c - Modeling on Europe data
   * Step 3d - Modeling on MENA data
   * Step 3d - Modeling on South America data

* data - folder includes data used for the analysis
   * mmALL_073119_csv.csv
     - original file       
   * xxx.csv
     - description of file
   * xxx.csv
     - description of file

* images:
   * screenshots used for README file
 
---
# Background
---
This data set consists of descriptions of protests throughout the world.

These description come from four primary sources:
 * New York Times 
 * Washington Post 
 * Christian Science Monitor 
 * Times of London

For regions in the middle east/North Africa, the other primary source was:
 * Jerusalem Post

Per the **Users Manual** that comes with the data [here]():

> "The search is restricted to newspaper sources – it proceeds as follows.
> First, search for the four terms above in a country, over a year in four primary sources:
> * New York Times Washington Post Christian Science Monitor Times of London
> In MENA, consider these four sources plus the Jerusalem Post.
>  
> If these sources return more than 100 articles, then proceed in searching the articles for evidence of codeable protest events. If these four sources do not return at least 100 articles, then expand the search to include regional and other sources. Proceed with coding protest events. Note that sometimes even this more source-inclusive search will not return 100 articles – in this case, add wire-reports to the search – then code appropriate protest events regardless of total articles returned."
    
The data includes protests from 1990 to 2019 in 166 countries.  It consists of 16,363 rows. The number of entries where protests occurred is 14,514 (1849 rows do not indicate where a protest occured.  It appears that these are included for the sake of time-series models so that almost each country has an entry for each year - whether or not protests occurred).

---
# Problem Statement
#### What are the factors that contribute to a successful protest? How do these factors vary by region or country? Can we reliably predict a successful protest outcome?
---

### The aim of this project was:
 * To better understand which protests were successful based on whether or not a protest received accommodations.
 * To identify patterns and characteristics of which types of protests and locations had a given response by the state.
 * To create a predictive model for classifying a successful protest.

---
# Data Dictionary
---

The **Users Manual** includes a data dictionary [here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt).  We describe key highlights from the data dictionary below, along with features that we engineered:

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

Since there were seven different demands and seven different responses, we used ...**JLW to finish**

**JENN

#### Protest Duration & Total Days
We wished to have a clearer image of the duration of an individual protest.  The original values for indexing time were specific to the original publishers of the dataset, and required some transformation for features that would relate to elapsed time. The original features based on time consisted of "start" and "end" values for each day of a month, month of a year, and actual year.  Differences between each start and end day, month or year were calculated as new featres titled "days," "months" and "years". A final "total_days" feature was calculated by multiplying the three features by the approximate number of days in their given units, two examples here:
* df['months'] = df['endmonth'] - df['startmonth']
* df['total_days'] = df['days'] + (df['months']*30.5) + (df['years']*365)

PLEASE NOTE: Inconsistencies would be present in this feature if, for example, the start and end day occur in different months, likewise in different years.  Most protests had a duration of less than one month and we can therefore be confident that the "total_days" result is not significantly damaged. We ask users to consider this feature as an approximate and not exact measure of protest duration.

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
    - Support Vector Classifier
    
* Standard Classification Metrics were measured, consisting of a Confusion Matrix, ROC Curves and the ratios for true and false positives and negatives.
* Each accuracy score was evaluated against the baseline accuracy for its respective region.

---
# Analysis
* The two classes were significantly imbalanced for the entire dataset and by each individual region.
* All models struggled to distinguish between classes as a result, with many having true positive counts of or near 0.
* Depending on the given region, baseline accuracy measures were around 87-93%
* A few models had higher test scores than baseline with only modest overfitting.
* Many models had tradeoffs of better metrics but higher variance or visa versa.
* One key takeaway from the imbalanced classes is that there are simply not many observations of a state having an accomodating response to protest activity.
-----

## EDA  - Highlights

### Entire Dataset
* tbd.....
* tbd.....
![](location of key plot)

### Africa
* tbd.....
* tbd.....
![](location of key plot)

### Asia
![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/Asia_avg_duration_num_protesters.png)

![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/Asia_country_year_stateresponse.png)

### Europe
* tbd.....
* tbd.....
![](location of key plot)

### MENA
![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/MENA_avg_country_duration.png)

![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/MENA_avg_country_duration.png)

### South America
* tbd.....
* tbd.....
![](location of key plot)
----

## Modeling  - Highlights

### Africa
* tbd.....
* tbd.....
![](location of key plot)

### Asia
![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/Asia_ada_metrics.png)

### Europe
* tbd.....
* tbd.....
![](location of key plot)

### MENA
![](https://git.generalassemb.ly/1aaronh/Group_Project_Boo-Leans/blob/master/images/MENA_DTree.png)

### South America
* tbd.....
* tbd.....
![](location of key plot)

-----
# Conclusions/ Next Steps
--------
### Conclusion
* We were not able to gain an insight on the features that predict a successful protest
* None of our modeling was able to significantly predict protest accomodations over baseline


### Recommendations
* Combine our work on regional data across the entire data set
* Time Series Analysis
* Combining these data with data on the rise of different forms of social media and technology
* And ...
