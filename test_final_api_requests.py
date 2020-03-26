import unittest
import make_requests
from unittest.mock import patch, mock_open
import json
from io import StringIO


def test_url(self):
	result = make_requests.test_url()
    self.assertRaisesRegex(ValueError, r'[a-zA-Z0-9.-]+\.(com|edu|net|gov)')

def test_request_response():
    # Send a request to the API server and store the response.
    response = requests.get('http://jsonplaceholder.typicode.com/todos')
    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

def test_build_file():

def test_load_json(self):
    sample_json = StringIO ('{"name": "John", "shares": "100", "price": 1230.23}')

    with patch('urllib.request.urlopen') as url_patch:
    	with patch('json.load') as j_patch:
            url_patch.return_value.__enter__.return_value = sample_json
            res = make_requests.load_json('test', file_counter=0)
            j_patch.assert_called_with({})

if __name__ == '__main__':
    unittest.main()