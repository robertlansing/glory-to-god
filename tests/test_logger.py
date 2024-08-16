import unittest
from logger.logger import get_glory_logger

class TestGloryLogger(unittest.TestCase):
    def test_logger_initialization(self):
        logger = get_glory_logger('test')
        self.assertTrue(logger is not None)

if __name__ == '__main__':
    unittest.main()
