import requests
from dotenv import load_dotenv
'''
loading environment variables, this allows me to obsfucate my API keys in a seperate folder
the benefit being that the unique keys belonging only ot me (and registered to me) are not
visible to others when I eventually create the repo and push to git
'''

import os

load_dotenv() #this loads my environment variables

def NASA_NEO():
   """
   Tests connection to NASA's Near Earth Object API
   Returns: bool indicating successful connections for each connection error
   """
   api_key = os.getenv('NASA_API_KEY') # calls the variable I declared in my .env file. 
   url = f"https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-01-24&end_date=2024-01-25&api_key={api_key}"  #f string that allows me to use the variable in a string
   
   try:
       print("🔄 Checking API connection...", end='\r')
       response = requests.get(url)
       print(" " * 30, end='\r')  # loading message so you know its doing something
       
       if response.status_code == 200:  # if connection is OK
           print("✅ API connection successful")
       elif response.status_code == 400:  # bad request
           print("⚠️ Bad request - check parameters")
       elif response.status_code == 401:  # lacks valid credentials
           print("🔒 Authentication failed - check API key")
       elif response.status_code == 403:  # forbidden
           print("🚫 Access forbidden - check permissions")
       elif response.status_code == 404:  # page not found
           print("❌ Endpoint not found")
       elif response.status_code == 429:  # too many requests
           print("⏳ Rate limit exceeded")
       elif response.status_code == 500:  # server error
           print("💥 Server error")
       elif response.status_code == 503:  # service unavailable
           print("🔧 Service temporarily unavailable")
       else:
           print(f"⚠️ Unexpected status code: {response.status_code}")
       return response.status_code == 200
   except requests.exceptions.RequestException as e:
       print(f"❌ Connection error: {e}")
       return False

if __name__ == "__main__":
   NASA_NEO()