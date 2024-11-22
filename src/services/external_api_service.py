import requests

def fetch_external_data(api_url, params=None, headers=None):
    """
    Fetches data from an external API.
    """
    try:
        response = requests.get(api_url, params=params, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None

def post_to_external_api(api_url, data=None, headers=None):
    """
    Sends data to an external API.
    """
    try:
        response = requests.post(api_url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error posting data to API: {e}")
        return None