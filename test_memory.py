from unittest.mock import patch
import unittest

from main import main


class TestMemoryMonitor(unittest.TestCase):
    @patch('main.psutil.virtual_memory')
    @patch('main.requests.request')
    def test_memory_usage_above_threshold(self, mock_request, mock_virtual_memory):
        mock_virtual_memory.return_value.percent = 95
        main()
        mock_request.assert_called_once_with("POST", "http://your-api-address", data='{"message": "Alarm"}')

    @patch('main.psutil.virtual_memory')
    @patch('main.requests.request')
    def test_memory_usage_below_threshold(self, mock_request, mock_virtual_memory):
        mock_virtual_memory.return_value.percent = 80
        main()
        mock_request.assert_not_called()


if __name__ == "__main__":
    unittest.main()
