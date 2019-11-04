# -*- coding: utf-8 -*-
import csv

from loguru import logger
from tqdm import tqdm

from src.configs import DIRECTORY
from src.data.stock_getter import StockDataGetter

STOCK_DATASET = ['TaiwanStockPrice', 'TaiwanCashFlowsStatement', 'TaiwanStockMarginPurchaseShortSale',
                 'InstitutionalInvestorsBuySell', 'Shareholding', 'BalanceSheet', 'TaiwanStockHoldingSharesPer',
                 'TaiwanStockMonthRevenue', 'TaiwanOption']
FINANCE_DATASET = ['FinancialStatements', 'StockDividend']
START_DATE = '2019-01-01'
TARGET_CATEGORIES = ['ETF', '半導體業', '電機機械', '電子零組件類']

CSV_DIR = DIRECTORY.CSV_DATA


def create_dataset_dirs():
    dirs = STOCK_DATASET + FINANCE_DATASET
    for d in dirs:
        p = CSV_DIR.joinpath(d)
        if not p.exists():
            p.mkdir()


def download_stock_data(stock_id):
    for dataset in STOCK_DATASET:
        stock_data = sdg.get_stock_data(dataset, stock_id, START_DATE)
        stock_file = CSV_DIR.joinpath(dataset, f'{stock_id}.csv')

        if stock_file.exists():
            stock_data.to_csv(stock_file, mode='a', header=False)
        else:
            stock_data.to_csv(stock_file)

    for dataset in FINANCE_DATASET:
        fin_stat = sdg.get_finance_statement(dataset, stock_id, START_DATE)
        fin_file = CSV_DIR.joinpath(dataset, f'{stock_id}.csv')

        if fin_file.exists():
            fin_stat.to_csv(fin_file, mode='a', header=False)
        else:
            fin_stat.to_csv(fin_file)


def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger.info('making data set from raw data')
    stock_info_file = CSV_DIR.joinpath('stock_info.csv')
    stock_info = sdg.get_stock_info()
    stock_info.to_csv(stock_info_file)

    with stock_info_file.open() as f:
        # idx 1 is category
        rows = [row for row in csv.reader(f) if row[1] in TARGET_CATEGORIES]

    for row in tqdm(rows):
        # idx 2 is stock_id
        download_stock_data(row[2])


if __name__ == '__main__':
    create_dataset_dirs()
    sdg = StockDataGetter()
    main()
