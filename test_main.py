import unittest

from main import Board


class BoardTest(unittest.TestCase):
	def test_creation(self):
		testboard = Board(2, 2, 1)
		self.assertFalse(testboard.is_over)


unittest.main()
