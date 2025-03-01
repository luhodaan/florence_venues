from typing import List, Union

from fastapi import FastAPI
from app.models import Venue
from db.supabase import create_supabase_client

app = FastAPI()

# Initialize supabase client
supabase = create_supabase_client()
app.get("/")(lambda: {"Welcome": "To Florence"})

# Retrieve a single venue
@app.get("/venue/{venue_id}", response_model=Venue)
def get_venue(venue_id: str):
    try:
        venue = supabase.from_("florence_open_data")\
            .select("id, venue_name, venue_type, venue_add_one, venue_web, latitude, longitude, wday_opening, wday_closing, wkd_opening, wkd_closing, variations, venue_capacity, instagram, quartiere")\
            .eq("id", venue_id)\
            .execute()

        if venue and venue.data:
            return venue.data[0]
        return {"message": "venue not found"}
    except Exception as e:
        print(f"Error: {e}")
        return {"message": "venue not found"}

# Retrieve all venues
@app.get("/venues", response_model=List[Venue])
def get_venues():
    try:
        venues = supabase.from_("florence_open_data")\
            .select("id, venue_name, venue_type, venue_add_one, venue_web, latitude, longitude, wday_opening, wday_closing, wkd_opening, wkd_closing, variations, venue_capacity, instagram, quartiere")\
            .execute()
        
        if venues and venues.data:
            return venues.data
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []