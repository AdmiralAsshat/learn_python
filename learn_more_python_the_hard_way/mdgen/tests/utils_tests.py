from nose.tools import *
from mdgen import utils
import re

def test_troll_directories():
	# given a directory, return all of its contents
	results = utils.troll_directories('.')
	# assert that we have the same contents
	assert_true('./NOTES' in results)
