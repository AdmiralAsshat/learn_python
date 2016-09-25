from nose.tools import *
from mdgen import utils
import re
import os

def test_troll_directories():
	# given a directory, return all of its contents
	results = utils.troll_directories('.')
	# assert that we have the same contents
	assert_true('./NOTES' in results)

def test_discover_targets():
	files = utils.troll_directories('docs')
	results = utils.discover_targets('docs', 'html', files)

	expecting = [('docs/index.md', 'html/index.html'), ('docs/stuff/index.md', 'html/stuff/index.html')]

	assert_equal(results, expecting)

def test_generate_html():
	source = 'docs/index.md'
	target = 'html/index.html'

	# remove file if already exists
	if os.path.exists(target):
		os.unlink(target)

	utils.generate_html(source, target)
	assert_true(os.path.exists(target))

def test_convert_md_directory():
	source = 'docs'
	target = 'html'
	expecting = target + '/index.html'

	# remove file if already exists
	if os.path.exists(expecting):
		os.unlink(expecting)

	utils.convert_md_directory(source, target)
	assert_true(os.path.exists(expecting))