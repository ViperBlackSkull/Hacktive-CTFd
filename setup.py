import requests
import re
from bs4 import BeautifulSoup

# Define the target URL
base_url = "https://dev.hacktive.education"
setup_url = f"{base_url}/setup"

# Start a session
session = requests.Session()

# Fetch the setup page
print("[*] Fetching the setup page...")
response = session.get(setup_url)

if response.status_code != 200:
    print("[!] Failed to fetch setup page, status code:", response.status_code)
    exit(1)

# Extract nonce from JavaScript
print("[*] Extracting CSRF nonce...")
nonce_match = re.search(r"'csrfNonce':\s*\"([a-f0-9]+)\"", response.text)
if nonce_match:
    nonce = nonce_match.group(1)
    print("[+] Found CSRF nonce:", nonce)
else:
    print("[!] Failed to extract CSRF nonce.")
    exit(1)

# Define form data
ctf_name = "Developpement Hacktive Education"
ctf_description = "Event description of the CTFd instance"
user_mode = "users"
challenge_visibility = "private"
account_visibility = "public"
score_visibility = "public"
registration_visibility = "public"
verify_emails = "false"
team_size = ""
name = "viper"
email = "vipergrosman@hotmail.com"
password = "AdminPassword"
ctf_theme = "core-beta"
theme_color = ""
start = ""
end = ""

# Prepare multipart form data
files = {
    "ctf_logo": (None, "", "application/octet-stream"),
    "ctf_banner": (None, "", "application/octet-stream"),
    "ctf_small_icon": (None, "", "application/octet-stream"),
}

data = {
    "ctf_name": ctf_name,
    "ctf_description": ctf_description,
    "user_mode": user_mode,
    "challenge_visibility": challenge_visibility,
    "account_visibility": account_visibility,
    "score_visibility": score_visibility,
    "registration_visibility": registration_visibility,
    "verify_emails": verify_emails,
    "team_size": team_size,
    "name": name,
    "email": email,
    "password": password,
    "ctf_theme": ctf_theme,
    "theme_color": theme_color,
    "start": start,
    "end": end,
    "_submit": "Finish",
    "nonce": nonce,
}

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Origin": base_url,
    "Referer": setup_url,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-User": "?1",
    "Sec-Fetch-Dest": "document",
}

# Submit the setup form
print("[*] Submitting setup form...")
response = session.post(setup_url, data=data, files=files, headers=headers)

print("[+] Status Code:", response.status_code)
print("[+] Response Length:", len(response.text))

# Check if setup was successful
print("[*] Verifying setup success...")
home_response = session.get(base_url)

if "setup" in home_response.url:
    print("[!] Setup failed, still redirecting to setup page.")
    exit(1)
else:
    print("[+] Setup completed successfully!")
