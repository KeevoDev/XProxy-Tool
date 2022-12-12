import os
import pystyle
import colorama
import requests
import threading
import time
import datetime
import json
from colorama import *

version = 'v1'
author = 'Keevo'
filename = 'XProxy'



title_menu = '[XProxy] - Main Menu'


def getCurrentTime():
    return datetime.datetime.utcnow().strftime('%H:%M:%S')

class xproxy():
    def https():
        print(f"""
        {Fore.YELLOW} __  ______                      
        {Fore.YELLOW} \ \/ /  _ \ _ __ _____  ___   _     {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Developed By:{Fore.GREEN} {author} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  \  /| |_) | '__/ _ \ \/ / | | |    {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Current Version:{Fore.GREEN} {version} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  /  \|  __/| | | (_) >  <| |_| |    {Fore.RESET}|
        {Fore.YELLOW} /_/\_\_|   |_|  \___/_/\_\\__, |     {Fore.RESET}|
        {Fore.YELLOW}                           |___/     {Fore.RESET}|
        """)
        with open(r"Results\HTTPS.txt", 'r') as fp:
            scraped_https = len(fp.readlines())
        os.system(f'title [XProxy] - Type: HTTPS ^| Scraped: {scraped_https}')
        r1  = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all")
        f = open(f'Results\HTTPS.txt','wb')
        f.write(r1.content)
        f.close()
        print()
        print(f"                                      {Fore.RESET}( {Fore.GREEN}*{Fore.RESET} ) {Fore.GREEN}Scraped {Fore.RESET}{scraped_https}{Fore.GREEN} HTTPS Proxies")
        time.sleep(3)
    def socks4():
        print(f"""
        {Fore.YELLOW} __  ______                      
        {Fore.YELLOW} \ \/ /  _ \ _ __ _____  ___   _     {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Developed By:{Fore.GREEN} {author} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  \  /| |_) | '__/ _ \ \/ / | | |    {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Current Version:{Fore.GREEN} {version} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  /  \|  __/| | | (_) >  <| |_| |    {Fore.RESET}|
        {Fore.YELLOW} /_/\_\_|   |_|  \___/_/\_\\__, |     {Fore.RESET}|
        {Fore.YELLOW}                           |___/     {Fore.RESET}|
        """)
        with open(r"Results\SOCKS4.txt", 'r') as fp:
            scraped_socks4 = len(fp.readlines())
        os.system(f'title [XProxy] - Type: SOCKS4 ^| Scraped: {scraped_socks4}')
        r1  = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all&ssl=all&anonymity=all")
        f = open(f'Results\SOCKS4.txt','wb')
        f.write(r1.content)
        f.close()
        print()
        print(f"                                      {Fore.RESET}( {Fore.GREEN}*{Fore.RESET} ) {Fore.GREEN}Scraped {Fore.RESET}{scraped_socks4}{Fore.GREEN} SOCKS4 Proxies")
        time.sleep(3)
    def socks5():
        print(f"""
        {Fore.YELLOW} __  ______                      
        {Fore.YELLOW} \ \/ /  _ \ _ __ _____  ___   _     {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Developed By:{Fore.GREEN} {author} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  \  /| |_) | '__/ _ \ \/ / | | |    {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Current Version:{Fore.GREEN} {version} {Fore.RESET})
        {Fore.LIGHTYELLOW_EX}  /  \|  __/| | | (_) >  <| |_| |    {Fore.RESET}|
        {Fore.YELLOW} /_/\_\_|   |_|  \___/_/\_\\__, |     {Fore.RESET}|
        {Fore.YELLOW}                           |___/     {Fore.RESET}|
        """)
        with open(r"Results\SOCKS5.txt", 'r') as fp:
            scraped_socks5 = len(fp.readlines())
        os.system(f'title [XProxy] - Type: SOCKS5 ^| Scraped: {scraped_socks5}')
        r1  = requests.get("https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all")
        f = open(f'Results\SOCKS5.txt','wb')
        f.write(r1.content)
        f.close()
        print()
        print(f"                                      {Fore.RESET}( {Fore.GREEN}*{Fore.RESET} ) {Fore.GREEN}Scraped {Fore.RESET}{scraped_socks5}{Fore.GREEN} SOCKS5 Proxies")
        time.sleep(3)


def menu():
    os.system(f"title {title_menu}")
    os.system(f"cls")
    print(f"""
    {Fore.YELLOW} __  ______                      
    {Fore.YELLOW} \ \/ /  _ \ _ __ _____  ___   _     {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Developed By:{Fore.GREEN} {author} {Fore.RESET})
    {Fore.LIGHTYELLOW_EX}  \  /| |_) | '__/ _ \ \/ / | | |    {Fore.RESET}|         {Fore.RESET}( {Fore.LIGHTRED_EX} Current Version:{Fore.GREEN} {version} {Fore.RESET})
    {Fore.LIGHTYELLOW_EX}  /  \|  __/| | | (_) >  <| |_| |    {Fore.RESET}|
    {Fore.YELLOW} /_/\_\_|   |_|  \___/_/\_\\__, |     {Fore.RESET}|
    {Fore.YELLOW}                           |___/     {Fore.RESET}|
    """)
    print(f"""
                    +══════════════════════════════╦════════════════════════════════+
                    |      {Fore.LIGHTCYAN_EX}<1> {Fore.RESET}Scrape HTTPs        |   {Fore.LIGHTCYAN_EX}>  {Fore.RESET}Scraping "{Fore.CYAN}HTTPS{Fore.RESET}" Proxies  |
                    |      {Fore.LIGHTCYAN_EX}<2> {Fore.RESET}Scrape SOCKS4       |   {Fore.LIGHTCYAN_EX}>  {Fore.RESET}Scraping "{Fore.CYAN}SOCKS4{Fore.RESET}" Proxies |
                    |      {Fore.LIGHTCYAN_EX}<3> {Fore.RESET}Scrape SOCKS5       |   {Fore.LIGHTCYAN_EX}>  {Fore.RESET}Scraping "{Fore.CYAN}SOCKS5{Fore.RESET}" Proxies |
                    +══════════════════════════════╧════════════════════════════════+     
    """)
    print()
    choice = input(f"                                         {Fore.YELLOW}> {Fore.RESET}")
    choice = int(choice)
    if choice == 1:
        os.system("cls")
        xproxy.https()
    if choice == 2:
        os.system("cls")
        xproxy.socks4()
    if choice == 3:
        os.system("cls")
        xproxy.socks5()
menu()