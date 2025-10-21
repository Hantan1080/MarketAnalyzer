# test_marketanalyzer.py
"""
Tests for MarketAnalyzer module.
"""

import unittest
from marketanalyzer import MarketAnalyzer

class TestMarketAnalyzer(unittest.TestCase):
    """Test cases for MarketAnalyzer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MarketAnalyzer()
        self.assertIsInstance(instance, MarketAnalyzer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MarketAnalyzer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
