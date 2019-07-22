from selenium import webdriver
import re
import numpy as np
import pandas as pd
import PageClasses as P

driver = webdriver.Chrome(r'C:\Users\310nutrition\Desktop\NYC_DSA\chromedriver\chromedriver.exe')

related_restaurants = ["https://www.yelp.com/biz/yakitori-totto-new-york", 
                      "https://www.yelp.com/biz/soba-totto-new-york",
                       "https://www.yelp.com/biz/nonono-new-york-6",
                       "https://www.yelp.com/biz/yakitori-taisho-new-york",
                       "https://www.yelp.com/biz/donburiya-new-york-2",
                       "https://www.yelp.com/biz/yakitori-tora-new-york",
                       "https://www.yelp.com/biz/ootoya-chelsea-new-york",
                       "https://www.yelp.com/biz/torishin-new-york-3",
                       "https://www.yelp.com/biz/sakagura-new-york",
                       "https://www.yelp.com/biz/yopparai-new-york"]

for res in related_restaurants:

	Main = P.BasePage(driver,res)
	Main.BasePageAttributes()

	for url in Main.urls_list:
		if url!= (Main.base_url+"?start=0"):
			Page = P.BasePage(driver, url)
			Results = P.SearchPageResults(Page)
			Results.review_user_info()
			Main.all_info = Main.all_info + [[Main.title_] +Results.review_info_list[i]+Results.user_info_list[i] for i in range(len(Results.review_info_list))]
		else: 
			Results = P.SearchPageResults(Main)	
			Results.review_user_info()
			Main.all_info = Main.all_info + [[Main.title_] +Results.review_info_list[i]+Results.user_info_list[i] for i in range(len(Results.review_info_list))]
	
	df=pd.DataFrame(Main.all_info, columns = ["title","rating", "date", "text","friends", "review_num","photos","Status"])
	df.to_csv((Main.title_+".csv"))

driver.close()
