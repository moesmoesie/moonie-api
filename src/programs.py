import pandas as pd
from src.links import create_income_statements_link
from time import sleep
from src.web import download_page_json

def download_income_statements(company_symbols = None, fields=None):
    with open("data/company_symbols.txt") as company_symbols_file:
            company_symbols = [value.strip() for value in company_symbols_file.readlines()]
    
    for company_symbol in company_symbols:
        link = create_income_statements_link(company_symbol, fields=fields)
        succes = download_page_json(link,f"data/income-statements/{company_symbol}.json")
        if succes:
            print(f"Succesfully downloaded the income statements of {company_symbol}")
        else:
            print(f"Failed to download the income statements of {company_symbol}")
        sleep(2.5)
            
if __name__ == '__main__':
    download_income_statements()