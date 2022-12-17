import requests
import json

def recommend_airbnb(latitude, longitude):
  # Make a request to the Airbnb API to search for listings near the given latitude and longitude
  api_url = "https://api.airbnb.com/v2/search_results"
  params = {
    "client_id": "YOUR_CLIENT_ID",
    "locale": "en-US",
    "currency": "USD",
    "_limit": 1,
    "lat": latitude,
    "lng": longitude
  }
  response = requests.get(api_url, params=params)
  response_json = response.json()

  # Get the first listing from the search results
  listing = response_json["search_results"][0]

  # Print the listing's name and price
  print(f"Recommendation: {listing['name']} - ${listing['price']} per night")

# Test the function with a location in San Francisco
recommend_airbnb(37.7749, -122.4194)
