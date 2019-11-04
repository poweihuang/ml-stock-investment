# -*- coding: utf-8 -*-
import time
from functools import partial

import requests
import pandas as pd
from loguru import logger
from FinMind.Data import Load

URL = 'http://finmindapi.servebeer.com/api/data'
LIST_URL = 'http://finmindapi.servebeer.com/api/datalist'
TRANSLATE_URL = 'http://finmindapi.servebeer.com/api/translation'


def execute_query(query):
    content = query().json()

    if content['status'] == 500:
        logger.info('Retry later due to request limit.')
        time.sleep(60 * 60)
        return execute_query(query)

    if content['status'] == 200:
        try:
            return pd.DataFrame(content['data'])
        except KeyError:
            logger.error(content)
            return pd.DataFrame({})


class StockDataGetter:
    """
    Using FinMind api to get stock and finance statements data.
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
        query = partial(requests.post, URL, verify=True, data=form_data)
        return execute_query(query)

    @staticmethod
    def get_stock_data(dataset, stock_id, date):
        form_data = {'dataset': dataset, 'stock_id': stock_id, 'date': date}
        query = partial(requests.post, URL, verify=True, data=form_data)
        return execute_query(query)

    @staticmethod
    def get_finance_statement(dataset, stock_id, date):
        form_data = {'dataset': dataset, 'stock_id': stock_id, 'date': date}
        query = partial(requests.post, URL, verify=True, data=form_data)
        data = execute_query(query)
        return data if data.empty else Load.transpose(data)
