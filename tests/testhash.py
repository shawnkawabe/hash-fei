# test_with_unittest.py

from unittest import TestCase

class TryTesting(TestCase):
  def test_uppercase(self):
    self.assertEqual( "loud noises".upper(), "LOUD NOISES")