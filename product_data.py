#requests module will allow you to send HTTP/1.1 requests using Python. With it, you can add content like headers, form data, multipart files, and parameters via simple Python libraries. It also allows you to access the response data of Python in the same way
import requests
#json module is used to convert the python dictionary into a JSON string that can be written into a file. It will convert strings to Python datatypes, normally the JSON functions are used to read and write directly from JSON files.
import json
#csv module implements classes to read and write tabular data in CSV format

from parse import product_details

#User defined function for extracting a portion of string from a given string.
def get_str(resp_str,frm_str,to_str):
    start_index = resp_str.find(frm_str)+ len(frm_str)
    end_index = resp_str.find(to_str, start_index)
    resp_dict = resp_str[start_index:(end_index)]
    return resp_dict

#User defined function for extracting a portion of string from a given string.
def get_json_from_strpage(resp_str,frm_str,to_str):
    start_index = resp_str.find(frm_str) + len(frm_str)
    end_index = resp_str.find(to_str) + len(to_str)
    resp_dict = resp_str[start_index:end_index]
    return resp_dict

#All men Tshirt-Category List Page url
Men_TShirt_url = "https://www.myntra.com/men-tshirts?src=sNav"

Men_TShirt_url_headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Host": "www.myntra.com",
    "Referer": "https://www.myntra.com/shop/men",
    "Connection": "keep-alive",
    "Accept-Language": "en-US,en;q=0.9"
}

Men_TShirt_List_page_resp = requests.get(Men_TShirt_url, headers=Men_TShirt_url_headers, timeout=20)

with open("Men_TShirt_List_page_resp.html", 'w', encoding='utf-8') as file:
   file.write(Men_TShirt_List_page_resp.text)

Men_TShirt_resp_List_page_dict = get_str(Men_TShirt_List_page_resp.text, '"results":', ',"seo":')


with open("Men_TShirt_resp_List_page_dict.html", 'w', encoding='utf-8') as file:
    file.write(Men_TShirt_resp_List_page_dict)

with open("Men_TShirt_resp_List_page_dict.html") as f:
    data = json.loads(f.read())


Total_No_pages = 2
# Total_No_pages = 2  # For testing upto 2 listpages

productDetails = {}

i = 1  # product count for Header

#Creating list to store all the product categories
categories = ['men-tshirts','men-casual-shirts','men-formal-shirts','men-sweatshirts','men-sweaters',
              'men-jackets','men-blazers','men-suits','men-jeans','men-casual-trousers','men-formal-trousers',
              'mens-shorts','men-trackpants','men-briefs-and-trunks','men-boxers','men-innerwear-vests','men-nightwear',
              'men-thermals','women-jeans','tops','women-trousers','women-shorts-skirts','women-sweaters-sweatshirts',
              'women-shrugs','women-jackets-coats','women-blazers-waistcoats','women-sportswear-clothing','bra','women-briefs','women-clothing-shapewear',
              'women-loungewear-and-nightwear','women-swimwear','camisoles-and-thermals']

#iterate through all the categories and store the product description in the sample.json file 
for category in categories:
    
    for lp_page in range(1, Total_No_pages):
        
        ##Hitting all List Pages 
        Men_TShirt_url = "https://www.myntra.com/"+category + "?p=" + str(lp_page)
        Men_TShirt_url_headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
            "Host": "www.myntra.com",
            "Referer": "https://www.myntra.com/shop/men",
            "Connection": "keep-alive",
            "Accept-Language": "en-US,en;q=0.9"
        }
        #obtain the correct page list,data and url
        Men_TShirt_List_page_resp = requests.get(Men_TShirt_url,headers = Men_TShirt_url_headers,  timeout = 20)

        with open("Men_TShirt_List_page_resp" + str(lp_page) + ".html", 'w', encoding='utf-8') as file:
            file.write(Men_TShirt_List_page_resp.text)

        Men_TShirt_resp_List_page_dict = get_str(Men_TShirt_List_page_resp.text,'"results":',',"seo":')

        with open("Men_TShirt_resp_List_page_dict" + str(lp_page) + ".html", 'w', encoding='utf-8') as file:
            file.write(Men_TShirt_resp_List_page_dict)

        with open("Men_TShirt_resp_List_page_dict" + str(lp_page) + ".html") as f:
            data = json.loads(f.read())

        #For each product in the each page, get the metadata product description
        for product in data['products']:
            Product_url = product['landingPageUrl']
            Product_url = 'https://www.myntra.com/' + Product_url
            product['landingPageUrl'] = Product_url
            product_detail = product_details(product['landingPageUrl'])
            productDetails[product['landingPageUrl']] = product_detail
#Dump all the product descriptions in the sample.json file
with open("sample.json", "w") as outfile:
    json.dump(productDetails, outfile)


        