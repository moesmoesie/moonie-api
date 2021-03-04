from os import name
from time import time

def create_income_statements_link(company_symbol,fields=None):
    ''' Returns link for extracting data of company income statements on Yahoo Finance'''

    if fields == None:
        with open("data/income_statement_fields.txt") as parameter_file:
            fields = [value.strip() for value in parameter_file.readlines()]
        
    base_url = f"https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{company_symbol}?"
    currentTimeStamp = str(time()).split(".")[0]    

    fields_parameters = f"type={','.join(fields)}"
    date_parameters = f"&period1=493590046&period2={currentTimeStamp}"
    domain_parameters = f"&corsDomain=finance.yahoo.com"

    full_url = base_url + fields_parameters + date_parameters + domain_parameters
    return full_url

if __name__ == '__main__':
    link = create_income_statements_link("GOOG")


def create_stock_price_link(company_symbol):
    ''' Returns link for extracting data of company stock data on Yahoo Finance'''

    currentTimeStamp = str(time()).split(".")[0]    
    full_url = f"https://query1.finance.yahoo.com/v7/finance/download/{company_symbol}?period1=860371200&period2={currentTimeStamp}&interval=1d&events=history&includeAdjustedClose=true"

    return full_url

if __name__ == '__main__':
    link = create_stock_price_link("GOOG")
    print(link)