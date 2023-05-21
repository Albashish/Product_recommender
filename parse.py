from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Chrome("C:/chromedriver")
from selenium.webdriver.common.by import By
Prod_page_url_headers = {
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
                "Host": "www.myntra.com",
                "Referer": "https://www.myntra.com/men-tshirts",
                "Connection": "keep-alive",
                "Accept-Language": "en-US,en;q=0.9"
            }
#Function to get the product description when the link for that product is given as an argument
#Here product description also contains the material, size, specifications etc.
def product_details(link):
    driver.get(link)
    content = driver.page_source
    #parse the page data using Beautiful soup
    soup=BeautifulSoup(content,"html.parser")
    tempString=""
    productDetails={}

    for y in soup.find_all("div",attrs={'class':'pdp-description-container'}):
        for i in (y.find('div',attrs={"class":"pdp-productDescriptors"})).find('div',attrs={'class':'pdp-productDescriptorsContainer'}).find_all('div'):
            if i.find('h4') is not None:
                    #print(i.find('h4').text)
                    if i.find('p') is not None:
                        productDetails[i.find('h4').text]=i.find('p').text
                        #print(productDetails[i.find('h4').text])
                    else:
                        #print("Class of the calue: ",i.get('class'))
                        if i.get('class')[0]=='index-sizeFitDesc':
                            try:
                                element=driver.find_element(By.CLASS_NAME,"index-showMoreText")
                            except:
                                element=None 
                            
                            if element is not None:
                                # print("Inside")
                                elements=driver.find_elements(By.CLASS_NAME,"index-row")
                                tempString='"'
                                for element in elements:
                                    tempString+=element.find_element(By.CLASS_NAME,"index-rowKey").text+':'+element.find_element(By.CLASS_NAME,"index-rowValue").text+','
                                tempString+='"'
                                productDetails[i.find('h4').text]=tempString
                                #print(tempString)
                                tempString=""
                            else:
                                elements=driver.find_elements(By.CLASS_NAME,"index-row")
                                tempString='"'
                                for element in elements:
                                    tempString+=element.find_element(By.CLASS_NAME,"index-rowKey").text+':'+element.find_element(By.CLASS_NAME,"index-rowValue").text+','
                                tempString+='"'
                                productDetails[i.find('h4').text]=tempString
                                #print(tempString)
                                tempString=""
                        else:    
                            productDetails[i.find('h4').text]=i.text                    
    return productDetails
