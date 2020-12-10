# The script extracts all the tweets of a particular company

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

# Create instance of web driver
option = webdriver.ChromeOptions()
option.add_argument('--headless')
#option.add_argument('user-agent=whatever you want')
driver = webdriver.Chrome(options=option)



def get_data(input_company):
	'''
	To get all the tweets
 	Input : Company name for which we want the tweets
	Scrolls the page and get all the tweets
	Returns List of urls of the tweets
	'''
	# Redirect to company page
	url = "https://twitter.com/search?q=%40" + input_company + "&src=recent_search_click"
	driver.get(url)


	# Required variables
	tweet_urls=[]
	screen_height = driver.execute_script("return window.screen.height")
	scrolling = True
	no_of_scroll = 1
	tweet_ids = set()
	sleep(random.randint(2,5))


	# To get 100 tweets by scrolling the page
	while scrolling:
		get_tweet_links(tweet_urls,tweet_ids)
		driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=no_of_scroll))
		no_of_scroll=no_of_scroll+1
		sleep(random.randint(1,3))
		scroll_height = driver.execute_script("return document.body.scrollHeight")

		if (screen_height) * no_of_scroll > scroll_height or len(tweet_urls) >= 15:
			break

	print(tweet_urls)
	print(len(tweet_urls))
	return tweet_urls

#
def get_tweet_links(tweet_urls,tweet_ids):
	'''
	Function to fetch all the urls and append it in tweet_urls
	Input : tweet_urls is the final list of tweets which get_data function will return and tweet_ids is set to avoid duplicate entries of tweet
	Appends the urls in tweet_urls and return to the calling function
	'''
	try:
		tweet_cards=driver.find_elements_by_xpath('/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div')
		for card in tweet_cards:
			try:
				link = card.find_element_by_xpath('./div/div/article/div/div/div/div[2]/div[2]/div[1]/div/div/div[1]/a').get_attribute('href')
				if link:
					tweet_id = ''.join(link)
					if tweet_id not in tweet_ids:
						tweet_ids.add(tweet_id)
						tweet_urls.append(link)
			except:
				print("Link not found!!")
	except:
		print("Tweet Card not found!!")
