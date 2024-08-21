import traceback
import random
import json

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.mmsonline.com"
URL = BASE_URL + '/suppliers'


session = requests.Session()


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.perplexity.ai/',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
}


def get_response(page_no='1', retry=3):
    params = {
        'sort': 'CmpGroupName_asc',
        'isFeaturedOnly': 'true',
        'page': page_no,
    }
    random.randint(1, 5)
    response = session.get(URL, params=params, headers=headers)
    if response.status_code != 200 and retry > 0:
        return get_response(page_no, retry=retry-1)
    
    else:
        return response


def extract_supplier_details(article):
    # Extracting Supplier Name
    supplier_name_tag = article.find('h2')
    supplier_name = supplier_name_tag.get_text(strip=True) if supplier_name_tag else None

    # Extracting Supplier Link
    supplier_link_tag = supplier_name_tag.find('a') if supplier_name_tag else None
    supplier_link = supplier_link_tag['href'] if supplier_link_tag else None

    # Extracting Location (City, State)
    location_tag = article.find('span', class_='fw-bold')
    location = location_tag.get_text(strip=True) if location_tag else None

    # Extracting Description
    description_tag = article.find('p')
    description = description_tag.get_text(strip=True) if description_tag else None

    # Extracting Social Media Links
    social_media_links = []
    social_media_tags = article.find_all('a', class_='company-social-link')

    for tag in social_media_tags:
        link = tag['href']
        social_media_links.append(link)
    # Returning the extracted details as a dictionary
    return {
        "Supplier Name": supplier_name,
        "supplier_link": BASE_URL + supplier_link,
        "Location": location,
        "Description": description,
        'social_media_links': social_media_links
    }


def extract_articles(response):
    soup = BeautifulSoup(response.content, 'html.parser')
    div = soup.find('div', {'class': 'product-companies-list'})
    articles = div.find_all('article')
    data = []    
    for article in articles:
        dt = extract_supplier_details(article)
        data.append(dt)

    return data

def export_data(dictionary, file_path="data1.json"):
    with open(file_path, 'a') as json_file:
        json.dump(dictionary, json_file, indent=4)

def extract_details():
    try:
        for no in range(1, 20):
            response = get_response(str(no))
            data = extract_articles(response)
            export_data(data)

    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == "__main__":
    extract_details()