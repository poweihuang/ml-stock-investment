# -*- coding: utf-8 -*-
# import click
import logging
# from pathlib import Path
# from dotenv import find_dotenv, load_dotenv
from src.data.stock_getter import StockDataGetter
import os

# @click.command()
# @click.argument('input_filepath', type=click.Path(exists=True))
# @click.argument('output_filepath', type=click.Path())
def main():
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    file_path = "../../data/"
    logger = logging.getLogger(__name__)
    logger.info('making data set from raw data')
    SDG = StockDataGetter()
    stock_info = SDG.stock_info_getter()
    stock_info.to_csv('../../data/stock_info.csv')

    stock_list = ['TaiwanStockPrice', 'TaiwanCashFlowsStatement', 'TaiwanStockMarginPurchaseShortSale',
             'InstitutionalInvestorsBuySell', 'Shareholding', 'BalanceSheet', 'TaiwanStockHoldingSharesPer',
             'TaiwanStockMonthRevenue', 'TaiwanOption']
    finance = ['FinancialStatements', 'StockDividend']
    stock_id = '2882'

    for stock in stock_list:
        stock_data = SDG.stock_data_getter(stock, stock_id, '2019-01-01')
        if not os.path.isfile('{stock_id}-{stock_list}.csv'.format(stock_id=stock_id, stock_list=stock)):
            stock_data.to_csv(file_path+'{stock_id}-{stock_list}.csv'.format(stock_id=stock_id, stock_list=stock))
        else:
            stock_data.to_csv(file_path + '{stock_id}-{stock_list}.csv'.format(stock_id=stock_id, stock_list=stock), mode='a', header=False)

    for fin in finance:
        fin_stat = SDG.finance_statement_getter(fin, stock_id, '2019-01-01')
        if not os.path.isfile('{stock_id}-{fin_stat}.csv'.format(stock_id=stock_id, fin_stat=fin)):
            fin_stat.to_csv(file_path+'{stock_id}-{fin_stat}.csv'.format(stock_id=stock_id, fin_stat=fin))
        else:
            fin_stat.to_csv(file_path+'{stock_id}-{fin_stat}.csv'.format(stock_id=stock_id, fin_stat=fin), mode='a', header=False)


if __name__ == '__main__':
    main()
    # log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # logging.basicConfig(level=logging.INFO, format=log_fmt)
    #
    # # not used in this stub but often useful for finding various files
    # project_dir = Path(__file__).resolve().parents[2]
    #
    # # find .env automagically by walking up directories until it's found, then
    # # load up the .env entries as environment variables
    # load_dotenv(find_dotenv())
    #
    # main()
