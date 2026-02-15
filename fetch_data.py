
import requests
from supabase import create_client

# פרטי החיבור המוכחים שלך
URL = "https://dwifoemfuvwvhkfekrky.supabase.co"
KEY = "sb_publishable_USB3t56P0aWyLOo6z-y-dg_X36TGa_t"
supabase = create_client(URL, KEY)

def get_full_scoreboard(sport, league):
    print(f"מושך נתונים עבור {sport} ({league})...")
    url = f"https://site.api.espn.com/apis/site/v2/sports/{sport}/{league}/scoreboard"
    try:
        res = requests.get(url).json()
        for event in res.get('events', []):
            game_id = event['id']
            name = event['shortName']
            status = event['status']['type']['shortDetail']
            
            # שליפת תוצאות
            competitors = event['competitions'][0]['competitors']
            score_h = competitors[0]['score']
            score_a = competitors[1]['score']
            
            # עדכון ב-Supabase
            supabase.table("matches").upsert({
                "id": int(game_id),
                "status": status,
                "score_home": int(score_h),
                "score_away": int(score_a)
            }).execute()
            print(f"עודכן: {name} | {status}")
    except Exception as e:
        print(f"שגיאה ב-{league}: {e}")

if __name__ == "__main__":
    get_full_scoreboard("soccer", "eng.1") # פרמייר ליג
    get_full_scoreboard("basketball", "nba") # NBA
