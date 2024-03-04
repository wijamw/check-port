import unittest
from unittest.mock import patch
from io import StringIO
from main import check_port

class TestCheckPort(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_check_port_output(self, mock_stdout):
        hostname = 'surabaya.go.id'
        port = 443
        check_port(hostname, port)
        output = mock_stdout.getvalue().strip()
        self.assertIsInstance(output, str, msg="Output should be a string")

if __name__ == '__main__':
    unittest.main()
