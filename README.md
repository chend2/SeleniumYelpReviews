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
 
![Figure_1](https://user-images.githubusercontent.com/14852897/61604742-c0772a00-ac10-11e9-8b03-74525d90c3cc.png)
![Figure_2](https://user-images.githubusercontent.com/14852897/61604748-c40ab100-ac10-11e9-8c0c-ccfa52d586e2.png)
![Figure_3](https://user-images.githubusercontent.com/14852897/61604749-c40ab100-ac10-11e9-8087-0ae1c2e6ee0b.png)
![Figure_4](https://user-images.githubusercontent.com/14852897/61604750-c40ab100-ac10-11e9-968a-ee565b8f81c6.png)
![Figure_5](https://user-images.githubusercontent.com/14852897/61604751-c40ab100-ac10-11e9-8480-bedf3082669a.png)
![Figure_9](https://user-images.githubusercontent.com/14852897/61604752-c40ab100-ac10-11e9-92f4-8f6255333590.png)
![Figure_10](https://user-images.githubusercontent.com/14852897/61604753-c4a34780-ac10-11e9-9769-cee60548d9d3.png)
![Figure_6](https://user-images.githubusercontent.com/14852897/61604754-c836ce80-ac10-11e9-954f-a71d3a792b46.png)
