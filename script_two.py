import traceback
import random
import json

import requests
from bs4 import BeautifulSoup


BASE_URL = "https://www.iqsdirectory.com/"
URL = BASE_URL + 'cnc-machining/cnc-machining-2/'


session = requests.Session()


headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8',
    'cache-control': 'max-age=0',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://www.iqsdirectory.com/',
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


def get_response(retry=3):
    random.randint(1, 5)
    response = session.get(URL, headers=headers)
    if response.status_code != 200 and retry > 0:
        return get_response(retry=retry-1)
    else:
        return response


def extract_supplier_details(li):
    # Extracting Supplier Name
    supplier_name_tag = li.find('span', itemprop='name')
    supplier_name = supplier_name_tag.get_text(strip=True) if supplier_name_tag else None

    # Extracting Supplier Website
    supplier_website_tag = li.find('a', itemprop='url')
    supplier_website = supplier_website_tag['href'] if supplier_website_tag else None

    # Extracting Location (City, State)
    location_tag = li.find('span', itemprop='addressLocality')
    location = location_tag.get_text(strip=True) if location_tag else None

    # Extracting Phone Number
    phone_number_tag = li.find('a', itemprop='telephone')
    phone_number = phone_number_tag.get_text(strip=True) if phone_number_tag else None

    # Extracting Company Profile Link
    company_profile_link_tag = li.find('a', title="Aaero Swiss Profile")
    company_profile_link = company_profile_link_tag['href'] if company_profile_link_tag else None
    if company_profile_link:
        company_profile_link = BASE_URL + company_profile_link.replace('../', '')
    # Extracting Company Description
    company_description_tag = li.find('p', itemprop='description')
    company_description = company_description_tag.get_text(strip=True) if company_description_tag else None
    return {
        "Supplier Name": supplier_name,
        "supplier_link": supplier_website,
        "Location": location,
        "phone_number": phone_number,
        "Description": company_description,
        'company_profile_link': company_profile_link
    }


def export_data(dictionary, file_path="data2.json"):
    with open(file_path, 'a') as json_file:
        json.dump(dictionary, json_file, indent=4)


def extract_details():
    try:
        response = get_response()
        soup = BeautifulSoup(response.content, 'html.parser')
        ul = soup.find('ul', {'class': 'adlist_ul'})
        l = soup.find_all('li')
        for li in l:
            data = extract_supplier_details(li)
            export_data(data)

    except Exception as e:
        print(e)
        traceback.print_exc()


if __name__ == "__main__":
    extract_details()