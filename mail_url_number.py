import argparse
import os
import re
import datetime
from urllib.parse import urlparse, urljoin
import requests
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Web Scraping Tool")
parser.add_argument('-u', '--url', type=str, metavar='', help="URL to be scraped")
args = parser.parse_args()

url = args.url if args.url else input("Enter a URL to be scraped: ")

if not url.startswith('http'):
    url = 'https://' + url

parsed_url = urlparse(url if args.url else url)
domain_name = parsed_url.netloc

try:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string.strip()
    print(f"Title: {title}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
    exit()

emails = set()
matches = re.findall(r'[\w\.-]+@[\w\.-]+', str(soup))
for match in matches:
    emails.add(match)

numbers = set()
matches = re.findall(r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}', str(soup))
for match in matches:
    numbers.add(match)

links = set()
for link in soup.find_all('a'):
    href = link.get('href')
    if href is not None:
        href = urljoin(url, href)
        parsed_href = urlparse(href)
        if parsed_href.netloc == domain_name:
            links.add(href)

php_files = set()
for link in links:
    if link.endswith('.php'):
        php_files.add(link)
    elif link.startswith(url) and 'id=' in link and 'php' in link:
        php_files.add(link)

summary = f"Summary:\nEmails found: {len(emails)}\nPhone numbers found: {len(numbers)}\nLinks found: {len(links)}\nPHP files found: {len(php_files)}"
print(summary)

filename = f"{domain_name}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
with open(filename, 'w') as file:
    file.write(f"Title: {title}\n\n")
    file.write("Emails found:\n")
    for email in emails:
        file.write(f"- {email}\n")
    file.write("\nPhone numbers found:\n")
    for number in numbers:
        file.write(f"- {number}\n")
    file.write("\nLinks found:\n")
    for link in links:
        file.write(f"- {link}\n")
    file.write("\nPHP files found:\n")
    for php_file in php_files:
        file.write(f"- {php_file}\n")
print(f"Results saved in {filename}")
