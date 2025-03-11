#
# Name		    : test.py
# Project	    : Google search scraper
# Description   : Tests the funcionality of app.py
#
# Author        : Jozef Bilko (xbilko03)
#
import unittest
import json
from app import app
from unittest.mock import patch

class FlaskAppTests(unittest.TestCase):

    # Mock test #
    @patch('requests.get')
    def test_search_success(self, mock_get):
        mock_response = {
            "items": [
                {
                    "title": "Test Title",
                    "link": "https://beer.com"
                },
                {
                    "title": "Test2",
                    "link": "https://gamer.com"
                }
            ]
        }
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # Run client and assert the mock response #
        with app.test_client() as client:
            response = client.get('/search?query=test')
            
            # Assert status code #
            self.assertEqual(response.status_code, 200)
            
            # Assert JSON #
            response_data = json.loads(response.data)
            self.assertEqual(len(response_data), 2)
            self.assertEqual(response_data[0]['title'], 'Test Title')
            self.assertEqual(response_data[0]['link'], 'https://beer.com')
            self.assertEqual(response_data[1]['title'], 'Test2')
            self.assertEqual(response_data[1]['link'], 'https://gamer.com')

    # No query test #
    @patch('requests.get')
    def test_search_no_query(self, mock_get):
        
        # Run client and assert empty query #
        with app.test_client() as client:
            response = client.get('/search')

            # Assert status code #
            self.assertEqual(response.status_code, 400)
            
            # Assert error #
            response_data = json.loads(response.data)
            self.assertEqual(response_data['error'], 'Please provide a search query.')

    # No results test #
    @patch('requests.get')
    def test_search_no_results(self, mock_get):
        mock_response = {
            "items": []
        }
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_response
        
        # Run client and assert empty result #
        with app.test_client() as client:
            response = client.get('/search?query=test')
            
            # Assert status code #
            self.assertEqual(response.status_code, 404)
            
            # Assert error #
            response_data = json.loads(response.data)
            self.assertEqual(response_data['error'], 'No results found.')

if __name__ == '__main__':
    unittest.main()
