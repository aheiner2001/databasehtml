import time
import requests

def keep_alive():
    url = "https://databasehtml.onrender.com/"  # Replace with your Render app URL
    while True:
        try:
            response = requests.get(url)
            print(f"Pinged {url}, Status Code: {response.status_code}")
        except Exception as e:
            print(f"Error pinging {url}: {e}")
        time.sleep(300)  # Wait 5 minutes between pings

if __name__ == "__main__":
    keep_alive()
