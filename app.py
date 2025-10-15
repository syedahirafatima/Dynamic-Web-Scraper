from flask import Flask, render_template, request, jsonify
from scraper import scrape_dynamic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    url = request.form.get('url')
    query = request.form.get('query')
    results = scrape_dynamic(url, query)
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
