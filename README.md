
# 🍪 Automated Cookie Clicker Bot

A simple Python bot that plays the [Cookie Clicker game](https://orteil.dashnet.org/experiments/cookie/) automatically using Selenium WebDriver.

This bot simulates clicking the cookie and purchases upgrades from the store to maximize cookie production.

## 🔧 Features

- Automatically clicks the cookie.
- Purchases the most expensive affordable upgrades every 20 seconds.
- Runs for a set number of upgrade cycles (default: 20).
- Uses Selenium and ChromeDriver.

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Google Chrome browser

Install required Python package:
```bash
pip install selenium
```

### Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Dinesh99673/Automated-Cookie-Clicker.git
   cd Automated-Cookie-Clicker
   ```

2. Ensure `chromedriver` is in your system PATH or in the same directory as the script.

3. Run the script:
   ```bash
   py main.py
   ```

## 🧠 How It Works

- The bot loads the game using Selenium.
- It continuously clicks the cookie for 20 seconds.
- After each cycle, it checks your cookie count and buys the most expensive upgrade you can afford.
- Repeats the process for 20 upgrade cycles. (you can change this number)

## 🛠 Technologies Used

- Python 🐍
- Selenium WebDriver
- Chrome + ChromeDriver

## 📸 Screenshot

![Screenshot 2025-06-09 113357](https://github.com/user-attachments/assets/e9aea679-e046-4095-8ada-65ed38b5a8d4)
