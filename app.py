from flask import Flask, render_template, request
import requests
import sqlite3

app = Flask(__name__)
url = f"https://api.pokemontcg.io/v2/cards"

@app.route('/')
def index():
    response = requests.get(url).json()
    img = response["data"][0]["images"]["large"]

    return render_template('index.html', img=img)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)