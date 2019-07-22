import re

class BasePage:
## BasePage Class holds list of urls for reviews, base url, # reviews, avg rating

    
    def __init__(self, driver, url):
        self.urls_list=[]
        self.driver = driver
        self.base_url = url
        driver.get(self.base_url)
        self.all_info=[]
        self.title_=''

# when basePage class is declared  something = new BasePage()
# init runs, driver and url are now available to class and driver is getting base_url

# basepageattributes populates the urls or reviews for putting through SearchPageResults    
# self object also gains total review and avg rating integers   
    def BasePageAttributes(self):
        overall_info = self.driver.find_element_by_class_name("biz-rating-very-large")
        total_rating = overall_info.find_element_by_class_name("i-stars").get_attribute("title")
        total_reviews= overall_info.find_element_by_class_name("review-count").text
        self.total_reviews = int(re.sub("[^0-9]", "",total_reviews))
        self.total_rating = int(re.sub("\D.","",total_rating))
        
        title_elements = self.driver.find_elements_by_class_name('biz-page-title')
        for elem in title_elements:
          if len(self.title_) > 0:
            self.title_ = self.title_ + '_' + elem.text
          else:
            self.title_ = self.title_ + elem.text
        num_urls = int(self.total_reviews/20)+1
        for i in range(num_urls):
            new_url = self.base_url + "?start=" + str(i*20)
            self.urls_list.append(new_url)



### Search Page Results 

class SearchPageResults(BasePage):

  def __init__(self, BasePage):
    self.driver = BasePage.driver
    self.review_info_list = []
    self.user_info_list = []

  def review_user_info(self):
    review_users = self.driver.find_elements_by_class_name("user-passport-stats")
    review_info = self.driver.find_elements_by_class_name("review-content")
    
    for info in review_info:
      rating = info.find_elements_by_class_name("i-stars")[0].get_attribute("title")
      date = info.find_elements_by_class_name("rating-qualifier")[0].text
      text = info.find_elements_by_tag_name("p")[0].text
      review_stats = [rating,date,text]
      self.review_info_list.append(review_stats)  
    
    for user in review_users:
      user_info_elements = user.find_elements_by_tag_name("li")
      user_info = [ x.text for x in user_info_elements]
      if len(user_info)==2:
        user_info.append("0 photos")

      if len(user_info)==3:
        user_info.append("Not Elite")
      self.user_info_list.append(user_info)  
