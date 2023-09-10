import requests
import time
from datetime import datetime

def fetch_exchange_rate():
    api_key = "a2be56bd1326c7655d13f584cbb35d2b"

    try:
        api_url = f"http://api.exchangeratesapi.io/v1/latest?access_key={api_key}&symbols=ILS&amount=1"
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception if the response status code is not 200
        data = response.json()
        return data["rates"]
    
    except requests.exceptions.RequestException as e:
        # We can improve this part by tracing the exception for later investigation
        return None
    
    except KeyError:
        # We can improve this part by tracing the exception for later investigation
        return None
    
def main():
    target_currency = "EUR to ILS"
    
    for hour in range(24):
        exchange_rate = fetch_exchange_rate()
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        if exchange_rate is not None:
            print(f"{timestamp} - 1 {target_currency} = {exchange_rate['ILS']}")
       
        else:
            print(f"{timestamp} - Failed to fetch data. Data will be collected in 1 hour.")
        
        time.sleep(60 * 60)  # Wait for 1 hour (60 seconds * 60 minutes)

if __name__ == "__main__":
    main()






