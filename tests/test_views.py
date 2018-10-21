import unittest
import os
import sys
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from app import app
from flask import session


class TestViews(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True
	def test_200(self):
		response = self.app.get("/")
		self.assertEqual(response.status_code,200)

if __name__ == '__main__':
    unittest.main()