try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'The program gets a street address from the command line arguments or the clipboard.  It then opens the web browser to the Google Maps page for the supplied address.',
	'author': 'Sunny Lam',
	'url': 'URL to get it at',
	'download_url': 'Where to download it',
	'author_email': 'sunny.lam@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['webbrowser','sys'],
	'scripts': [],
	'name': 'Map It Demo Program Using the `webbrowser` module'
}

setup(**config)