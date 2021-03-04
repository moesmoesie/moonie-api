from time import time



def create_income_statements_link(company_symbol,fields=["annualTotalRevenue"]):
    ''' Returns link for extracting data of company income statements on Yahoo Finance'''

    base_url = f"https://query1.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{company_symbol}?"
    currentTimeStamp = str(time()).split(".")[0]    

    fields_parameters = f"type={','.join(fields)}"
    date_parameters = f"&period1=493590046&period2={currentTimeStamp}"
    domain_parameters = f"&corsDomain=finance.yahoo.com"

    full_url = base_url + fields_parameters + date_parameters + domain_parameters
    return full_url