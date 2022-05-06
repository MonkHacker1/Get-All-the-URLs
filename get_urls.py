import requests
from bs4 import BeautifulSoup
import re
from colorama import Fore
import os
import time
from time import sleep
import readline

command = "toilet -f bigmono9 -F gay Aurls" #command to be executed

print("\n")
print(Fore.YELLOW+"-"*60)
print(Fore.RED+"""\n
                                   
                           ███          
        ██                   █          
        ██                   █          
       ▒██▒  █   █   █▒██▒   █    ▒███▒ 
       ▓▒▒▓  █   █   ██  █   █    █▒ ░█ 
       █░░█  █   █   █       █    █▒░   
       █  █  █   █   █       █    ░███▒ 
      ▒████▒ █   █   █       █       ▒█ 
      ▓▒  ▒▓ █▒ ▓█   █       █░   █░ ▒█ 
      █░  ░█ ▒██▒█   █       ▒██  ▒███▒ 


\n""")
print(Fore.YELLOW+"*"*60)
print(Fore.RED+"Coded By: Aamir Hussain"+Fore.YELLOW+"\t\t\t\t\t"+"   |")
print(Fore.YELLOW+"*"*60)
print("\n")
query=input(Fore.CYAN+"Enter the Search String: ")
print(Fore.RESET+"")
time.sleep(3)
print(Fore.GREEN+"Colloecting the urls.....")
type(query)
try:
    page = requests.get("https://www.google.dz/search?q="+str(query))
    soup = BeautifulSoup(page.content,"lxml")
    links = soup.findAll("a")
    cnt=0
    link_list=[]
    new_list=[]
    for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        cnt+=1
        link_list.append(re.split(":(?=http)",link["href"].replace("/url?q=","")))
    print(Fore.YELLOW+"-"*50)   
    print(Fore.RED+"SUCCESS! Total Number Of Links Found: ",cnt,Fore.YELLOW+" "+"\t"+" |")
    print(Fore.YELLOW+"-"*50)
    for urls in link_list:
        print(Fore.CYAN+"")
        print(Fore.RED+"> ",Fore.GREEN,*urls)   
    print(Fore.YELLOW+"\t\t\t\t\t"+"<"+"-"*50+"DONE"+"-"*50+">")  
except (requests.ConnectionError, requests.Timeout) as exception:
    print(Fore.RESET+"")
    print(Fore.RED+"Internet is off")
