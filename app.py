#
# Name		    : app.py
# Project	    : Google search scraper
# Description   : Parses google search results and shows them as a JSON file
#
# Author        : Jozef Bilko (xbilko03)
#
import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify

# SETUP #
app = Flask(__name__)
load_dotenv()

# Get API Key #
# https://console.cloud.google.com/ #
API_KEY = os.getenv("API_KEY")

# Get Search Engine ID #
# https://developers.google.com/custom-search #
SEARCH_KEY = os.getenv("SEARCH_KEY")

# Show index.html #
@app.route('/')
def index():
    return render_template('index.html')

# Show search result #
@app.route('/search', methods=['GET'])

def search():
    query = request.args.get('query')

    if not query:
        return jsonify({"error": "Please provide a search query."}), 400

    # Build the Google Custom Search API URL #
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={SEARCH_KEY}"

    # Send request to Google API #
    response = requests.get(url)

    # Print the full HTTP response for debugging purposes #
    # print("Status Code:", response.status_code)
    # print("Headers:", response.headers)
    # print("Response Body:", response.text)

    # Parse JSON response #
    results = response.json()

    # Check for valid results #
    if "items" in results and results["items"]:
        search_results = [
            {"title": item["title"], "link": item["link"]}
            for item in results["items"]
        ]
        return jsonify(search_results)
    else:
        return jsonify({"error": "No results found."}), 404

# RUN #
if __name__ == '__main__':
    app.run()