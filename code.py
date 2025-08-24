import requests
from bs4 import BeautifulSoup

def scrape_hackernews():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch the page")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.select(".titleline a")  # select article titles

    print("\nTop Articles from Hacker News:\n")
    for i, article in enumerate(articles[:10], start=1):  # limit to first 10
        title = article.get_text()
        link = article.get("href")
        print(f"{i}. {title} ({link})")

if __name__ == "__main__":
    scrape_hackernews()
