import os
from dotenv import load_dotenv
from supabase import Client, create_client

# Load environment variables from .env file
load_dotenv()

api_url: str = os.getenv("url")
key: str = os.getenv("api")

def create_supabase_client():
    supabase: Client = create_client(api_url, key)
    return supabase
