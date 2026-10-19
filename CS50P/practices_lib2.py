import requests


def main():

    try:
        response = requests.get("example.com")
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"Request failed: {error}")


if __name__ == "__main__":
    main()