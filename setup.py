from setuptools import setup

setup(
	name = 'panjareh',
	version = '0.0.01',
	description = 'Sliding Window library for image processing in Python',
	url = 'https://github.com/mohseniaref/panjareh',
	author = 'Mohammad Mohseni Aref',
	author_email = 'mohseni.aref@gmail.com',
	license = 'MIT',
	packages = ['panjareh'],
	zip_safe = True,
	install_requires = [
		'numpy',
		'psutil'
	]
)
