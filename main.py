from strategies.moving_average import execute_moving_average_strategy
from utils.logger import setup_logger
from config import SYMBOL, SHORT_WINDOW, LONG_WINDOW, QUANTITY


logger = setup_logger()

if __name__ == "__main__":
    logger.info("Starting the trading bot...")
    execute_moving_average_strategy(SYMBOL, SHORT_WINDOW, LONG_WINDOW, QUANTITY)
