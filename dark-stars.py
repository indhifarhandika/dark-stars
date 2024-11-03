import time
import os
import subprocess

try:
    import requests
except Exception:
    print('[+] python3 requests is not installed')
    os.system('pip3 install requests')
    os.system('pip3 install requests[socks]')
    print('[!] python3 requests is installed ')

try:
    check_tor = subprocess.check_output('which tor', shell=True)
except subprocess.CalledProcessError:
    print('[+] tor is not installed !')
    subprocess.check_output('sudo apt update',shell=True)
    subprocess.check_output('sudo apt install tor -y',shell=True)
    print('[!] tor is installed succesfully ')

os.system("clear")

def ma_ip():
    url='http://checkip.amazonaws.com'
    proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    get_ip= requests.get(url, proxies=proxies)
    return get_ip.text

def change():
    os.system("brew services restart tor")
    time.sleep(5)
    print ('[+] Your IP has been Changed to : '+str(ma_ip()))

time.sleep(3)
println("==== DARK STARS by indhifarhandika ====")
print("\033[1;32;40m change your  SOCKES to 127.0.0.1:9050 \n")

print("Starting infinite IP change. Press Ctrl+C to stop.")
while True:
    try:
        time.sleep(20) 
        change() 
    except KeyboardInterrupt:
        print('\nAuto IP changer is closed.')
        break
