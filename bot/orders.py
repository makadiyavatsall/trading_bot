"""
orders.py

Business logic for placing Binance Futures orders.
"""

from binance.enums import (
    SIDE_BUY,
    SIDE_SELL,
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_LIMIT,
    TIME_IN_FORCE_GTC,
)

from bot.logging_config import setup_logger

logger = setup_logger(__name__)


class OrderManager:
    """Handles order placement."""

    def __init__(self, client):
        self.client = client

    def place_market_order(self, symbol, side, quantity):
        logger.info("Placing MARKET order")

        return self.client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity,
        )

    def place_limit_order(self, symbol, side, quantity, price):
        logger.info("Placing LIMIT order")

        return self.client.futures_create_order(
            symbol=symbol,
            side=SIDE_BUY if side == "BUY" else SIDE_SELL,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC,
        )