from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

def scrape_info():
    browser = init_browser()
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    res = soup.find('div', class_='slide')

    
    #results ={}
    # Identify and return title of listing
    #results["news_title"] = soup.find('div', class_='content_title').text
    news_title = res.find('div', class_='content_title').text.strip()

    # Identify and return price of listing
    #results["news_p"] = soup.a.text
    news_p = res.a.text.strip()
   


    #####################################
    browser = init_browser()
    urln = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    url_i='https://www.jpl.nasa.gov'
    browser.visit(urln)
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    

    categories = soup.find('div',class_='sm:object-cover object-cover')
    image = categories.find('img')['src']
    #results["image"]=url_i + {image}
    #image = url_i + image

    
    ######################################
    mars_url='https://space-facts.com/mars/'
    tables = pd.read_html(mars_url)
    mars_df=tables[0]
    mars_df.columns=['','Mars']
    #results["table"]=mars_df.to_html()
    table=mars_df.to_html()
    #####################################

    ######################################
    hem_url='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hem_url) 


    images = browser.find_by_css("a.product-item h3")
    hemisphere_image_url=[]



    for i in range(len(images)):
        url_info={}
        browser.find_by_css("a.product-item h3")[i].click()
        cat_info=browser.links.find_by_text('Sample').first
        url_info['title']=browser.find_by_css('h2.title').text
        url_info['link_url'] = cat_info['href']
        hemisphere_image_url.append(url_info)
        browser.back()
    


    
    results={
        "news_title":news_title,
        "news_p":news_p,
        "image":image,
        "table":table,
        
       


    }


    return results
