import requests
import json


def main():

    try:
        response = requests.get("https://example.com")
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Request failed: {error}")
    else:
        print("Request succeeded!")


if __name__ == "__main__":
    main()