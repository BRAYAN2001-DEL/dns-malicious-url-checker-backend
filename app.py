from flask import Flask, jsonify
from flask_cors import CORS
from dns_inventory import get_dns_records
from url_analysis import get_url_analysis

app = Flask(__name__)
CORS(app)  # Habilitar CORS en la aplicación Flask

@app.route('/dns/<domain>', methods=['GET'])
def dns_inventory(domain):
    records = get_dns_records(domain)
    return jsonify(records)

@app.route('/url/<path:url>', methods=['GET'])
def url_analysis(url):
    analysis = get_url_analysis(url)
    return jsonify(analysis)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
