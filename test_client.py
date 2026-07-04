from bot.client import BinanceClient

client = BinanceClient().get_client()

print("Successfully Connected!")

account = client.futures_account()

print(account["feeTier"])