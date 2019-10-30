# -*- coding: utf-8 -*-
import requests
import pandas as pd
from FinMind.Data import Load

URL = 'http://finmindapi.servebeer.com/api/data'
LIST_URL = 'http://finmindapi.servebeer.com/api/datalist'
TRANSLATE_URL = 'http://finmindapi.servebeer.com/api/translation'


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

    @staticmethod
    def get_stock_info():
        form_data = {'dataset': 'TaiwanStockInfo'}
        res = requests.post(
            URL, verify=True,
            data=form_data)

        data = pd.DataFrame(res.json()['data'])
        return data

    @staticmethod
    def get_stock_data(dataset, stock_id, date):
        form_data = {'dataset': dataset,
                     'stock_id': stock_id,
                     'date': date}
        res = requests.post(
            URL, verify=True,
            data=form_data)

        data = pd.DataFrame(res.json()['data'])
        return data

    @staticmethod
    def get_finance_statement(dataset, stock_id, date):
        form_data = {'dataset': dataset,
                     'stock_id': stock_id,
                     'date': date}
        res = requests.post(
            URL, verify=True,
            data=form_data)

        data = pd.DataFrame(res.json()['data'])
        data = Load.transpose(data)
        return data
