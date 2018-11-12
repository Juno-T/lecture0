import requests

def main():
    base = "EUR"
    cur = input("Currency: ")
    res = requests.get("http://data.fixer.io/api/latest?access_key=35f5ad7056f50ad8f610a49200a67cf0&format=1",
                       params={"symbols": cur})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = data["rates"][cur]
    print(f"1 {base} is equal to {rate} {cur}")

if __name__ == "__main__":
    main()
