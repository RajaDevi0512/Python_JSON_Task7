import requests

class MyBreweries:
    def __init__(self, url):
        self.url = url

    # Function to get breweries by state
    def get_breweries_by_state(self, state):
        params = {'by_state': state}
        response = requests.get(self.url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error fetching data for {state}. Status code: {response.status_code}")
            return []

    # Function to list all brewery names in the states
    def list_breweries(self, states):
        breweries_info = {}
        for state in states:
            breweries_info[state] = self.get_breweries_by_state(state)
            print(f"\nBreweries in {state}:")
            for brewery in breweries_info[state]:
                print(brewery['name'])
        print('-' * 30)
        return breweries_info

    # Function to count breweries in each state
    def count_breweries(self, breweries_info):
        for state, breweries in breweries_info.items():
            print(f"{state} has {len(breweries)} breweries.")

    # Function to count brewery types in each city of the states
    def count_brewery_types_by_city(self, breweries_info):
        for state, breweries in breweries_info.items():
            city_types = {}
            for brewery in breweries:
                city = brewery['city']
                brewery_type = brewery['brewery_type']
                if city not in city_types:
                    city_types[city] = set()
                city_types[city].add(brewery_type)
            print(f"\nBrewery types by city in {state}:")
            for city, types in city_types.items():
                print(f"{city}: {len(types)} types")
        print('-' * 30)

    # Function to count how many breweries have websites
    def count_breweries_with_websites(self, breweries_info):
        for state, breweries in breweries_info.items():
            count = sum(1 for brewery in breweries if brewery['website_url'])
            print(f"{state} has {count} breweries with websites.")
        print('-' * 30)

# List of states to query
states = ["Alaska", "Maine", "New York"]

# Instantiate the class
my_breweries = MyBreweries("https://api.openbrewerydb.org/v1/breweries")

# Get brewery information for the states
breweries_info = my_breweries.list_breweries(states)

# Count number of breweries in each state
my_breweries.count_breweries(breweries_info)

# Count brewery types by city
my_breweries.count_brewery_types_by_city(breweries_info)

# Count how many breweries have websites
my_breweries.count_breweries_with_websites(breweries_info)
