import requests
from bs4 import BeautifulSoup

url = input("Enter website URL: ")

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    print("\nPage Title:")
    print(soup.title.string.strip())

    print("\nHeadings:\n")

    headings = soup.find_all(["h1", "h2", "h3"])

    count = 1

    for heading in headings:
        text = heading.get_text(" ", strip=True)

        if text:
            print(f"{count}. {text}")
            count += 1

    if count == 1:
        print("No headings found.")

except requests.exceptions.RequestException as e:
    print("Error:", e)