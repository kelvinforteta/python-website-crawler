#!/usr/bin/env python

import requests

discovered_subdomains = []


def request(url):
    try:
        return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
        pass


print("Enter target URL")
target_url = input(">>> ")


def discover_subdomain():
    with open("subdomains.list", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = word + "." + target_url
            response = request(test_url)
            if response:
                discovered_subdomains.append(test_url)
                print("[+] Discovered subdomain --> " + test_url)


def discover_directory():
    with open("file_directory_word.list", "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = f"{target_url}/{word}"
            response = request(test_url)
            if response:
                discovered_subdomains.append(test_url)
                print("[+] Discovered file/directory --> " + test_url)


discover_directory()
