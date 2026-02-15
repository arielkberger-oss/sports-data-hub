import requests
from supabase import create_client

# פרטי החיבור שלך - כבר מוטמעים
URL = "https://dwifoemfuvwvhkfekrky.supabase.co"
KEY = "sb_publishable_USB3t56P0aWyLOo6z-y-dg_X36TGa_t"
supabase = create_client(URL, KEY)

def run_check():
    print("--- שלב 1: בדיקת חיבור ל-Supabase ---")
    try:
        # ננסה להכניס שורת בדיקה
        test_row = {"id": 1, "status": "LIVE_TEST", "score_home": 7, "score_away": 7}
        supabase.table("matches").upsert(test_row).execute()
        print("✅ הצלחתי לעדכן את הטבלה ב-Supabase!")
    except Exception as e:
        print(f"❌ שגיאה בחיבור ל-Supabase: {e}")

    print("\n--- שלב 2: בדיקת נתונים מ-ESPN ---")
    try:
        url = "https://site.api.espn.com/apis/site/v2/sports/soccer/scorepanel"
        res = requests.get(url).json()
        leagues = res.get('leagues', [])
        print(f"נמצאו {len(leagues)} ליגות פעילות ב-ESPN.")
        
        for league in leagues:
            for event in league.get('events', []):
                print(f"נמצא משחק: {event.get('name')}")
    except Exception as e:
        print(f"❌ שגיאה במשיכת נתונים מ-ESPN: {e}")

if __name__ == "__main__":
    print("הסקריפט התחיל לרוץ...")
    run_check()
    print("הסקריפט סיים.")
