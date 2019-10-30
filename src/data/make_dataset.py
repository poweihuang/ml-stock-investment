# -*- coding: utf-8 -*-
import os
import logging
from src.data.stock_getter import StockDataGetter


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    file_path = "../../data/"
    logger = logging.getLogger(__name__)
    logger.info('making data set from raw data')
    SDG = StockDataGetter()
    stock_info = SDG.get_stock_info()
    stock_info.to_csv('../../data/stock_info.csv')

    stock_list = ['TaiwanStockPrice', 'TaiwanCashFlowsStatement', 'TaiwanStockMarginPurchaseShortSale',
             'InstitutionalInvestorsBuySell', 'Shareholding', 'BalanceSheet', 'TaiwanStockHoldingSharesPer',
             'TaiwanStockMonthRevenue', 'TaiwanOption']
    finance = ['FinancialStatements', 'StockDividend']
    stock_id = '2882'

    for stock in stock_list:
        stock_data = SDG.get_stock_data(stock, stock_id, '2019-01-01')
        stock_id = stock_id
        stock_list = stock
        if os.path.isfile(f'{stock_id}-{stock_list}.csv'):
            stock_data.to_csv(file_path + f'{stock_id}-{stock_list}.csv', mode='a', header=False)
        else:
            stock_data.to_csv(file_path + f'{stock_id}-{stock_list}.csv')


    for fin in finance:
        fin_stat = SDG.get_finance_statement(fin, stock_id, '2019-01-01')
        if os.path.isfile(f'{stock_id}-{fin}.csv'):
            fin_stat.to_csv(file_path+f'{stock_id}-{fin}.csv', mode='a', header=False)
        else:
            fin_stat.to_csv(file_path+f'{stock_id}-{fin}.csv')



if __name__ == '__main__':
    main()