"""import requests
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
        return {}"""




import requests
import base64
import mysql.connector

VIRUSTOTAL_API_KEY = '4833db36ffe63ef1c5750ff9eb802f7a92ea0d1a30713fcaac64903ce2956d74'

# Configuración de la conexión a MySQL
mysql_connection = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='admin',
    database='dns'
)

def save_to_mysql(url_name, url_id, first_submission_date):
    cursor = mysql_connection.cursor()
    insert_query = "INSERT INTO url_analysis_data (url_id, url_name, first_submission_date) VALUES (%s, %s, %s)"
    cursor.execute(insert_query, (url_id, url_name, first_submission_date))
    mysql_connection.commit()
    cursor.close()

def get_url_analysis(url):
    url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    url_name = url  # Assuming the URL itself can serve as its name for simplicity
    headers = {
        'x-apikey': VIRUSTOTAL_API_KEY
    }
    response = requests.get(f'https://www.virustotal.com/api/v3/urls/{url_id}', headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        first_submission_date = data.get('data', {}).get('attributes', {}).get('first_submission_date', '')
        if first_submission_date:
            save_to_mysql(url_name, url_id, first_submission_date)
        return data
    else:
        return {}
