import requests
import json
import csv

def get_page_content(url):
    response = make_request(url)

    if response.status_code != 200:
        return None
    
    return response.content

def get_page_json(url):
    response = make_request(url)
    if response.status_code != 200:
        return None

    try:
        return response.json()
    except:
        return None

def download_page_json(url,path):
    response = make_request(url)
    if response.status_code != 200:
        return None

    try:
        with open(path, 'w') as outfile:
            data = response.json()
            json.dump(data, outfile,indent=4)
        return response.json()
    except:
        return None

def download_page_csv(url,path):
    response = make_request(url)
    if response.status_code != 200:
        return None

    try:
        with open(path, 'w') as outfile:
            decoded_content = response.content.decode('utf-8')
            outfile.write(decoded_content)
        return True
    except:
        return None


def make_request(url):
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0"
    }

    response = requests.get(url,headers=header)
    return response