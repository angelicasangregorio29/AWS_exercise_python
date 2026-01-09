import urllib.parse
import urllib.request
import json

BASE_URL = "https://is.gd/create.php"

def shorten_url(url, alias=None):
    """
    Shorten a URL using is.gd API.
    Returns (short_url, error_message).
    """
    params = {
        'format': 'json',
        'url': url
    }
    if alias:
        params['shorturl'] = alias
        
    query_string = urllib.parse.urlencode(params)
    target_url = f"{BASE_URL}?{query_string}"
    
    try:
        # User-Agent is sometimes required by APIs to avoid 403
        req = urllib.request.Request(
            target_url, 
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response:
            if response.status != 200:
                return None, f"HTTP Error: {response.status}"
            
            try:
                data = json.loads(response.read().decode())
            except json.JSONDecodeError as e:
                 print(f"DEBUG: Failed to decode JSON. Raw response might be invalid.")
                 return None, f"JSON Decode Error: {e}"

            print(f"DEBUG: Raw API Response: {data}")
            
            if 'errorcode' in data:
                return None, f"API Error: {data.get('errormessage', 'Unknown error')}"
                
            if 'shorturl' in data:
                return data['shorturl'], None
                
            return None, "Invalid response from API"
            
    except urllib.error.URLError as e:
        return None, f"Network Error: {str(e)}"
    except Exception as e:
        return None, f"Error: {str(e)}"
