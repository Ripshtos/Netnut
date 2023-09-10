import yfinance as yf
import time
from datetime import datetime

def fetch_currency_exchange_rate(currency_pair):
    try:
        currency_data = yf.Ticker(currency_pair)
        current_price = currency_data.history(period='1m')['Close'].iloc[-1]
        return current_price
    
    except Exception as e:
        print('Error fetching exchange rate:', str(e))
        return None

def main():
    currency_pair = 'USDILS=X'  # Convert from USD to ILS 
    target_currency = 'ILS' 
    
    print(f'Collecting the USD to ILS exchange rate data every hour for 24 hours:')
    
    for i in range(24):
        exchange_rate = fetch_currency_exchange_rate(currency_pair)
        
        if exchange_rate is not None:
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(f'{current_time}: 1 {currency_pair[:3]} = {exchange_rate} {target_currency}')

        if exchange_rate is None:
            print(f'Error fetching data from api, will try again in one hour.')

        # Sleep for an hour 
        time.sleep(3600)

if __name__ == "__main__":
    main()