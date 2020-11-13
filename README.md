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

---


### The aim of this project was:
 * To better understand which protests were successful based on whether or not a protest received accommodations 
 * To create a predictive model for classifying a successful protest


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

## Engineered Features

Since there were seven different demands and seven different responses, we used ...**JLW to finish**



*** other features go here

#### Protest Duration & Total Days
We wished to have a clearer image of the duration of an individual protest.  The original values for indexing time were specific to the original publishers of the dataset, and required some transformation for features that would relate to elapsed time. The original features based on time consisted of "start" and "end" values for each day of a month, month of a year, and actual year.  Differences between each start and end day, month or year were calculated as new featres titled "days," "months" and "years". A final "total_days" feature was calculated by multiplying the three features by the approximate number of days in their given units, two examples here:
df['months'] = df['endmonth'] - df['startmonth']
df['total_days'] = df['days'] + (df['months']*30.5) + (df['years']*365)

PLEASE NOTE: Inconsistencies would be present in this feature if, for example, the start and end day occur in different months, likewise in different years.  Most protests had a duration of less than one month and we can therefore be confident that the "total_days" result is not significantly damaged. We ask users to consider this feature as an approximate and not exact measure of protest duration.



---
# General Workflow/ Methodology

---

## Step 1 - Import Data and do general cleaning

DESCRIBE FURTHER (potentially copy/past intro from notebooks)


## Step 2 - EDA on entire dataset and individual regions

DESCRIBE FURTHER (potentially copy/past intro from notebooks)


## Step 3 - Modeling on individual regions

DESCRIBE FURTHER (potentially copy/past intro from notebooks)


---
# Analysis

---

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
* tbd.....
* tbd.....
![](location of key plot)

### Europe
* tbd.....
* tbd.....
![](location of key plot)

### MENA
* tbd.....
* tbd.....
![](location of key plot)

### South America
* tbd.....
* tbd.....
![](location of key plot)



## Modeling  - Highlights

### Africa
* tbd.....
* tbd.....
![](location of key plot)

### Asia
* tbd.....
* tbd.....
![](location of key plot)

### Europe
* tbd.....
* tbd.....
![](location of key plot)

### MENA
* tbd.....
* tbd.....
![](location of key plot)

### South America
* tbd.....
* tbd.....
![](location of key plot)



### Limitation of Data   
* Did not find source that combines SAT and ACT data for student test takers, so I had to make assumptions to calculate the total number of test takers.
* There's a negative correlation between the two and many states have a dominant test that most students take.  So I assumed the higher value of test taking percent as the total test takers for a given state (so where states have more of a mix in test this undercounts the total percent of test takers).
![](image?)

![](image?)

---
# Conclusions/ Next Steps

---

### Conclusion
* We were not able to gain an insight on the features that predict a successful protest
* None of our modeling was able to significantly predict protest accomodations over baseline


### Recommendations
* Combine our work on regional data across the entire data set
* Time series analysis
* Combining these data with data on the rise of different forms of social media and technology
* And ...


![](image?)




