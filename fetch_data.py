import requests
from supabase import create_client

URL = "https://dwifoemfuvwvhkfekrky.supabase.co"
KEY = "sb_publishable_USB3t56P0aWyLOo6z-y-dg_X36TGa_t"
supabase = create_client(URL, KEY)

def save_to_supabase(home, away, score_h, score_a):
    # פונקציה שמכניסה נתונים לטבלת המשחקים שיצרת
    try:
        supabase.table("matches").upsert({
            "id": hash(home + away) % 1000000, # מזהה זמני
            "status": "LIVE",
            "score_home": score_h,
            "score_away": score_a
            # כאן אפשר להוסיף עוד שדות לפי הטבלה שלך
        }).execute()
        print(f"Saved: {home} vs {away}")
    except Exception as e:
        print(f"Error saving: {e}")

def get_live_scores():
    espn_url = "https://site.api.espn.com/apis/site/v2/sports/soccer/scorepanel"
    res = requests.get(espn_url).json()
    for league in res.get('leagues', []):
        for event in league.get('events', []):
            comp = event['competitions'][0]
            home = comp['competitors'][0]['team']['displayName']
            away = comp['competitors'][1]['team']['displayName']
            s_h = comp['competitors'][0]['score']
            s_a = comp['competitors'][1]['score']
            save_to_supabase(home, away, s_h, s_a)

if __name__ == "__main__":
    get_live_scores()
