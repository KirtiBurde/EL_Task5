# EL_Task5
**1. Importing Required Libraries**

The following Python libraries were imported for data analysis and visualization:

import pandas as pd        # For data manipulation and analysis
import numpy as np         # For numerical operations
import seaborn as sns      # For data visualization
import matplotlib.pyplot as plt  # For plotting graphs

These libraries are essential for handling datasets, performing statistical operations, and creating visual insights.

**2. Loading the Dataset**

df = pd.read_csv('../DataSets/SHOES.csv')

The dataset named SHOES.csv was loaded into a pandas DataFrame named df. This dataset contains sales-related information for various shoe products across different regions and stores.

**3. Previewing the Dataset**

Upon loading, the first few and last few rows were displayed, showing a total of 395 rows and 7 columns. The columns in the dataset are:

Region: The geographical area (e.g., Africa, Western Europe)

Product: The type of shoe product (e.g., Sandal, Men's Dress)

Subsidiary: The subsidiary office or location (e.g., Addis Ababa, Rome)

Stores: Number of stores selling that product

Sales: Revenue generated (in USD)

Inventory: Value of inventory (in USD)

Returns: Value of product returns (in USD)

Data Cleaning and Structure Validation

**4. Checking Data Types and Null Values**

df.info()

The df.info() function provides a concise summary of the DataFrame, including:

Total entries: 395

Column names and non-null counts

Data types of each column


Insight:
All columns contain 395 non-null values, meaning there are no missing values. However, some columns like 'Sales', 'Inventory', and 'Returns' are currently of type object, which suggests that these values may contain formatting (e.g., dollar signs, commas) that prevents them from being interpreted as numerical data.


---

**5. Data Cleaning: Converting Columns to Numeric**

df['Sales'] = df['Sales'].str.replace(',', '').str.replace('$', '').astype(float)
df['Inventory'] = df['Inventory'].str.replace(',', '').str.replace('$', '').astype(float)
df['Returns'] = df['Returns'].str.replace(',', '').str.replace('$', '').astype(float)

This block cleans and converts the following columns from string (object) type to float:

Sales

Inventory

Returns


Steps taken:

str.replace(',', ''): Removes commas (e.g., "29,761" → "29761")

str.replace('$', ''): Removes dollar signs

.astype(float): Converts cleaned string to numerical (float) type


Result:
These financial columns can now be used for mathematical operations, statistical summaries, and plotting.

**6. describe()**
This will give the basic statistics of all the numeric columns.
Numeric columns are: Stores
                     
                     Sales

                     Inventory

                     Return
The basic statistics it explains that are: Count                     

                                           Mean

                                           std

                                           min

                                           25%

                                           50%

                                           75%

                                           max

**7. Finding the value counts:**

1. Region

code: df.Region.value_counts()

It show that which region hs how much values.

Shows the values highest to the lowest.

output:

Western Europe               62
Africa                       56
South America                54
Pacific                      45
United States                40
Canada                       37
Central America/Caribbean    32
Eastern Europe               31
Middle East                  24
Asia                         14

2. Product

code: df.Product.value_counts()

output:

Boot              52
Slipper           52
Sport Shoe        51
Women's Dress     51
Men's Dress       50
Sandal            49
Men's Casual      45
Women's Casual    45

3. Subsidiary

code: df.Subsidiary.value_counts()

output:

Addis Ababa     8
Chicago         8
Canberra        8
Jakarta         8
Kuala Lumpur    8
Manila          8
Buenos Aires    8
Caracas         8
La Paz          8
Montevideo      8
Sao Paulo       8
Los Angeles     8
Al-Khobar       8
Minneapolis     8
New York        8
Seattle         8
Copenhagen      8
Geneva          8
Heidelberg      8
Lisbon          8
London          8
Paris           8
Dubai           8
Tel Aviv        8
Warsaw          8
Managua         8
Cairo           8
Khartoum        8
Seoul           8
Montreal        8
Prague          8
Toronto         8
Vancouver       8
Kingston        8
Rome            8
Mexico City     8
San Juan        8
Budapest        8
Bogota          7
Luanda          7
Algiers         7
Auckland        7
Kinshasa        7
Santiago        7
Moscow          7
Ottawa          7
Singapore       6
Nairobi         6
Calgary         6
Madrid          6
Johannesburg    5
Bangkok         5
Tokyo           1


**8. HEATMAP**

This heatmap shows the correlation matrix of four key business variables: Returns, Inventory, Sales, and Stores. It was generated using Python's Seaborn library in a Jupyter Notebook.

Interpretation of the Heatmap

Each cell in the heatmap represents the Pearson correlation coefficient between two variables, which ranges from -1 (perfect negative correlation) to +1 (perfect positive correlation). The color scale helps visually identify the strength of the relationships:

Dark Red (close to 1) = Strong positive correlation

Blue (closer to 0) = Weak or no correlation


 Key Insights from the Heatmap

Variables	Correlation Coefficient	Insight

Returns & Sales	 0.96	Very strong positive correlation – higher sales tend to result in more returns.

Returns & Inventory	0.90	Very strong positive correlation – high inventory levels are linked with higher returns.

Sales & Inventory	0.95	Very strong positive correlation – higher inventory supports higher sales.

Stores & Returns	0.41	Moderate correlation – more stores might contribute to more returns.

Stores & Sales	0.42	Moderate correlation – more stores are generally associated with more sales.

Stores & Inventory	0.48	Moderate correlation – more stores likely require more inventory.


Conclusion for the Report

The heatmap indicates strong interdependence among Returns, Sales, and Inventory, suggesting that any strategic decisions in one of these areas are likely to affect the others. The number of Stores shows a moderate correlation with the rest, indicating its impact is present but not as strong.

This correlation analysis can help guide decisions such as optimizing inventory levels, forecasting returns, or evaluating store performance.


**9. PAIRPLOT**


A pairplot is a visualization tool from the seaborn library that shows:

Scatter plots for each pair of numerical variables.

Histograms (or KDE plots) on the diagonal for individual variables.


Variables in Your Plot

From your image, the columns being compared are:

Stores

Sales

Inventory

Returns


 How to Read It

Each cell shows a plot between two variables:

Diagonal: Distribution of a single variable.

Bottom-left to top-right triangle: Scatter plots showing how two variables relate.


1. Stores vs Sales

Observation: There's a clear positive linear correlation between the number of stores and sales.

Insight: More stores lead to higher sales. This suggests that geographical expansion (more stores) directly contributes to increased revenue.

Action: Consider investing in more store locations in underperforming regions.

2. Sales vs Inventory

Observation: There is a positive trend, though slightly scattered.

Insight: Higher sales are associated with higher inventory levels. This is typical for successful regions or products that require frequent restocking.

Action: Optimize inventory levels to avoid overstocking while ensuring product availability in high-sales zones.

3. Inventory vs Returns

Observation: Strong positive correlation.

Insight: More inventory leads to more returns. This could be due to:

Overstocking leading to unsold, expired, or damaged goods.

High product availability increasing chances of returns.


Action: Analyze product-specific return reasons. Implement stricter quality control or return policy changes.

4. Sales vs Returns

Observation: Moderate to strong positive relationship.

Insight: As sales increase, returns also increase. This is expected but also suggests that:

Popular products may have quality or sizing issues.

Higher sales channels (like online) might have looser return policies.


Action: Monitor return rates (% of sales) to identify problematic products or sellers.

 5. Stores vs Returns

Observation: Positive relationship.

Insight: More stores mean more customer interactions and hence more returns.

Action: Ensure customer service and return processes are efficient across all store locations.

6. Distributions (on the diagonal)

Skewness is present in all variables:

Most stores have low values, with a few high outliers.

Sales, Inventory, and Returns are all right-skewed.


Insight: There are a few high-performing stores or products driving the bulk of the business.

Action: Consider log transformation for predictive models; also analyze top-performing SKUs or stores for best practices.

 Overall Business Insight

> The business is growth-oriented: expansion in stores leads to higher sales, which increases inventory needs and returns. But operational costs (inventory, returns) also rise. Balancing growth with efficiency is key.


**10. HISTPLOT**

X-axis (Count): Number of records (e.g., transactions, entries, or data points).

Y-axis (Region): Various regions such as:

Africa

Asia

Canada

Central America/Caribbean

Eastern Europe

Middle East

Pacific

South America

United States

Western Europe



This chart tells you how many records (or rows) exist for each region in your dataset.


Observations & Insights

Region	Insight

Western Europe	Has the highest number of records. Possibly the largest market in dataset.
Africa	Also has a high count, slightly less than Western Europe.
Asia, Middle East	Have moderate record counts.
Canada, Central America	Have fewer entries than most regions.
Asia	Surprisingly low count, may need to explore why (missing data or underperformance).
South America, U.S.	Both show medium-to-high representation.

Possible Interpretations

1. Data Distribution:

Your data is not equally distributed across regions.

Some regions are more represented (e.g., Western Europe) than others (e.g., Asia).



2. Market Size or Coverage:

Regions with more entries may represent larger markets, more transactions, or better data availability.

Less-represented regions may be underserved or under-analyzed.



3. Need for Normalization:

When comparing sales, returns, etc., normalize by count or population to avoid bias toward regions with more entries.

Business Use-Cases

Prioritization: Focus on regions with more data for deeper analysis.

Gap Identification: Asia's lower count could mean potential for growth or data collection improvements.

Reporting: Use this plot in executive dashboards to highlight data coverage. 


**11. SCATTER PLOT**

**1.**

 Scatter Plot Explanation: Inventory vs Sales

This scatter plot (from your Jupyter notebook cell) visualizes:

X-axis: Inventory (number of units available)

Y-axis: Sales (total sales amount)

Region: Appears to include all data (no filtering like in the previous chart)


Code used:

sns.scatterplot(x=df.Inventory, y=df.Sales)
plt.show()


Key Observations:

Feature	Description

Positive Correlation	A clear upward trend: as inventory increases, sales also tend to increase.
Clustered Data	Most data points are clustered between 0 and 1 million for inventory and 0 to 0.6 million for sales.
Outliers	A few data points have very high inventory (above 2 million) and very high sales (above 1 million), indicating bulk stock/sales for some regions/products.
Linear Trend	The pattern looks roughly linear, meaning more inventory generally leads to higher sales (to a limit).


Business Insights:

1. Balanced Inventory Drives Sales

Increasing inventory does lead to increased sales up to a point.

Having enough stock is critical for meeting demand and maximizing revenue.



2. Diminishing Returns After a Point

Beyond ~2 million in inventory, sales growth slows, indicating overstocking doesn’t guarantee proportional sales growth.



3. High Performers Should Be Studied

The few data points with high sales and high inventory may represent successful products or regions. Consider duplicating their strategy elsewhere.



4. Forecasting Opportunity

A predictive model (e.g., linear regression) could be built to predict sales based on inventory with reasonably high accuracy due to the clear trend.

**2.**

Explanation of the Scatter Plot

From the image, we can interpret the following:

Axes:

X-axis (Returns): This represents the monetary value or quantity of product returns.

Y-axis (Sales): This represents the corresponding sales value.


Each dot on the scatter plot represents a data point, i.e., a sales transaction with its associated returns.


 Key Observations

1. Positive Correlation (with a ceiling):

The plot shows a general upward trend — as sales increase, returns also tend to increase.

This suggests that higher sales volumes typically result in higher return values (which is expected in real-world scenarios).



2. Clusters of Points:

There is a dense cluster of data points in the lower left corner (Sales < 400,000 and Returns < 10,000).

This indicates that most transactions are relatively low in both sales and returns.



3. Outliers:

A few points appear far right (high returns) or high up (high sales).

For example, one point has extremely high returns (~60,000), which may be an anomaly or special case worth investigating.

Insights and Actionable Conclusions

1. High Sales = High Returns Trend:

There is a direct relationship between sales and returns. This could mean your return rate is proportional to your sales volume.

Consider calculating the return rate (%) to analyze product performance more precisely.



2. Outliers Detection:

Investigate the outliers — especially transactions with very high returns. These may indicate:

Faulty product batches

Customer dissatisfaction

Errors in data entry or billing


**12. BOX PLOT** 

Explanation of the Box Plot

This updated box plot visualizes the distribution of four variables:

Stores

Sales

Inventory

Returns


Each vertical box plot shows how values are spread out for that particular variable.


 Interpretation of Each Variable

1. Stores

The values are very low, mostly clustered around zero.

Very little variability, and no significant outliers.

Interpretation: This could be a count or ID field. If it's count data, most products seem to be linked with few stores.

2. Sales

Moderate spread in the box (middle 50%).

A large number of outliers on the higher end.

Interpretation: Most sales values are relatively low, but there are some products or regions with extremely high sales — these may be driving overall revenue.

3. Inventory

The widest box with many extreme outliers.

The highest variability among all features.

Interpretation: There are major differences in inventory levels — possibly due to different product types or demand patterns. Some products have extremely high stock levels that may need optimization.

4. Returns

Very tight box near zero, with a few outliers.

Most values are small, indicating returns are generally low.

Interpretation: Returns are controlled for most products, but a few cases of high returns could signal quality or customer satisfaction issues.

 Key Insights

1. High Variability in Inventory and Sales:

These two features show strong dispersion and many outliers.

Suggests that some products or stores are overstocked or extremely high-performing.

These values may skew KPIs and require segmentation.


2. Returns Are Low But Worth Watching:

Despite being small overall, the presence of outliers in returns calls for root cause analysis (e.g., poor product quality, regional issues).


3. Inventory Optimization Opportunity:

Consider reducing inventory on low-performing products or redistributing stock based on demand.


4. Skewed Distributions:

All variables except Stores are right-skewed — meaning a log transformation may help with normalization if you're applying machine learning or statistical models.

**13. Finding outliers in Inventory column**

Explanation of the Boxplot
The image shows a Jupyter Notebook displaying a boxplot, likely created using pandas or matplotlib in Python. The boxplot visualizes four variables from a dataset:

Stores

Sales

Inventory

Returns

Each of these variables is represented as a separate boxplot, allowing for a comparison of their distributions.

Boxplot Elements:

The central line in each box represents the median value.

The box edges represent the first (Q1) and third (Q3) quartiles.

Whiskers extend to show the range within 1.5 times the interquartile range (IQR) from the quartiles.

Dots outside the whiskers indicate outliers.

Insights from the Boxplot
Stores:
The distribution is tightly clustered, with a small IQR and few outliers. This suggests that most products/subsidiaries have a similar number of stores, with only a few exceptions.

Sales:
The boxplot for sales is more spread out, indicating greater variability. There are several outliers on the higher end, suggesting that while most products have moderate sales, a few have exceptionally high sales.

Inventory:
Inventory also shows a wide spread and a significant number of outliers, indicating that some products or subsidiaries maintain much higher inventory levels than the majority. This could point to overstocking or anticipation of high demand for certain items.

Returns:
Returns have a very tight distribution with a small box and a few outliers. This suggests that most products have low return rates, but a few experience unusually high returns, which may warrant further investigation.

Key Observations
Presence of Outliers:
All four variables show outliers, particularly sales and inventory, indicating some products or subsidiaries significantly deviate from the norm.

Variability:
Sales and inventory are more variable compared to stores and returns. This could reflect differences in product popularity, stocking strategies, or demand fluctuations.

Operational Insights:

High sales outliers could represent best-selling products or successful marketing campaigns.

High inventory outliers may indicate overstocking or slow-moving products.

High return outliers could point to product quality issues or mismatched customer expectations.

Data Quality:
The presence of outliers suggests the need for further analysis, such as investigating the causes or considering data transformation or filtering steps for modeling.

Storing the index index in a variable
 o = o.index

 Displaying the indexes
 o
  The output displays the indices stored in o which are collection of integer row indices: 
  index are([ 16,  21,  99, 101, 103, 106, 108, 111, 114, 179, 182, 185, 187, 192,
       193, 210, 232, 294, 295, 297, 318, 321, 324, 339, 353, 361])

Removing the rows from the DataFrame
df = df.drop(labels=o)
This will remove the rows containing outliers in the DataFrame with this drop fuction.

df
This line shows the DataFrame after cleaning and removing the outliers.
