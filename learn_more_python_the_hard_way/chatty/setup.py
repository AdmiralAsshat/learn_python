try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

confg = {
	'description': 'My Project',
	'author': 'My Name',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it.',
	'author_email': 'My email.',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['chatty'],
	'scripts': [],
	'name': 'chatty'
}

setup(**config)
