from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

CODES = {
    'ADMIN2024TEST': {'days': 30, 'used': False},
    'USER7DAYS': {'days': 7, 'used': False},
    'TRIAL1DAY': {'days': 1, 'used': False},
}

CARDS = [
    {'name': 'Fakka 20', 'price': 11.5, 'units': 550, 'days': 7, 'type': 'Fakka'},
    {'name': 'Fakka 25', 'price': 15.5, 'units': 625, 'days': 7, 'type': 'Fakka'},
    {'name': 'Fakka 26', 'price': 17.5, 'units': 650, 'days': 10, 'type': 'Fakka'},
    {'name': 'Mared 10', 'price': 10.5, 'units': 400, 'days': 7, 'type': 'Mared'},
    {'name': 'Social 7', 'price': 7, 'units': 300, 'days': 3, 'type': 'Social'},
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({'status': 'online', 'app': 'VF Cash'})

@app.route('/api/verify-code', methods=['POST'])
def verify_code():
    code = request.json.get('code', '').upper()
    if code not in CODES:
        return jsonify({'success': False, 'message': '❌ خطأ'}), 401
    if CODES[code]['used']:
        return jsonify({'success': False, 'message': '❌ مستخدم'}), 401
    CODES[code]['used'] = True
    return jsonify({'success': True, 'message': '✅ OK'}), 200

@app.route('/api/get-cards', methods=['GET'])
def get_cards():
    return jsonify({'success': True, 'cards': CARDS})

@app.route('/api/charge', methods=['POST'])
def charge():
    return jsonify({'success': True, 'message': '✅ OK'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
