import requests
import base64

VIRUSTOTAL_API_KEY = '4833db36ffe63ef1c5750ff9eb802f7a92ea0d1a30713fcaac64903ce2956d74'

def get_url_analysis(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    headers = {
        'x-apikey': VIRUSTOTAL_API_KEY
    }
    response = requests.get(f'https://www.virustotal.com/api/v3/urls/{url_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return {}
