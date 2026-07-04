"""
client.py

Creates and returns a Binance Futures Testnet client.
"""

import os

from dotenv import load_dotenv
from binance.client import Client

from bot.logging_config import setup_logger

load_dotenv()

logger = setup_logger(__name__)


class BinanceClient:
    """Factory class for creating a Binance client."""

    TESTNET_URL = "https://testnet.binancefuture.com"

    def __init__(self) -> None:
        self.api_key = os.getenv("BINANCE_API_KEY")
        self.api_secret = os.getenv("BINANCE_API_SECRET")

        if not self.api_key:
            raise ValueError("BINANCE_API_KEY not found in .env")

        if not self.api_secret:
            raise ValueError("BINANCE_API_SECRET not found in .env")

    def get_client(self) -> Client:
        """
        Returns an authenticated Binance Client
        configured for Futures Testnet.
        """

        logger.info("Initializing Binance Client...")

        client = Client(
            api_key=self.api_key,
            api_secret=self.api_secret,
        )

        # Switch to Futures Testnet
        client.FUTURES_URL = self.TESTNET_URL + "/fapi"

        logger.info("Binance Futures Testnet client initialized successfully.")

        return client