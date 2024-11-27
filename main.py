import requests
import sys
import traceroute

def main():
    args = sys.argv

    if len(args) == 1:
        dst = "example.com"
    elif len(args) == 2:
        dst = args[1]
    else:
        print("Usage: python main.py <dst-address>")
        sys.exit(1)

    ip_addresses = traceroute.traceroute(dst)

    ip_addresses = sorted(set(ip_addresses), key=ip_addresses.index)

    for ip in ip_addresses:
        response = requests.get(f"https://ipinfo.io/{ip}/org")
        if response.status_code == 200:
            print(f"IP: {ip} (AS: {response.text.strip()})")
        else:
            print(f"IP: {ip} (Error fetching AS info)")
        
if __name__ == "__main__":
    main()
    
    