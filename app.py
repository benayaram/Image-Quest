from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# API credentials
UNSPLASH_ACCESS_KEY = '-FraqxuinfcshLREvU12OJYsVjUFvQLJuk7sCF7SmWg'

def search_images(query):
    url = f'https://api.unsplash.com/search/photos'
    headers = {'Authorization': f'Client-ID {UNSPLASH_ACCESS_KEY}'}
    params = {'query': query, 'per_page': 12}  # Limiting to 10 results for simplicity
    response = requests.get(url, headers=headers, params=params)
    data = response.json()
    return data['results']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
    images = search_images(query)
    return render_template('results.html', images=images)

if __name__ == '__main__':
    app.run()
