# test_checkeroriginality.py
"""
Tests for CheckerOriginality module.
"""

import unittest
from checkeroriginality import CheckerOriginality

class TestCheckerOriginality(unittest.TestCase):
    """Test cases for CheckerOriginality class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CheckerOriginality()
        self.assertIsInstance(instance, CheckerOriginality)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CheckerOriginality()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
