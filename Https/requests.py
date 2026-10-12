#: Call a safe public/sample endpoint if available in your environment, or inspect a provided JSON response offline.
import json
import logging
import urllib.request
import urllib.error

# Configure basic logging
logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)

# Safe, free public sample REST API endpoint
URL = "https://jsonplaceholder.typicode.com/todos/1"

def fetch_sample_data(endpoint_url: str):
    logging.info(f"Initiating GET request to {endpoint_url}")
    
    try:
        req = urllib.request.Request(endpoint_url, headers={"User-Agent": "Python/3.x"})
        with urllib.request.urlopen(req, timeout=5) as response:
            status_code = response.getcode()
            logging.info(f"Received HTTP {status_code} response.")
            
            # Read and decode JSON payload
            raw_data = response.read().decode("utf-8")
            data = json.loads(raw_data)
            
            logging.info("Successfully parsed JSON payload.")
            return data

    except urllib.error.HTTPError as e:
        logging.error(f"HTTP Error encountered: {e.code} - {e.reason}")
    except urllib.error.URLError as e:
        logging.error(f"Network error / URL unreachable: {e.reason}")
    except json.JSONDecodeError as e:
        logging.error(f"Failed to decode JSON output: {e}")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {e}")
        
    return None

# Execute network fetch
data = fetch_sample_data(URL)

if data:
    print("\n--- Parsed JSON Result ---")
    print(f"User ID   : {data.get('userId')}")
    print(f"ID        : {data.get('id')}")
    print(f"Title     : {data.get('title')}")
    print(f"Completed : {data.get('completed')}")