import requests
import json
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))    # I need to understand this
from el_library import lines
from el_library import bar


def main():
    problem_set()


def problem_set():
    """
    In a file called bitcoin.py, implement a program that:
        - Expects the user to specify as a command-line argument the 
            number of Bitcoins, 𝑛, that they would like to buy. If that 
            argument cannot be converted to a float, the program should 
            exit via sys.exit with an error message.
        - Queries the API for the CoinCap Bitcoin Price Index at 
            rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should
            replace YourApiKey with the actual API key you obtained from 
            your CoinCap account dashboard, which returns a JSON object, 
            among whose nested keys is the current price of Bitcoin as a float. 
            Be sure to catch exceptions.
        - Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places,
            using , as a thousands separator.
    """

    # Solutions
    

    try:
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=7dd353ae112e671b2ae7434d98b19988ac1aacb3f27852a5a6718cce7c596416")
        response.raise_for_status()
    except requests.RequestException:
        print("Request failed!")
    else:
        print("Request succeeded!")     # Checking
        if len(sys.argv) < 2:
            print("Missing command-line argument")
        else:
            if not sys.argv[1].isdigit():
                print("command-line argument is not a number")
            else:
                # Make the conversion:
                m_bitcoin = float(sys.argv[1])
                data = response.json()["data"]
                us_dollars = float(data["priceUsd"])
                amount = m_bitcoin * us_dollars
                print(f"${amount:,.4f}")
                print("USD")    # Checking: display the corresponding price in USD
                lines(2)
                print(response.text)    # Checking






if __name__ == "__main__":
    main()