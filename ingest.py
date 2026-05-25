import requests
from bs4 import BeautifulSoup

def fetch_financial_news():
    articles = []
    
    # Source: Reuters Business RSS (free, no login)
    feeds = [
        "https://feeds.reuters.com/reuters/businessNews",
        "https://feeds.reuters.com/reuters/technologyNews"
    ]
    
    for url in feeds:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, "xml")
            
            for item in soup.findAll("item")[:10]:
                title = item.title.text if item.title else ""
                desc = item.description.text if item.description else ""
                link = item.link.text if item.link else ""
                
                if title:
                    articles.append({
                        "title": title,
                        "content": desc,
                        "link": link
                    })
        except Exception as e:
            print(f"Error: {e}")
    
    # If RSS also fails, use hardcoded sample data
    if len(articles) == 0:
        print("⚠️ Using sample data...")
        articles = [
            {
                "title": "Apple reports record Q3 earnings",
                "content": "Apple Inc reported record revenue of $94 billion in Q3 2025, driven by strong iPhone and services growth. CEO Tim Cook highlighted AI features as a key growth driver.",
                "link": "https://example.com/apple-earnings"
            },
            {
                "title": "Microsoft Azure AI revenue surges 50%",
                "content": "Microsoft reported Azure cloud revenue grew 50% year over year, driven by enterprise AI adoption. The company raised its annual guidance citing strong demand for AI services.",
                "link": "https://example.com/microsoft-azure"
            },
            {
                "title": "Google DeepMind launches new AI model",
                "content": "Google DeepMind announced Gemini Ultra 2.0, claiming state of the art performance on financial reasoning benchmarks. Several major banks are already in pilot testing.",
                "link": "https://example.com/google-deepmind"
            },
            {
                "title": "Federal Reserve holds interest rates steady",
                "content": "The Federal Reserve kept interest rates unchanged at 5.25% citing stable inflation data. Markets rallied on the news with S&P 500 gaining 1.2% on the day.",
                "link": "https://example.com/fed-rates"
            },
            {
                "title": "Tesla stock rises after strong delivery numbers",
                "content": "Tesla reported 500,000 vehicle deliveries in Q3 2025, beating analyst expectations of 470,000. Stock rose 8% in after hours trading following the announcement.",
                "link": "https://example.com/tesla-deliveries"
            },
            {
                "title": "Amazon AWS launches financial AI services",
                "content": "Amazon Web Services introduced new AI tools specifically designed for financial institutions including fraud detection, risk assessment and automated trading compliance systems.",
                "link": "https://example.com/aws-finance"
            },
            {
                "title": "Indian stock market hits all time high",
                "content": "BSE Sensex crossed 85,000 points for the first time driven by strong FII inflows and positive GDP data. IT and banking sectors led the rally with gains of 3-4%.",
                "link": "https://example.com/sensex-high"
            },
            {
                "title": "Nvidia reports AI chip demand remains strong",
                "content": "Nvidia posted quarterly revenue of $26 billion with data center segment growing 400% year over year. CEO Jensen Huang said demand for AI chips continues to far exceed supply.",
                "link": "https://example.com/nvidia-chips"
            }
        ]
    
    print(f"✅ Fetched {len(articles)} articles!")
    return articles

# Test it
if __name__ == "__main__":
    articles = fetch_financial_news()
    for a in articles[:3]:
        print("📰", a["title"])