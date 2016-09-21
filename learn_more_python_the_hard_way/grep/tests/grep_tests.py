from nose.tools import *
from grep import utils
import re

def test_convert_patterns():
	# test that I can convert a list of patterns to expressions
	results = utils.convert_patterns(['.*.py'])
	# assert that they are equal to my expectations
	assert_equal(results, [re.compile('.*.py')])

def test_troll_directories():
	# given a directory, return all of its contents
	results = utils.troll_directories('.')
	# assert that we have the same contents
	assert_true('./NOTES' in results)

def test_apply_patterns():
	# get a list of directories
	files = utils.troll_directories('.')
	patterns = utils.convert_patterns(['.*.py'])
	# apply a simple pattern on them
	utils.apply_patterns(files, patterns)
	# assert that we get the right results