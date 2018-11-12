import requests

def main():
    res = requests.get("http://data.fixer.io/api/latest?access_key=35f5ad7056f50ad8f610a49200a67cf0&format=1&symbols=USD")
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    print(data)

if __name__ == "__main__":
    main()
