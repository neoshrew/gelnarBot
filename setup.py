from setuptools import setup

setup(
	name='gelnar_bot',
	version='0.1a',
	author="Andrew Gelnar",
	packages=['gelnar_bot'],
	install_requires=[
		'irc',
	],
	entry_points={
		'console_scripts': [
			'gelnarBot=gelnar_bot:main',
		],
	},
)
