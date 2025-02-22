from typing import Union

from fastapi import FastAPI
from app.models import Venue
from db.supabase import create_supabase_client

app = FastAPI()

# Initialize supabase client
supabase = create_supabase_client()
app.get("/")(lambda: {"Welcome": "To Florence"})

# Retrieve a venue
@app.get("/venue")
def get_venue(venue_id: Union[str, None] = None):
    try:
        if venue_id:
            venue = supabase.from_("florence_open_data")\
                .select("id", "venue_name")\
                .eq("id", venue_id)\
                .execute()

            if venue:
                return venue
        else:
            venues = supabase.from_("florence_open_data")\
                .select("id", "venue_name")\
                .execute()
            if venues:
                return venues
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "venue not found"}