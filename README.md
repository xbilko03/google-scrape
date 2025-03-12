# Google Search Scraper

This project is a **Google Search Scraper** built using **Flask**. It interacts with the **Google Custom Search API** to retrieve search results in JSON format.

## Description
The application performs the following key tasks:

1. **Google API Key Integration**
   - The app uses an **API Key** and **Search Engine ID** from Google Custom Search to bypass Google's anti-bot protection and fetch search results programmatically

2. **Request Handling**
   - When a user submits a search query, the app constructs a URL that sends a request to the **Google Custom Search API**

3. **JSON Response Parsing**
   - The received data is parsed into a structured JSON format. Users can view this data directly in their browser or save it for further use

## How to Run the Server

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Create a `.env` file** and add your Google API credentials:
```
API_KEY=your_google_api_key
SEARCH_KEY=your_google_search_engine_id
```

3. **Run the application**
```bash
python app.py
```

4. **Access the web interface**
- Visit [http://localhost:5000](http://localhost:5000) in your browser and use search function

---

## Tests
The `test.py` file contains unit tests to ensure the functionality of the scraper behaves as expected

### Test Cases
1. **Successful Search Test**
   - Simulates a successful search request with mock data

2. **No Query Test**
   - Tests the behavior when no search query is provided

3. **No Results Found Test**
   - Simulates a search query that returns no results

### Running the Tests
To run the tests, use the following command:
```bash
python test.py
```

---

## Author
**Jozef Bilko (xbilko03)**

