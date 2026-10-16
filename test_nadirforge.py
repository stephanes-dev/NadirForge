# test_nadirforge.py
"""
Tests for NadirForge module.
"""

import unittest
from nadirforge import NadirForge

class TestNadirForge(unittest.TestCase):
    """Test cases for NadirForge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NadirForge()
        self.assertIsInstance(instance, NadirForge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NadirForge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
