"""
cli.py

Command Line Interface for Binance Futures Trading Bot.
"""

import argparse
import traceback

from binance.exceptions import BinanceAPIException

from bot.client import BinanceClient
from bot.orders import OrderManager
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
from bot.logging_config import setup_logger

logger = setup_logger(__name__)


def main():
    print("\n========== Binance Futures Trading Bot ==========\n")

    parser = argparse.ArgumentParser(
        description="Binance Futures Trading Bot CLI"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="Trading Symbol (Example: BTCUSDT)"
    )

    parser.add_argument(
        "--side",
        required=True,
        choices=["BUY", "SELL"],
        help="Order Side"
    )

    parser.add_argument(
        "--type",
        required=True,
        choices=["MARKET", "LIMIT"],
        help="Order Type"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float,
        help="Order Quantity"
    )

    parser.add_argument(
        "--price",
        type=float,
        help="Price (Required for LIMIT Orders)"
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(args.symbol)
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)
        price = validate_price(args.price)

        print("✓ Inputs validated")

        client = BinanceClient().get_client()

        print("✓ Connected to Binance Testnet")

        trader = OrderManager(client)

        print("\n========== ORDER REQUEST ==========")
        print(f"Symbol      : {symbol}")
        print(f"Side        : {side}")
        print(f"Order Type  : {order_type}")
        print(f"Quantity    : {quantity}")

        if order_type == "LIMIT":
            if price is None:
                raise ValueError("LIMIT order requires --price")
            print(f"Price       : {price}")

        print("===================================\n")

        if order_type == "MARKET":
            response = trader.place_market_order(
                symbol=symbol,
                side=side,
                quantity=quantity
            )

        else:
            response = trader.place_limit_order(
                symbol=symbol,
                side=side,
                quantity=quantity,
                price=price
            )

        print("\n========== ORDER SUCCESS ==========")
        print(f"Order ID      : {response.get('orderId')}")
        print(f"Status        : {response.get('status')}")
        print(f"Executed Qty  : {response.get('executedQty')}")

        if "avgPrice" in response:
            print(f"Average Price : {response.get('avgPrice')}")

        print("===================================\n")

    except BinanceAPIException as e:
        logger.exception("Binance API Error")

        print("\n========== API ERROR ==========")
        print(f"Code    : {e.code}")
        print(f"Message : {e.message}")
        print("===============================\n")

    except Exception as e:
        logger.exception("Unexpected Error")

        print("\n========== ERROR ==========")
        print(str(e))
        print("===========================\n")

        traceback.print_exc()


if __name__ == "__main__":
    main()