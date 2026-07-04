# Binance Futures Trading Bot (CLI)

## Overview

This project is a production-ready Command Line Interface (CLI) trading bot built in Python for the Binance USDT-M Futures Testnet. It allows users to place MARKET and LIMIT orders through a clean, modular architecture while following industry-standard software engineering practices.

The application focuses on secure API authentication, input validation, structured logging, exception handling, and reusable code organization.

---

## Features

- Place MARKET orders
- Place LIMIT orders
- Support BUY and SELL order sides
- Binance Futures Testnet integration
- Secure API key management using environment variables
- Command Line Interface using `argparse`
- Input validation
- Structured logging
- Graceful exception handling
- Modular project architecture

---

## Project Structure

```
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── logging_config.py
│   ├── orders.py
│   └── validators.py
│
├── cli.py
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

## Tech Stack

- Python 3.x
- python-binance
- argparse
- python-dotenv
- logging

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/makadiyavatsall/trading_bot.git
```

### 2. Navigate to the Project

```bash
cd trading_bot
```

### 3. Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_SECRET_KEY
```

> Never commit the `.env` file to GitHub.

---

## Binance Futures Testnet

Generate API credentials from your Binance Futures Testnet account and store them in the `.env` file before running the application.

Base URL

```
https://testnet.binancefuture.com
```

---

## Usage

### MARKET Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### LIMIT Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

---

## CLI Arguments

| Argument | Description | Required |
|----------|-------------|----------|
| `--symbol` | Trading Symbol (Example: BTCUSDT) | Yes |
| `--side` | BUY or SELL | Yes |
| `--type` | MARKET or LIMIT | Yes |
| `--quantity` | Order Quantity | Yes |
| `--price` | Limit Price (Required only for LIMIT orders) | Conditional |

---

## Logging

The application generates a log file named:

```
trading_bot.log
```

The log file records:

- Application events
- API requests
- API responses
- Errors
- Debug information

---

## Validation

The application validates:

- Trading Symbol
- Order Side
- Order Type
- Quantity
- Price (for LIMIT orders)

Invalid inputs are rejected before making API requests.

---

## Error Handling

The application gracefully handles:

- Invalid user input
- Missing API credentials
- Binance API exceptions
- Network failures
- Authentication errors

Detailed errors are written to the log file while user-friendly messages are displayed on the terminal.

---

## Assumptions

- A valid Binance Futures Testnet account is available.
- API credentials are correctly configured in the `.env` file.
- Internet connectivity is available.
- Successful order execution requires sufficient demo balance in the Binance Futures Testnet account.

---

## Future Improvements

- Stop-Limit Orders
- OCO Orders
- Grid Trading
- TWAP Execution
- Interactive CLI Menu
- Docker Support
- Unit Testing
- CI/CD Pipeline
- Configuration File Support

---

## Requirements

- Python 3.10 or later
- Binance Futures Testnet Account
- API Key
- Secret Key

---

## License

This project is developed for educational and interview evaluation purposes.

---

## Author

**Vatsal Makadiya**

GitHub: https://github.com/makadiyavatsall
