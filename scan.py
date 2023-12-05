#tested in python 3.11

import socket
import requests

import subprocess
import importlib.util

def portScan(host):
    ports = [21,22,23,25,53,80,111,135,139,443,445,3306,8080,9090]

    for port in ports:
        client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(0.1)
        code = client.connect_ex((host, port))
        if code == 0:
            try:
                service = socket.getservbyport(port)
                print ("Open port found: ", port, " - ", service)
            except:
                continue

def ipData(host):
    response = requests.get(f'http://ip-api.com/json/{host}')
    print (response.json())


def main():
    opcao = input("1 - Ip local, 2 ip externo")
    if opcao == '1':
        host = input("Enter a IP/Host: ")
        (portScan(host)
	
    elif opcao == '2':
        host = input("Enter a IP/Host: ")
        ipData(host)
        portScan(host)

if __name__ == "__main__":
    main()
