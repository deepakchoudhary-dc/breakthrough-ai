import requests
from config import SERPAPI_KEY

def perform_search(query):
    url = "https://serpapi.com/search.json"
    params = {
        "q": query,
        "api_key": SERPAPI_KEY
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json().get("organic_results", [])
    except requests.RequestException as e:
        print(f"Error in perform_search: {e}")
        return None
