# pip install colorama
# pip install requests[socks] beautifulsoup4 stem


import requests
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

# Function to get the HTML content of a .onion link
def get_onion_content(url):
    session = requests.Session()
    session.proxies = {
        'http': 'socks5h://127.0.0.1:9050',
        'https': 'socks5h://127.0.0.1:9050'
    }
    try:
        response = session.get(url, timeout=30)
        if response.status_code == 200:
            return response.text
        else:
            print(f"{Fore.RED}Failed to retrieve {url} with status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}Error accessing {url}: {e}")
    return None

# Function to search for a specific value in the HTML content
def search_value_in_content(content, value):
    soup = BeautifulSoup(content, 'html.parser')
    if value in soup.text:
        print(f"{Fore.GREEN}Value '{value}' found!")
    else:
        print(f"{Fore.YELLOW}Value '{value}' not found.")

def main():
    onion_links = input("Enter the .onion links separated by commas: ").split(',')
    search_value = input("Enter the value to search for: ").strip()

    for link in onion_links:
        link = link.strip()
        if not link.startswith("http"):
            link = "http://" + link
        
        print(f"\n{Style.BRIGHT}Searching in {Fore.CYAN}{link}...")
        content = get_onion_content(link)
        if content:
            search_value_in_content(content, search_value)

if __name__ == "__main__":
    main()
