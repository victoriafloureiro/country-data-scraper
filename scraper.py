import requests
from bs4 import BeautifulSoup
import csv

# Target URL (Substitui pelo link do site que se usa)
URL = "https://www.scrapethissite.com/pages/simple/" 
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def scrape_countries():
    print("[*] Starting country data extraction...")
    response = requests.get(URL, headers=HEADERS)
    
    if response.status_code != 200:
        print(f"[!] Failed to fetch data. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    countries_data = []

    # Exemplo de extração (Ajusta os seletores conforme o projeto)
    # rows = soup.find_all("div", class_="country-row")
    
    print("[*] Parsing data and formatting...")
    # Lógica de loop aqui

    # Guardar os dados em CSV
    with open("countries_data.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Country Name", "Capital", "Population", "Area (sq km)"]) # Headers
        writer.writerows(countries_data)
        
    print("[+] Success! Data saved to countries_data.csv")

if __name__ == "__main__":
    scrape_countries()
