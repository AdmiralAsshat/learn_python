from nose.tools import *
from grep import utils
import re

def test_convert_patterns():
	# test that I can convert a list of patterns to expressions
	results = utils.convert_patterns(['.*.py'])
	# assert that they are equal to my expectations
	assert_equal(results, [re.compile('.*.py')])

def test_troll_directories():
	pass

def test_apply_patterns():
	pass