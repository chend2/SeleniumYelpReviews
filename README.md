# SeleniumYelpReviews

The goal of this project was to utilize data visualization tools to generate figures that one could use to better 
understand the relationship between a set of variables collected from the yelp reviews of each restaurant. 

Selenium was used to scrape the review information off of each site. The data was manipulated using Pandas
and stored in CSVs at multiple points between downloading, processing, and visualizing to limit the number of times 
the scraper had to be used, lowering the risk of detection. 

Some visualizations were made with Pandas/Maplotlib/Seaborn, examining the relationship of ratings, user information, 
and review information. Natural language processing was done to generate N-grams based on review rating. 

At this time significant clean up work still has to be done for refactoring and labelling. 
There are still quite a few plots in Selenium still to be generated that could provide valuable insight to users 
and restaurant owners alike. 

The end goal of this project is to create an application in which users can enter an input that could be used to query
 the yelp search bar, the application would scrape the first ten restaurants returned and all of their results, and 
 generate significantly greater insights and visualizations for the user. Additionally, it could help inform 
 restaurant owners and provide actionable feedback based on the aggregated reviews. 
 
