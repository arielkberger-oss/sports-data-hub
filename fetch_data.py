import requests
from bs4 import BeautifulSoup
from supabase import create_client

# פרטי החיבור האישיים שלך
URL = "https://dwifoemfuvwvhkfekrky.supabase.co"
KEY = "sb_publishable_USB3t56P0aWyLOo6z-y-dg_X36TGa_t"
supabase = create_client(URL, KEY)

def get_live_scores():
    print("שואב תוצאות חיות מ-ESPN...")
    espn_url = "https://site.api.espn.com/apis/site/v2/sports/soccer/scorepanel"
    try:
        response = requests.get(espn_url).json()
        for league in response.get('leagues', []):
            for event in league.get('events', []):
                comp = event['competitions'][0]
                home = comp['competitors'][0]['team']['displayName']
                away = comp['competitors'][1]['team']['displayName']
                score_home = comp['competitors'][0]['score']
                score_away = comp['competitors'][1]['score']
                print(f"{home} {score_home} - {score_away} {away}")
    except Exception as e:
        print(f"שגיאת ESPN: {e}")

def get_sport5_news():
    print("שואב כותרות מספורט 5...")
    try:
        res = requests.get("https://www.sport5.co.il/")
        soup = BeautifulSoup(res.content, 'html.parser')
        headlines = soup.select('.main-article-h2, .news-item-h2')
        for h in headlines[:5]:
            print(f"חדשות: {h.get_text().strip()}")
    except Exception as e:
        print(f"שגיאת ספורט 5: {e}")

if __name__ == "__main__":
    get_live_scores()
    get_sport5_news()
