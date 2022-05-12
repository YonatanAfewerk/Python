import requests as rq
from datetime import datetime
import logging
import objectpath  # Read the library doc: http://objectpath.org/

logger = logging.getLogger(__name__)


def get_api_data(url):
    try:
        response = rq.get(url)
        response.raise_for_status()
        logger.debug("Getting API data - Done")
        api_data = response.json()
        logger.debug("Converting API data to JSON - Done")
        return api_data
    except Exception as e:
        logger.debug("Exception occurred.", exc_info=True)


def main():
    # CoinDesk API Link
    API_LINK = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    # Getting the data from API
    data = get_api_data(API_LINK)
    tree_data = objectpath.Tree(data)

    time = next(tree_data.execute('$..updated'))
    price = next(tree_data.execute('$..USD'))

    print(f"The price in {price['description']} - USD: {price['rate']}")
    print(f"Time of the price: {time}")


if __name__ == '__main__':
    LOG_FORMAT = '%(levelname)s : %(asctime)s - %(message)s'
    logging.basicConfig(level=logging.DEBUG,
                        format=LOG_FORMAT, filemode='w')
    main()
