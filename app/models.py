from pydantic import BaseModel

class Venue(BaseModel):
    id: int
    venue_name: str
    venue_type: str | None
    venue_add_one: str | None
    venue_web: str | None
    latitude: float | None
    longitude: float | None
    wday_opening: str | None
    wday_closing: str | None
    wkd_opening: str | None
    wkd_closing: str | None
    variations: str | None
    venue_capacity: str | None
    instagram: str | None
    quartiere: str | None
  
