# -*- coding: utf-8 -*-
from FinMind.Data import Load
import requests
import pandas as pd

url = 'http://finmindapi.servebeer.com/api/data'
list_url = 'http://finmindapi.servebeer.com/api/datalist'
translate_url = 'http://finmindapi.servebeer.com/api/translation'

class StockDataGetter:
    """
    Using FinMind api to get stock and finance statsments data.
    input:
        dataset: list of string
        stock_id: list of string
        date: string. Data time interval is date ~ now
    output:
        pandas dataframe
    """
    def __init__(self, dataset=None, stock_id=None, date=None):
        self.dataset = dataset
        self.stock_id = stock_id
        self.date = date

    def stock_info_getter(self):
        form_data = {'dataset': 'TaiwanStockInfo'}
        res = requests.post(
            url, verify=True,
            data=form_data)

        temp = res.json()
        data = pd.DataFrame(temp['data'])
        return data

    def stock_data_getter(self, dataset, stock_id, date):
        form_data = {'dataset': dataset,
                     'stock_id': stock_id,
                     'date': date}
        res = requests.post(
            url, verify=True,
            data=form_data)

        temp = res.json()
        data = pd.DataFrame(temp['data'])
        return data

    def finance_statement_getter(self, dataset, stock_id, date):
        form_data = {'dataset': dataset,
                     'stock_id': stock_id,
                     'date': date}
        res = requests.post(
            url, verify=True,
            data=form_data)

        temp = res.json()
        data = pd.DataFrame(temp['data'])
        data = Load.transpose(data)
        return data
