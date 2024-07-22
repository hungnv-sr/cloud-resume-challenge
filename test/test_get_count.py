import unittest
from unittest.mock import patch, MagicMock
import json
from src.get_count import get_count, lambda_handler

class TestCloudResumeChallenge(unittest.TestCase):

    @patch('src.get_count.table')
    @patch('src.get_count.Key')
    def test_get_count(self, mock_Key, mock_table):
        # Mock the Key object
        mock_Key.return_value.eq.return_value = 'mocked_condition'

        # Mock the query method of the table
        mock_table.query.side_effect = [
            {'Items': [{'visitors': '10'}]},
            {'Items': [{'requests': '20'}]}
        ]

        # Call the function
        result = get_count()

        # Assert the result
        expected_result = json.dumps({"visitors": 10, "requests": 20})
        self.assertEqual(result, expected_result)

        # Assert that query was called twice with correct arguments
        mock_table.query.assert_any_call(KeyConditionExpression='mocked_condition')
        mock_table.query.assert_any_call(KeyConditionExpression='mocked_condition')

        # Assert that Key was called correctly
        mock_Key.assert_any_call('ID')
        mock_Key.return_value.eq.assert_any_call('visitors')
        mock_Key.return_value.eq.assert_any_call('requests')

    @patch('src.get_count.get_count')
    def test_lambda_handler(self, mock_get_count):
        # Mock the get_count function
        mock_get_count.return_value = json.dumps({"visitors": 10, "requests": 20})

        # Call the lambda_handler
        result = lambda_handler(None, None)

        # Assert the result
        expected_result = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': '*',
                'Content-Type': 'application/json'
            },
            'body': json.dumps({"visitors": 10, "requests": 20})
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()