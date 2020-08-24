import requests
import re
import json
from bs4 import BeautifulSoup

NEWS_URLS = {
    "The Hindu" : "https://www.thehindu.com/",
    "Deccan Herald": "https://www.deccanherald.com/"
}

def get_news():
    print("Collecting news..")

    #webscrape some websites
    news_map = scrape_deccan_herald()
    #print("------------------- NEWS -------------------------------")
    #for link, headline in news_map.items():
    #    print(link, headline)
    #print("---------------------------------------------------------")
    return news_map

def scrape_timesofindia():
    URL  = ""

def scrape_deccan_herald():
    print("Scraping Deccan herald...")
    MAIN_URL = "https://www.deccanherald.com/"
    page = requests.get(MAIN_URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    news_map = {} #hyper link: news text

    all_urls = soup.find_all("a", href=re.compile("(?i)corona|covid")) #ignore case
    all_urls = list(set(all_urls)) #remove duplicates
    for url in all_urls:
        sub_url = url['href']
        sub_page = requests.get(MAIN_URL + sub_url)
        sub_soup = BeautifulSoup(sub_page.content, 'html.parser')
        news_content = sub_soup.find_all("script",type="application/ld+json")
        for news in news_content:
            news_content_json = json.loads(news.text) #this is json
            if 'articleBody' in news_content_json.keys() and 'headline' in news_content_json.keys():
                news_map.update({ MAIN_URL+sub_url : news_content_json['headline']})

    if len(news_map) == 0:
        print("Deccan herald: No news found!")
    from pdb import set_trace
    #set_trace()
    for k, v in news_map.items():
        print("--------------------")
        print("key:", k)
        print("value:", v)

    return news_map

if __name__ == "__main__":
    get_news()
