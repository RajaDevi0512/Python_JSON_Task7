import requests

class MyrestCountries:
    def __init__ (self,url):
        self.url = url

    def status_test(self):
        response = requests.get(self.url)
        return response.status_code
    
    def fetch_api_data(self):
        if self.status_test() == 200:
            return requests.get(self.url).json()
        else:
            return "ERROR - 404"
        
    def fetch_country_currency_currencySymbol(self):
        if self.status_test() == 200:
            data = self.fetch_api_data()
            for country_data in data:
                country_name = country_data.get('name', {}).get('common', 'No name available')
                currencies = country_data.get('currencies', {})

                if currencies:
                    for currency_data, currency_info in currencies.items():
                        currency_name = currency_info.get('name', 'No currency name')
                        currency_symbol = currency_info.get('symbol', 'No symbol')
                        print(f"COUNTRY: {country_name}")
                        print(f"Currency: {currency_name}")
                        print(f"Currency Symbol: {currency_symbol}")
                        print('-' * 30)
                else:
                    print(f"COUNTRY: {country_name}")
                    print("No currency information available")
                    print('-' * 30)

    def fetch_countries_with_dollar_symbol(self):
        # Method to fetch countries that use "$" as the currency symbol
        if self.status_test() == 200:
            data = self.fetch_api_data()  # Get the API data
            print("Countries using the '$' currency symbol:")
            for country_data in data:
                # Extract the country name from the data
                country_name = country_data.get('name', {}).get('common', 'No name available')
                # Extract the currencies data
                currencies = country_data.get('currencies', {})
                
                # Loop through each currency and check for the "$" symbol
                for currency_code, currency_info in currencies.items():
                    # Check if the symbol is "$"
                    if currency_info.get('symbol', '') == '$':
                        print(f"COUNTRY: {country_name} - Currency: {currency_info['name']} - Symbol: {currency_info['symbol']}")
            print('-' * 30)
    
    
    def fetch_countries_with_euro_symbol(self):
        # Method to fetch countries that use "€" as the currency symbol
        if self.status_test() == 200:
            data = self.fetch_api_data()  # Get the API data
            print("Countries using the '€' currency symbol:")
            for country_data in data:
                # Extract the country name from the data
                country_name = country_data.get('name', {}).get('common', 'No name available')
                # Extract the currencies data
                currencies = country_data.get('currencies', {})
                
                # Loop through each currency and check for the "€" symbol
                for currency_code, currency_info in currencies.items():
                    # Check if the symbol is "€"
                    if currency_info.get('symbol', '') == '€':
                        print(f"COUNTRY: {country_name} - Currency: {currency_info['name']} - Symbol: {currency_info['symbol']}")
            print('-' * 30)
            
# Instantiate and call the methods
fetch_object = MyrestCountries('https://restcountries.com/v3.1/all')   

# Call to test the status
print(fetch_object.status_test())

# Call to fetch all api data
print(fetch_object.fetch_api_data())

# Call to display countries with their currency and symbol
fetch_object.fetch_country_currency_currencySymbol()

# Call to display countries with Dollar
fetch_object.fetch_countries_with_dollar_symbol()

# Call to display countries with Euro
fetch_object.fetch_countries_with_euro_symbol()

