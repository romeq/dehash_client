#!/bin/python3

# Hash decryption: MD5, SHA1, SHA3, SHA256, SHA384, SHA512
# using dehash.lt api
import requests


def request_data(uhash: str):
    req = requests.get(f"https://api.dehash.lt/api.php?search={uhash}")
    if req.status_code != 200:
        print("Request failed. Invalid hash?")
        return -1
    else:
        result = req.text.split(':')[1].split('\n')[0]
        print(f"Result found: {result}")
        return 0


def run() -> int:
    uhash = input("Hash: ")
    request_data(uhash)
    return 0


if __name__ == "__main__":
    run()
