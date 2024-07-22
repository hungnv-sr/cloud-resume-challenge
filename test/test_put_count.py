import unittest
from unittest.mock import patch, MagicMock
from src.put_count import lambda_handler

class TestCloudResumeChallengeVisitorUpdater(unittest.TestCase):

    @patch('src.put_count.table')
    def test_lambda_handler(self, mock_table):
        # Mock the update_item method of the table
        mock_update_item = MagicMock()
        mock_table.update_item = mock_update_item

        # Call the lambda_handler
        result = lambda_handler(None, None)

        # Assert that update_item was called with correct arguments
        mock_update_item.assert_called_once_with(
            Key={
                'ID': 'visitors'
            },
            UpdateExpression='ADD visitors :incr',
            ExpressionAttributeValues={
                ':incr': 1
            },
            ReturnValues="UPDATED_NEW"
        )

        # Assert the result
        expected_result = {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': '*',
                'Access-Control-Allow-Credentials': '*',
                'Content-Type': 'application/json'
            }
        }
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
