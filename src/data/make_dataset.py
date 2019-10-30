# -*- coding: utf-8 -*-
from loguru import logger

from src.configs import DIRECTORY
from src.data.stock_getter import StockDataGetter

stock_dataset = ['TaiwanStockPrice', 'TaiwanCashFlowsStatement', 'TaiwanStockMarginPurchaseShortSale',
                 'InstitutionalInvestorsBuySell', 'Shareholding', 'BalanceSheet', 'TaiwanStockHoldingSharesPer',
                 'TaiwanStockMonthRevenue', 'TaiwanOption']
finance_dataset = ['FinancialStatements', 'StockDividend']
stock_id = '2882'
start_date = '2019-01-01'
csv_dir = DIRECTORY.CSV_DATA


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger.info('making data set from raw data')
    sdg = StockDataGetter()
    stock_info = sdg.get_stock_info()
    stock_info.to_csv(csv_dir.joinpath('stock_info.csv'))

    for dataset in stock_dataset:
        stock_data = sdg.get_stock_data(dataset, stock_id, start_date)
        stock_file = csv_dir.joinpath(f'{stock_id}-{dataset}.csv')

        if stock_file.exists():
            stock_data.to_csv(stock_file, mode='a', header=False)
        else:
            stock_data.to_csv(stock_file)

    for dataset in finance_dataset:
        fin_stat = sdg.get_finance_statement(dataset, stock_id, start_date)
        fin_file = csv_dir.joinpath(f'{stock_id}-{dataset}.csv')

        if fin_file.exists():
            fin_stat.to_csv(fin_file, mode='a', header=False)
        else:
            fin_stat.to_csv(fin_file)


if __name__ == '__main__':
    main()
